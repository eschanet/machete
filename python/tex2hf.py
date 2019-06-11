#!/usr/bin/env python3

'''
This script transforms tex systematic tables into histfitter config files. It's incredibly versatile.
(No, of course it is not versatile, stupid! What world are you living in, wake up! This only works for very specific cases and is ugly anyway.)
'''

import os
import sys
import argparse
import collections
import mmap
import pprint
import math
from itertools import tee

import logging
from commonHelpers.logger import logger
logger = logger.getChild("mephisto")

parser = argparse.ArgumentParser(description='Transform tex systematic tables into histfitter config files')
parser.add_argument('files', type=argparse.FileType('r'), nargs='+', help='List of files that you want to convert into HF file')
parser.add_argument('-b', '--backgrounds', nargs='+', help='List of backgrounds that are used to automatically detect which file is used', default=["ttbar", "wjets", "zjets", "vh", "tth", "diboson", "multiboson", "singletop", "ttv"])
parser.add_argument('-s', '--systematics', nargs='+', help='List of systematic variation names to be considered', default=["CKKW","QSF","RenormFac","PDF"])
parser.add_argument('-a', '--analysis', help='What analysis to consider. Currently supported: 1Lbb and strong1L')
parser.add_argument('-r', '--regions', nargs='+', help='List of regions of interest')
# parser.add_argument('-r', '--regions', nargs='+', help='List of regions of interest')

args = parser.parse_args()

if not (args.analysis or (args.backgrounds and args.regions)):
    logger.error('No analysis nor processes/regions given! Dropping out.')
    sys.exit()
elif not args.analysis and (args.backgrounds and args.regions):
    logger.info('Did not provide analysis, but provided backgrounds and regions, so lets guess.')
if args.analysis:
    logger.info('Considering analysis: %s' % args.analysis)
    if args.analysis == '1Lbb':
        args.backgrounds = ["ttbar", "wjets", "zjets", "vh", "tth", "diboson", "multiboson", "singletop", "ttv"]
        args.regions = ['SRLMincl','SRMMincl','SRHMincl','SRLM','SRMM','SRHM','WR','STCR','TRLM','TRMM','TRHM','VRtt1on','VRtt2on','VRtt3on','VRtt1off','VRtt2off','VRtt3off']
    elif args.analysis == 'strong1L':
        args.backgrounds = ["ttbar", "wjets", "zjets", "vh", "tth", "diboson", "multiboson", "singletop", "ttv"]
        regions = ['SR2J','SR4Jhighx','SR4Jlowx','SR6J', 'TR2J', 'WR2J', 'TR4Jhighx', 'WR4Jhighx', 'TR4Jlowx', 'WR4Jlowx', 'TR6J', 'WR6J', 'VR2Jmet','VR2Jmt', 'VR4Jhighxapl', 'VR4Jhighxmt','VR4Jlowxhybrid','VR4Jlowxapl','VR6Japl','VR6Jmt']
        meff_binning = collections.OrderedDict()
        meff_binning["2J"] = [700.,1150.,1600.,2050.,2500.]
        meff_binning["4Jlowx"] = [1000.,1600.,2200.,2800.]
        meff_binning["4Jhighx"] = [1000.,1600.,2200.,2800.]
        meff_binning["6J"] = [700.,1400,2100,2800,3500.]

        for region in regions:
            for tower,bins in meff_binning.iteritems():
                if tower in region:
                    logger.debug('Tower %s in %s' % (tower,region))
                    if "VR"+tower in region:
                        #we are in VR, so dont differentiate between BTEM and BVEM
                        for i,bin in enumerate(bins[:-1]):
                            args.regions.append(region+btag+"_bin{}".format(i+1))
                    else:
                        for btag in ["BVEM", "BTEM"]:
                            for i,bin in enumerate(bins[:-1]):
                                args.regions.append(region+btag+"_bin{}".format(i+1))

    else:
        logger.error('Analysis not known. Dropping out.')
        sys.exit()

#first, get some dictionary ready with the necessary structure
values = collections.OrderedDict()
for sys in args.systematics:
    values[sys] = collections.OrderedDict()
    for r in args.regions:
        values[sys][r] = {"up":[], "down":[]}

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def getRegionFromExpression(expr):
    if args.analysis == '1Lbb':
        if expr == 'SRLM' or expr == 'SRMM' or expr == 'SRHM':
            return 0
        if expr == 'SRLMincl' or expr == 'SRMMincl' or expr == 'SRHMincl':
            return expr
        if 'SRLM' in expr:
            return 'SRLM'
        if 'SRMM' in expr:
            return 'SRMM'
        if 'SRHM' in expr:
            return 'SRHM'
    elif args.analysis == 'strong1L':
        return expr
    for region in args.regions:
        if expr == region:
            return expr
    else:
        logger.error('Region not found: {}'.format(expr))
        return 0


