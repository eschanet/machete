#!/usr/bin/python

"""
Plotting all the CR, VR plots as well as plots at preselection for TR and WR.
"""

import machete as me
from machete import pythonHelpers as ph

import ROOT
import datetime
from MPF.dataMCRatioPlot import DataMCRatioPlot
from MPF.atlasStyle import setAtlasStyle
from MPF.treePlotter import TreePlotter
from MPF import globalStyle as gst
from MPF.legend import Legend as leg
from MPF.process import Process

import normfactors as nf
import os
import argparse
import errno
import json
import sys, getopt
import collections
import builtins

# welp, hardcoding some stuff
def modify_var_dict(d, varname, region):
    yMax = None
    if 'strong' in region:
        if varname is 'meff':
            yMax = 2e8
        if varname is 'aplanarity':
            yMax = 4e7
        if varname is 'njet':
            yMax = 9e8
        if varname is 'nbjet30':
            yMax = 2e9
        if varname is 'mu':
            yMax = 8e7
        if varname is 'actual_mu':
            yMax = 8e7
        if varname is 'combined_mu':
            yMax = 8e7
    elif '1Lbb' in region:
        if varname is 'mbb':
            yMax = 4e8
        if varname is 'mct':
            yMax = 8e7
        if varname is 'njet':
            yMax = 1e9
        if varname is 'nbjet30':
            yMax = 2e10
        if varname is 'mu':
            yMax = 8e7
        if varname is 'actual_mu':
            yMax = 8e7
        if varname is 'combined_mu':
            yMax = 8e7
        if varname is 'mlb1':
            yMax = 2e7
    elif 'weak':
        if varname is 'mjj':
            yMax = 2e9
        if varname is 'mu':
            yMax = 8e8
        if varname is 'actual_mu':
            yMax = 8e7
        if varname is 'combined_mu':
            yMax = 8e7
        if varname is 'nbjet30':
            yMax = 5e9
    return (d,yMax)
