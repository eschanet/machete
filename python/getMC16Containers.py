#!/usr/bin/env python

"""
Use rucio to get the xAOD information for a given DSID.
"""

def commandline():
  from optparse import OptionParser,OptionGroup
  usage   = "usage: %prog [options] DSID"
  version = "%prog v1.0"
  parser  = OptionParser(usage=usage,version=version)
  parser.add_option("-v","--verbose", dest="verbose", action="store_true",help="print more information (default: %default)")
  parser.add_option("-x","--debug",   dest="debug",   action="store_true",help="print debug information (default: %default)")
  parser.add_option("-d","--dsid",    dest="dsid",    action="store",     help="input DSID (default: %default)")
  parser.add_option("-c","--campaign",dest="campaign",action="store",     help="input campaign (default: %default)")
  parser.set_defaults(verbose=False,debug=False,dsid=None,campaign="MC16a,MC16c")
  (opts, args) = parser.parse_args()
  verbose = opts.verbose
  debug   = opts.debug
  if debug: verbose = True
  if not opts.dsid:
    parser.error("Give 6-digit DISD number as argument")
  return opts.dsid, opts.campaign.split(','), debug, verbose

def main(argv=None):
  import pprint
  pp = pprint.PrettyPrinter(indent=1)
  try:
    from rucio.client.didclient import DIDClient
    try: 
      client = DIDClient()
    except:
      print "Failed to get DIDClient"
      return
  except:
    print "Please first setup rucio"
    return
  if argv is None: argv = sys.argv
  dsid, campaigns, debug, verbose = commandline();
  if verbose:
    print (__doc__)
  scope = "mc16_13TeV"
  name = scope + "." + dsid + ".*.merge.AOD.*"
  #name = scope + "." + dsid + ".*.recon.AOD.*"
  if verbose: 
    print "Inputs:", scope, dsid, name
    print
  dids = {'name': name}

  count = 0
  datasetList = DIDClient.list_dids(client,scope,dids,'container')
  for dsn in datasetList:
    count += 1
    container = dsn
    contevents=0
    contcampaigns=[]
    matchcampaign=False
    if ':' in container:
      scope = container.split(':')[0]
      container = container.split(':')[1]
    else:
      scope = container.split('.')[0]

    contents = DIDClient.list_content(client,scope,container)

    for task in contents:
      name = task['name']
      scope = name.split('.')[0]
      if debug:
        print name

      meta = DIDClient.get_metadata(client,scope,name)
      if debug:
        pp.pprint(meta)
      campaign = meta['campaign'].split(':')[1]
      if debug:
        print campaign
      if campaign in campaigns:
        matchcampaign=True
      dsnInfo  = DIDClient.list_files(client,scope,name)
      events = 0
      for data in dsnInfo:
        events += int(data['events'])
      if debug:
        print events


      contevents+=events
      if campaign not in contcampaigns: contcampaigns.append(campaign)
    if matchcampaign:
      print '%10s %10s %s' % (",".join(contcampaigns), str(contevents), container)

  if count == 0: print "No merge.AOD containers for", dsid, "found [", name, "]"

import sys
if __name__ == '__main__':
  sys.exit(main())