for f in args.files:
    logger.info('Got file: {}'.format(os.path.basename(f.name)))
    if not os.path.basename(f.name)[-4:] == ".tex":
        logger.error('This is not a tex file. Do not try to fool me again! Skipping...')
        continue

    #check if we can get a background matched!
    b_matches = [b for b in args.backgrounds if b.lower() in os.path.basename(f.name).lower()]
    if len(b_matches) > 1:
        logger.warning('Found more than one background process matching filename: {}'.format(b_matches))
        logger.warning('Will only take first one.')
    elif len(b_matches) == 1:
        logger.info('Found process: {}'.format(b_matches[0]))
    elif len(b_matches) == 0:
        logger.error('No process found! Dropping out.')
        sys.exit()
    background = b_matches[0]

    #now check if we can get the systematic variation name matched
    sys_matches = [s for s in args.systematics if s.lower() in os.path.basename(f.name).lower()]
    if len(sys_matches) > 1:
        logger.warning('Found more than one systematic variation matching filename: {}'.format(sys_matches))
        logger.warning('Will only take first one.')
    elif len(sys_matches) == 1:
        logger.info('Found systematic variation: {}'.format(sys_matches[0]))
    elif len(sys_matches) == 0:
        logger.error('No systematic variation found! Dropping out.')
        sys.exit()
    systematic = sys_matches[0]

    ##let's check if we are using an up or a down variation (or symmetric...)
    is_up = False
    is_down = False
    if "up" in os.path.basename(f.name).lower():
        is_up = True
        logger.info('This should be an UP variation.')
    elif "down" in os.path.basename(f.name).lower():
        is_down = True
        logger.info('This should be a DOWN variation.')
    else:
        logger.warning('Probably neither up nor down, but a symmetrised table. Sure?')
    ##now comes the ugly parsing part
    ##can we do this at least not too ugly?

    lines = []
    #first, get the relevant part from the tex file. If the user has made it easy and tagged the respective parts with %tex2hf, we can simply use what's between it
    keywords = False
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if s.find(b'tex2hf') != -1:
            logger.info('Found keywords in file, so now we can just use what is between them')
            keywords = True
    if keywords == True:
        copy = False
        for line in f:
            if "tex2hf" in line.strip():
                copy = not copy
                continue
            elif copy:
                lines.append(line.strip())
    else:
        #otherwise just drop out, I don't want to think about this any further ...
        logger.error('You need to provide keywords. I am too lazy to think about something else. Put "tex2hf" before the first and after the last line (as a comment of course, you do not want this to show up in the table, do you?).')
        sys.exit()

    for line in lines:
        #get rid of any symbols we don't need
        line = line.strip().replace("$","").replace("\\","")
        #latex columns, get the region first. Need to strip all whitespace
        region = "".join(line.split("&")[0].split())
        region = getRegionFromExpression(region)
        if region == 0:
            continue
        #then the uncertainty, usually in the last column

        # print("{} : {}".format(region, line.split("&")[-1]))
        uncertainty = round(float(line.split("&")[-1].replace("pm","").replace("%","").strip())/100,4)
        # print(uncertainty)
        if is_up:
            if uncertainty < -1.0:
                uncertainty = -1.0
                logger.warning('Uncertainty larger than 100%. Truncating to 1.-1.')
            values[systematic][region]["up"].append(uncertainty)
        elif is_down:
            if uncertainty < -1.0:
                uncertainty = -1.0
                logger.warning('Uncertainty larger than 100%. Truncating to 1.-1.')
            values[systematic][region]["down"].append(uncertainty)
        else:
            up_unc = abs(uncertainty)
            down_unc = -up_unc
            if abs(uncertainty) > 1.0:
                logger.warning('Uncertainty larger than 100%. Truncating to 1.-1.')
                down_unc = -1
            values[systematic][region]["up"].append(up_unc)
            values[systematic][region]["down"].append(down_unc)

# pprint.pprint(values)



##
##
## Now let's start writing some HF configs ...
##
##

header = r'''
import ROOT
from ROOT import gSystem
gSystem.Load("libSusyFitter.so")

from systematic import Systematic
from configManager import configMgr
'''

if args.analysis == 'strong1L':
    header += r'''
Regions = [ 'BVEM', 'BTEM' ]
MeffBins = [ '_bin1', '_bin2', '_bin3', '_bin4']
'''

