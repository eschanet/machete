#!/usr/bin/env python
import ROOT

import os
import errno
import json
from array import array

import argparse

import logging
from commonHelpers.logger import logger
logger = logger.getChild("mephisto")

parser = argparse.ArgumentParser(
    description='This script helps in creating a proper normalization for trees that have been processed through e.g. SimpleAnalysis and lack the "traditional" genWeight branch.',
    epilog="You beautiful person, you."
)
parser.add_argument('inputfile', help='The ROOT file')
parser.add_argument('inputtree', help='The ROOT tree')
parser.add_argument('--dsid', help='The DSID',default=None)
parser.add_argument('--normBranch', help='Branch used for normalisation',default="genWeight")
parser.add_argument('--xsec-file', help='Path to the xsec file',nargs='?', const='/cvmfs/atlas.cern.ch/repo/sw/database/GroupData/dev/PMGTools/PMGxsecDB_mc16.txt', default=None)
parser.add_argument('--xsec', '-x', help='Actual xsection (in case no xsec file) in pb',default=None)
parser.add_argument('--fb', help='Normalise to 1/fb instead of 1/pb',action='store_true')
parser.add_argument('--applyGenWeight', help='Apply generator weight to the normalisation branch',action='store_true')
args = parser.parse_args()

if not os.path.isfile(args.inputfile):
    logger.error("Provided ROOT file does not exist or is not a file!")
    raise ValueError("Sorry, need to exit here.")

if args.xsec_file:
    if not os.path.isfile(args.xsec_file):
        logger.error("Provided xsec file does not exist or is not a file!")
        raise ValueError("Sorry, need to exit here.")
    else:
        if not args.dsid:
            logger.warning("Provided a xsec file, but not a DSID, will try to guess ...")
        else:
            logger.info("Provided xsec file and DSID, thanks mate!")

def get_xsec(xsec_file,my_dsid=None):
    with open(xsec_file) as f:
        f.readline()
        for l in f:
            # DSID is the first field
            if int(my_dsid) == int(l.rstrip().split()[0]):
                xsec = float(l.rstrip().split()[2])
                filter_eff = float(l.rstrip().split()[3])
                kfactor = float(l.rstrip().split()[4])

                logger.info("Got xsec: {}".format(xsec))
                return xsec*filter_eff*kfactor
        else:
            logger.error("Didn't find a xsec ... sorry!")
            return None

if not args.xsec:
    xsec = get_xsec(args.xsec_file,args.dsid)
    if not xsec: raise ValueError("Exiting here.")
else:
    xsec = args.xsec

if args.fb:
    xsec *= 1000

#
# Let's do it
#
tf = ROOT.TFile(args.inputfile)
tree = tf.Get(args.inputtree)
nentries = tree.GetEntries()

sumofweights=0
for event in tree:
    sumofweights+=event.eventWeight

if int(sumofweights) != int(nentries):
    logger.warning("SumW : {}, nEvents : {}".format(sumofweights,nentries))

tree.SetBranchStatus(args.normBranch,0)
if args.applyGenWeight:
    tree.SetBranchStatus("eventWeight",0)
ntf = ROOT.TFile(args.inputfile.replace('.root','_updateNorm.root'),'recreate')
ntree = tree.CloneTree(0)

eventWeight=array('f',[0])
tree.SetBranchStatus("eventWeight",1)
tree.SetBranchAddress("eventWeight", eventWeight)

# name = f.replace('.root','_NoSys')
# ntree.SetName(name)

# x = ROOT.Double(xsec/sumofweights)
normWeight = array('d', [0])

ntree.Branch(args.normBranch,normWeight,'{}/D'.format(args.normBranch))

for i in range(nentries):
    if i % 100000 == 0 :
        logger.info("Processed {} events".format(i))
    tree.GetEntry(i)
    normWeight[0] = ROOT.Double(eventWeight[0]*xsec/sumofweights) if args.applyGenWeight else ROOT.Double(xsec/sumofweights)
    ntree.Fill()

#ntree.AutoSave()
ntf.Write()
tf.Close()