def run():
    now = datetime.datetime.now()
    tagDate = now.strftime("%Y_%j")

    parser = argparse.ArgumentParser(description='Make simple ratioplots with data and MC')
    parser.add_argument('-campaign', help='which campaign', default='combined')
    parser.add_argument('--contribution', help='BG contribution', action='store_true')
    parser.add_argument('--significance', help='Significance scan plot', action='store_true')
    parser.add_argument('-input_bkg', help='input MC bkg trees', default='/project/etp5/SUSYInclusive/trees/v2-0/allTrees_v2_0_4_bkg_strong1L_skim_simpleJER.root')
    parser.add_argument('-input_signal', help='input MC signal trees', default='/project/etp5/SUSYInclusive/trees/v2-0/allTrees_v2_0_5_signal_strong1L_skim_simpleJER.root')
    parser.add_argument('-input_data', help='input data trees', default='/project/etp5/SUSYInclusive/trees/v2-0/allTrees_v2_0_data_strong1L_skim.root')
    parser.add_argument('-output_path', help='path to plots', default='v2-0-2')
    parser.add_argument('-tag', help='A tag that serves as a subdirectory in the output directory', default='default')
    parser.add_argument('--srs', help='Plot SRs', action='store_true')
    parser.add_argument('--crs', help='Plot CRs', action='store_true')
    parser.add_argument('--vrs', help='Plot VRs', action='store_true')
    parser.add_argument('-analysis', help='Analysis to consider', default=None)
    parser.add_argument('--signal', help='Add signal points', action='store_true')
    parser.add_argument('-normalize', help='Normalize everything', default=False)
    args = parser.parse_args()

    print(args)
    setAtlasStyle()

    gst.mergeCMEIntoLumiLabel = True
    gst.noLinesForBkg = True
    gst.legendXMin = 0.75

    if args.tag:
        args.output_path+="_"+args.tag

    args.output_path += "_postfit"

    args.output_path = "/project/etp5/eschanet/data-mc/"+args.output_path+"/"
    args.output_path = args.output_path.replace("//","/")


    regions = {}
    if args.analysis == "1Lbb" or args.analysis == "strong1L" or args.analysis == "alt_strong-1L":

        tempDict = {}
        if args.crs: tempDict.update(me.controlregionsDict)
        if args.vrs: tempDict.update(me.validationregionsDict)
        if args.srs: tempDict.update(me.signalregionsDict)

        for region, cuts in tempDict.iteritems():
            if not args.analysis in region:
                continue
            regions[region] = cuts
    else:
        print 'I do not know what analysis to consider, going for all preselections'
        regions = me.preselectionsDict

    print regions.keys()
    for region, cut in regions.iteritems():
        print(region)
        output_path = output_path = args.output_path+"/"+region+"/"

        setLogScale = True
        yTitle = None
        setMoreInfoLabel=region.replace("alt_strong-1L","").replace("_"," ")
        weights="genWeight*leptonWeight*jvtWeight*pileupWeight*bTagWeight"

        if 'SR' in region:
            overflow=True
        else:
            overflow=False

        if args.contribution:
            tp = TreePlotter(plotType="BGContributionPlot",inputLumi=0.001, targetLumi=139.0, addOverflowToLastBin=overflow, normStack=args.normalize)#43.5844
        elif args.significance:
            tp = TreePlotter(plotType="SignificanceScanPlot", inputLumi=0.001, targetLumi=139.0, addOverflowToLastBin=overflow, normStack=False)#43.5844
        else:
            tp = TreePlotter(plotType="DataMCRatioPlot", inputLumi=0.001, targetLumi=139.0, addOverflowToLastBin=overflow, normStack=args.normalize)#43.5844

        trees = ["ttbar", "singletop", "wjets", "zjets", "diboson", "ttv"]#, "tth","vh", "multiboson"]

        for treename in trees:

            if treename in ["wjets", "ttbar", "singletop"]:
                p = Process(me.names[treename], color=me.colors[treename])

                meff_bins = me.alt_meff_binning if args.analysis == "alt_strong-1L" else me.meff_binning
                for tower,bins in meff_bins.iteritems():
                    if tower in region:
                        my_bins = bins
                        tower = tower.replace("SR","").replace("VR","").replace("TR","").replace("WR","")
                        if not (("VR"+tower in region) or ("TR"+tower in region) or ("WR"+tower in region) or ("SR"+tower in region)):
                            continue
                        meff_for_data = bins[0]
                        #dont differentiate between BT and BV
                        i = 0
                        for (low,high) in ph.pairwise(bins):
                            i += 1
                            if high and (not high is bins[-1]) :
                                process_cuts = cut + " && (meffInc30 >= "+str(low)+ " && meffInc30 < "+str(high)+")"
                            elif (high is bins[-1]):
                                process_cuts = cut + " && (meffInc30 >= "+str(low)+")"

                            name = "W" if treename == "wjets" else "Top"
                            name = "mu_"+name+"_"+tower+"_bin"+str(i)
                            nf = me.normFactorsDict[name] if name != "mu_Top_4J_bin3" else me.normFactorsDict["mu_Top_4J_bin2"]

                            # weights
                            weights = "eventWeight*genWeight*leptonWeight*jvtWeight*pileupWeight*bTagWeight" if not treename == "wjets" else "(((fabs(eventWeight)<100.)*eventWeight) + (eventWeight>100.) - (eventWeight<-100.))*genWeight*leptonWeight*jvtWeight*pileupWeight*bTagWeight"

                            p.addTree(args.input_bkg, treename+"_NoSys",cut="(({})*({})*({}))".format(weights,process_cuts,nf))
                            print(p)
                            print(nf)
                            print(process_cuts)

                tp.addProcess(p)

            else:
                weights = "eventWeight*genWeight*leptonWeight*jvtWeight*pileupWeight*bTagWeight"
                tp.addProcessTree(me.names[treename], args.input_bkg, treename+"_NoSys", cut="(({})*({}))".format(weights,cut+" && (meffInc30 >= "+str(meff_for_data)+")"), style="background", color=me.colors[treename])

        if args.signal or args.significance:
            if args.analysis == "strong1L" or args.analysis == "alt_strong-1L":
                signalpoints = [
                    ("2J","GG_oneStep_1100_1060_1020","GG_oneStep_1100_1060_1020"),
                    # ("2J","GG_oneStep_1200_1160_1120","GG_oneStep_1200_1160_1120"),
                    # ("2J","GG_oneStep_1200_1100_1000","GG_oneStep_1200_1100_1000"),
                    # ("2J","SS_oneStep_800_750_700","SS_oneStep_800_750_700"),
                    # ("2J","SS_oneStep_700_675_650","SS_oneStep_700_675_650"),
                    ("2J","SS_oneStep_600_575_550","SS_oneStep_600_575_550"),
                    # ("4Jlowx","GG_oneStep_2000_960_60","GG_oneStep_2000_960_60"),
                    # ("4Jlowx","GG_oneStep_2000_660_60","GG_oneStep_2000_660_60"),
                    ("4Jlowx","GG_oneStep_1800_360_60","GG_oneStep_1800_360_60"),
                    # ("4Jlowx","SS_oneStep_1400_260_60","SS_oneStep_1400_260_60"),
                    ("4Jlowx","SS_oneStep_1300_260_60","SS_oneStep_1300_260_60"),
                    # ("4Jlowx","SS_oneStep_1400_460_60","SS_oneStep_1400_460_60"),
                    # ("4Jhighx","GG_oneStep_2000_1860_60","GG_oneStep_2000_1860_60"),
                    # ("4Jhighx","GG_oneStep_1900_1890_60","GG_oneStep_1900_1890_60"),
                    ("4Jhighx","GG_oneStep_1900_1850_60","GG_oneStep_1900_1850_60"),
                    # ("4Jhighx","SS_oneStep_1400_1350_60","SS_oneStep_1400_1350_60"),
                    # ("4Jhighx","SS_oneStep_1400_1390_60","SS_oneStep_1400_1390_60"),
                    ("4Jhighx","SS_oneStep_1300_1250_60","SS_oneStep_1300_1250_60"),
                    ("6J","GG_oneStep_2000_1012_24","GG_oneStep_2000_1012_24"),
                    # ("6J","GG_oneStep_2200_1200_200","GG_oneStep_2200_1200_200"),
                    # ("6J","GG_oneStep_2000_1500_1000","GG_oneStep_2000_1500_1000"),
                    ("6J","SS_oneStep_1400_712_24","SS_oneStep_1400_712_24"),
                    # ("6J","SS_oneStep_1400_900_400","SS_oneStep_1400_900_400"),
                    # ("6J","SS_oneStep_1000_850_700","SS_oneStep_1000_850_700"),
                ]
                for tower,name,treename in signalpoints:
                    if tower in region:
                        my_name = "#tilde{g}#tilde{g} " if "GG_oneStep" in name else "#tilde{q}#tilde{q} "
                        masses = name.replace("SS_oneStep_","").replace("GG_oneStep_","").split("_")
                        my_name += "({},{},{})".format(masses[0],masses[1],masses[2])
                        tp.addProcessTree(my_name,args.input_signal, treename+"_NoSys", style="signal", cut="(({})*({}))".format(weights,cut+" && (meffInc30 >= "+str(meff_for_data)+")"), lineStyle=1, lineWidth=4)


        data_process = 'data'
        tp.addProcessTree(data_process, args.input_data, "data",cut=cut+" && (meffInc30 >= "+str(meff_for_data)+")", style="data")


        gst.noLinesForBkg = True
        gst.defaultLogyYmin = 0.1

        processLabel = '#bf{Strong 1-lepton}                              #bf{Signal points}: m(#tilde{g})/m(#tilde{q}), m(#tilde{#chi}^{#pm}_{1}),  m(#tilde{#chi}^{0}_{1})'

        tp.setDefaults(legendOptions=builtins.dict(nColumns=3,forceDynamicFontSize=True, noDynamicFontSize=False, scaleLegend=1.0),infoLabel=setMoreInfoLabel, yTitle=yTitle, processLabel=processLabel)

       # if 'strong' in region:
       #    if 'soft' in region:
       #        nf.getAndSetNFs(presel_soft, tp, 'softpresel')
       #    elif 'hard' in region:
       #        nf.getAndSetNFs(presel_hard, tp, 'hardpresel')
       #    elif 'presel' in region:
       #        nf.getAndSetNFs(cut, tp, 'presel')


        for varname, dict in me.varsDict.iteritems():
            yMin=None
            # if not varname == 'lep1Pt':
            #     yMin=0.2
            if not 'strong' in region and ('soft' in varname or 'hard' in varname):
                continue

                # dict['xTitle'] += " (mu)"
            if varname is 'lep1Pt':
                if 'electron' in region:
                    dict['xTitle'] = "Electron p_{T}^{lep}"
                elif 'muon' in region:
                    dict['xTitle'] = "Muon p_{T}^{lep}"
                else:
                    dict['xTitle'] = "p_{T}^{lep}"

            # if 'strong' in region or '1Lbb' in region:
            yMin = None

            if varname is 'meff':
                print(my_bins)
                dict['binLowEdges'] = my_bins

            (dict,yMax) = modify_var_dict(dict,varname,region)

            if "presel" in region:
                tp.registerPlot(output_path+"hists/"+varname+".pdf", yMin=yMin, insideTopMargin = 0.35,logy=setLogScale,**dict)
            else:
                tp.registerPlot(output_path+"hists/"+varname+".pdf",insideTopMargin = 0.40, yMin=yMin,logy=setLogScale,**dict)

        tp.plotAll()


if __name__ == "__main__":
    run()