header += r'''
{}Systematics={{}}
'''.format(background)

if args.analysis == '1Lbb':

    main = r''''''

    for sys,d in values.items():
        main += '''
    '''
        for region,uncertainties in d.items():
            up_uncertainties = uncertainties["up"]
            down_uncertainties = uncertainties["down"]
            ups = ""
            for up_unc in up_uncertainties:
                if up_unc > 0:
                    up_unc = "+{}".format(abs(up_unc))
                else:
                    up_unc = "-{}".format(abs(up_unc))
                ups += "(1.{}),".format(up_unc)
            downs = ""
            for down_unc in down_uncertainties:
                if down_unc > 0:
                    down_unc = "+{}".format(abs(down_unc))
                else:
                    down_unc = "-{}".format(abs(down_unc))
                downs += "(1.{}),".format(down_unc)
            ups = ups[:-1]
            downs = downs[:-1]

            main += '''{bkg}Systematics['{bkg}{syst}_{region}'] = Systematic("{bkg}{syst}", configMgr.weights, [{ups}], [{downs}], "user","userHistoSys")
'''.format(bkg = background, syst = sys, region = region, ups=ups, downs=downs)

    footer = r'''
def TheorUnc(generatorSyst):
    for key in {bkg}Systematics:
        name=key.split('_')[-1]

        if "SRLMincl" in name:
            generatorSyst.append((("{bkg}","SRLMinclEM"), {bkg}Systematics[key]))
        elif "SRMMincl" in name:
            generatorSyst.append((("{bkg}","SRMMinclEM"), {bkg}Systematics[key]))
        elif "SRHMincl" in name:
            generatorSyst.append((("{bkg}","SRHMinclEM"), {bkg}Systematics[key]))
        elif "SRLM" in name:
            generatorSyst.append((("{bkg}","SRLMEM"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","SRLMEl"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","SRLMMu"), {bkg}Systematics[key]))
        elif "SRMM" in name:
            generatorSyst.append((("{bkg}","SRMMEM"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","SRMMEl"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","SRMMMu"), {bkg}Systematics[key]))
        elif "SRHM" in name:
            generatorSyst.append((("{bkg}","SRHMEM"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","SRHMEl"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","SRHMMu"), {bkg}Systematics[key]))
        elif "TRLM" in name:
            generatorSyst.append((("{bkg}","TRLMEM"), {bkg}Systematics[key]))
        elif "TRMM" in name:
            generatorSyst.append((("{bkg}","TRMMEM"), {bkg}Systematics[key]))
        elif "TRHM" in name:
            generatorSyst.append((("{bkg}","TRHMEM"), {bkg}Systematics[key]))
        elif "WR" in name:
            generatorSyst.append((("{bkg}","WREM"), {bkg}Systematics[key]))
        elif "STCR" in name:
            generatorSyst.append((("{bkg}","STCREM"), {bkg}Systematics[key]))
        elif "VRtt1on" in name:
            generatorSyst.append((("{bkg}","VRtt1onEM"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt1onEl"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt1onMu"), {bkg}Systematics[key]))
        elif "VRtt2on" in name:
            generatorSyst.append((("{bkg}","VRtt2onEM"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt2onEl"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt2onMu"), {bkg}Systematics[key]))
        elif "VRtt3on" in name:
            generatorSyst.append((("{bkg}","VRtt3onEM"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt3onEl"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt3onMu"), {bkg}Systematics[key]))
        elif "VRtt1off" in name:
            generatorSyst.append((("{bkg}","VRtt1offEM"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt1offEl"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt1offMu"), {bkg}Systematics[key]))
        elif "VRtt2off" in name:
            generatorSyst.append((("{bkg}","VRtt2offEM"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt2offEl"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt2offMu"), {bkg}Systematics[key]))
        elif "VRtt3off" in name:
            generatorSyst.append((("{bkg}","VRtt3offEM"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt3offEl"), {bkg}Systematics[key]))
            generatorSyst.append((("{bkg}","VRtt3offMu"), {bkg}Systematics[key]))

    '''.format(bkg=background)

