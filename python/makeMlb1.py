#!/usr/bin/env python
import ROOT
from MPF.dataMCRatioPlot import DataMCRatioPlot
from MPF.atlasStyle import setAtlasStyle
from MPF.treePlotter import TreePlotter
from MPF import globalStyle as gst
from MPF.n1plotter import N1Plotter
from MPF import pyrootHelpers as PH

import os
import errno
import json
from array import array

import argparse

import logging
from commonHelpers.logger import logger
logger = logger.getChild("mephisto")

parser = argparse.ArgumentParser(
    description='This script creates mlb1 in a set of trees',
    epilog="You beautiful person, you."
)
parser.add_argument('inputfile', help='The input file')
args = parser.parse_args()


with open(args.xsecsfile, 'r') as document:
    dict = {}
    for line in document:
        line = line.split()
        if not line:  # empty line?
            continue
        dict[line[0]] = float(line[1])

        print('{} : {}'.format(int(line[0]),float(line[1])))

for indx,f in enumerate(os.listdir(args.inputdir)):
    if f.endswith(".root"):

        def getxsec(filename):
            if "oneStep" in filename:
                mass_string = filename.replace('GG_oneStep_','').replace('.root','').split('_')[0]
            elif "Wh_hbb" in filename:
                mass_string = filename.replace('C1N2_Wh_hbb_','').replace('.root','').split('_')[0]
            else:
                logger.error("Cannot figure out signal model.")
                raise ValueError("Sorry, need to exit here.")

            mass_string = mass_string.replace("p0","").replace("p5",".5")

            if not dict.has_key(mass_string):
                lowerMass = int(float(mass_string)) // 5 * 5
                upperMass = lowerMass + 5

                xsec = (dict[str(lowerMass)] + dict[str(upperMass)]) / 2.0
                return xsec
            else:
                return dict[mass_string]

        xsec = getxsec(f)
        logger.info("Found xsec: " + str(xsec))
        logger.info("Updating "+f)
        tf = ROOT.TFile(args.inputdir+"/"+f)
        # tree = tf.Get('OneLepton2016__ntuple')
        tree = tf.Get('EwkOneLeptonTwoBjets2018_simplifiedfit__ntuple')
        nentries = tree.GetEntries()
        sumofweights=0
        for event in tree:
            sumofweights+=event.eventWeight

        nBJet30_MV2c10=array('i',[0])
        if int(sumofweights) != int(nentries):
            logger.warning("SumW is not equal to nEntries. Did not expect that!")
        tree.SetBranchStatus("genWeight",0)
        # tree.SetBranchAddress("nBJet20_MV2c10", nBJet30_MV2c10)

        ntf = ROOT.TFile(args.inputdir+"/"+f.replace('.root','_update.root'),'recreate')
        ntree = tree.CloneTree(0)
        name = f.replace('.root','_NoSys')
        ntree.SetName(name)
        x = ROOT.Double(0.19*xsec/sumofweights) #TODO: fix FILTEREFF
        genWeight = array('d', [x])

        ntree.Branch('genWeight',genWeight,'genWeight/D')
        # ntree.Branch('nBJet30_MV2c10',nBJet30_MV2c10,'nBJet30_MV2c10/I')
        for i in range(nentries):
            tree.GetEntry(i)
            ntree.Fill()

        #ntree.AutoSave()
        ntf.Write()
        tf.Close()