elif args.analysis == 'strong1L':

    main = r''''''

    for sys,d in values.items():
        main += '''
    '''
        for region,uncertainties in d.items():
            up_uncertainties = uncertainties["up"]
            down_uncertainties = uncertainties["down"]
            ups = ""
            for up_unc in up_uncertainties:
                if up_unc > 0:
                    up_unc = "+{}".format(abs(up_unc))
                else:
                    up_unc = "-{}".format(abs(up_unc))
                ups += "(1.{}),".format(up_unc)
            downs = ""
            for down_unc in down_uncertainties:
                if down_unc > 0:
                    down_unc = "+{}".format(abs(down_unc))
                else:
                    down_unc = "-{}".format(abs(down_unc))
                downs += "(1.{}),".format(down_unc)
            ups = ups[:-1]
            downs = downs[:-1]

            main += '''{bkg}Systematics['{bkg}{syst}_{region}'] = Systematic("{bkg}{syst}", configMgr.weights, [{ups}], [{downs}], "user","userHistoSys")
'''.format(bkg = background, syst = sys, region = region, ups=ups, downs=downs)


    footer = r'''
def TheorUnc(generatorSyst):
    for key in {bkg}Systematics:
           name=key.split('_')
           name1=name[1]+"_"+name[2]

           if "SR2JBVEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_2J_bin1","SR2JBVEM"), WjetsSystematics[key]))
           if  "SR2JBVEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_2J_bin2","SR2JBVEM"), WjetsSystematics[key]))
           if  "SR2JBVEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_2J_bin3","SR2JBVEM"), WjetsSystematics[key]))
           if  "SR2JBVEM" in name1 and "_bin4" in name1:
              generatorSyst.append((("Wjets_2J_bin4","SR2JBVEM"), WjetsSystematics[key]))

           if "SR2JBTEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_2J_bin1","SR2JBTEM"), WjetsSystematics[key]))
           if "SR2JBTEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_2J_bin2","SR2JBTEM"), WjetsSystematics[key]))
           if "SR2JBTEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_2J_bin3","SR2JBTEM"), WjetsSystematics[key]))
           if "SR2JBTEM" in name1 and "_bin4" in name1:
              generatorSyst.append((("Wjets_2J_bin4","SR2JBTEM"), WjetsSystematics[key]))


           if "VR2JmtEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_2J_bin1","VR2JmtEM"), WjetsSystematics[key]))
           if  "VR2JmtEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_2J_bin2","VR2JmtEM"), WjetsSystematics[key]))
           if  "VR2JmtEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_2J_bin3","VR2JmtEM"), WjetsSystematics[key]))
           if  "VR2JmtEM" in name1 and "_bin4" in name1:
              generatorSyst.append((("Wjets_2J_bin4","VR2JmtEM"), WjetsSystematics[key]))

           if "VR2JmetEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_2J_bin1","VR2JmetEM"), WjetsSystematics[key]))
           if  "VR2JmetEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_2J_bin2","VR2JmetEM"), WjetsSystematics[key]))
           if  "VR2JmetEM" in name1 and "_bin3" in name1:
             generatorSyst.append((("Wjets_2J_bin3","VR2JmetEM"), WjetsSystematics[key]))
           if  "VR2JmetEM" in name1 and "_bin4" in name1:
             generatorSyst.append((("Wjets_2J_bin4","VR2JmetEM"), WjetsSystematics[key]))


           if "SR4JlowxBVEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_4Jlowx_bin1","SR4JlowxBVEM"), WjetsSystematics[key]))
           if  "SR4JlowxBVEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_4Jlowx_bin2","SR4JlowxBVEM"), WjetsSystematics[key]))
           if  "SR4JlowxBVEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_4Jlowx_bin3","SR4JlowxBVEM"), WjetsSystematics[key]))


           if "SR4JlowxBTEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_4Jlowx_bin1","SR4JlowxBTEM"), WjetsSystematics[key]))
           if "SR4JlowxBTEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_4Jlowx_bin2","SR4JlowxBTEM"), WjetsSystematics[key]))
           if "SR4JlowxBTEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_4Jlowx_bin3","SR4JlowxBTEM"), WjetsSystematics[key]))



           if "VR4JlowxhybridEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_4Jlowx_bin1","VR4JlowxhybridEM"), WjetsSystematics[key]))
           if  "VR4JlowxhybridEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_4Jlowx_bin2","VR4JlowxhybridEM"), WjetsSystematics[key]))
           if  "VR4JlowxhybridEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_4Jlowx_bin3","VR4JlowxhybridEM"), WjetsSystematics[key]))

           if "VR4JlowxaplEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_4Jlowx_bin1","VR4JlowxaplEM"), WjetsSystematics[key]))
           if  "VR4JlowxaplEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_4Jlowx_bin2","VR4JlowxaplEM"), WjetsSystematics[key]))
           if  "VR4JlowxaplEM" in name1 and "_bin3" in name1:
             generatorSyst.append((("Wjets_4Jlowx_bin3","VR4JlowxaplEM"), WjetsSystematics[key]))





           if "SR4JhighxBVEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin1","SR4JhighxBVEM"), WjetsSystematics[key]))
           if  "SR4JhighxBVEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin2","SR4JhighxBVEM"), WjetsSystematics[key]))
           if  "SR4JhighxBVEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin3","SR4JhighxBVEM"), WjetsSystematics[key]))


           if "SR4JhighxBTEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin1","SR4JhighxBTEM"), WjetsSystematics[key]))
           if "SR4JhighxBTEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin2","SR4JhighxBTEM"), WjetsSystematics[key]))
           if "SR4JhighxBTEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin3","SR4JhighxBTEM"), WjetsSystematics[key]))



           if "VR4JhighxhybridEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin1","VR4JhighxhybridEM"), WjetsSystematics[key]))
           if  "VR4JhighxhybridEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin2","VR4JhighxhybridEM"), WjetsSystematics[key]))
           if  "VR4JhighxhybridEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin3","VR4JhighxhybridEM"), WjetsSystematics[key]))


           if "VR4JhighxaplEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin1","VR4JhighxaplEM"), WjetsSystematics[key]))
           if  "VR4JhighxaplEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin2","VR4JhighxaplEM"), WjetsSystematics[key]))
           if  "VR4JhighxaplEM" in name1 and "_bin3" in name1:
             generatorSyst.append((("Wjets_4Jhighx_bin3","VR4JhighxaplEM"), WjetsSystematics[key]))



           if "VR4JhighxmtEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin1","VR4JhighxmtEM"), WjetsSystematics[key]))
           if  "VR4JhighxmtEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin2","VR4JhighxmtEM"), WjetsSystematics[key]))
           if  "VR4JhighxmtEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_4Jhighx_bin3","VR4JhighxmtEM"), WjetsSystematics[key]))



           if "SR6JBVEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_6J_bin1","SR6JBVEM"), WjetsSystematics[key]))
           if  "SR6JBVEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_6J_bin2","SR6JBVEM"), WjetsSystematics[key]))
           if  "SR6JBVEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_6J_bin3","SR6JBVEM"), WjetsSystematics[key]))
           if  "SR6JBVEM" in name1 and "_bin4" in name1:
              generatorSyst.append((("Wjets_6J_bin4","SR6JBVEM"), WjetsSystematics[key]))

           if "SR6JBTEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_6J_bin1","SR6JBTEM"), WjetsSystematics[key]))
           if "SR6JBTEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_6J_bin2","SR6JBTEM"), WjetsSystematics[key]))
           if "SR6JBTEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_6J_bin3","SR6JBTEM"), WjetsSystematics[key]))
           if "SR6JBTEM" in name1 and "_bin4" in name1:
              generatorSyst.append((("Wjets_6J_bin4","SR6JBTEM"), WjetsSystematics[key]))


           if "VR6JmtEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_6J_bin1","VR6JmtEM"), WjetsSystematics[key]))
           if  "VR6JmtEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_6J_bin2","VR6JmtEM"), WjetsSystematics[key]))
           if  "VR6JmtEM" in name1 and "_bin3" in name1:
              generatorSyst.append((("Wjets_6J_bin3","VR6JmtEM"), WjetsSystematics[key]))
           if  "VR6JmtEM" in name1 and "_bin4" in name1:
              generatorSyst.append((("Wjets_6J_bin4","VR6JmtEM"), WjetsSystematics[key]))

           if "VR6JaplEM" in name1 and "_bin1" in name1:
              generatorSyst.append((("Wjets_6J_bin1","VR6JaplEM"), WjetsSystematics[key]))
           if  "VR6JaplEM" in name1 and "_bin2" in name1:
              generatorSyst.append((("Wjets_6J_bin2","VR6JaplEM"), WjetsSystematics[key]))
           if  "VR6JaplEM" in name1 and "_bin3" in name1:
             generatorSyst.append((("Wjets_6J_bin3","VR6JaplEM"), WjetsSystematics[key]))
           if  "VR6JaplEM" in name1 and "_bin4" in name1:
             generatorSyst.append((("Wjets_6J_bin4","VR6JaplEM"), WjetsSystematics[key]))

return generatorSyst
'''.format(bkg=background)

content = header + main + footer
if not os.path.exists("hf_configs/"):
    os.makedirs("hf_configs/")
with open("hf_configs/"+"theoryUncertainties_"+args.analysis+"_"+background+".py", 'w') as f:
    f.write(content)
