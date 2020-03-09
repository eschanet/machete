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

import MPF.vars_mpf as vars

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
    parser.add_argument('--dijets', help='Adding dijets', action='store_true')
    parser.add_argument('-input_bkg', help='input MC bkg trees', default='/project/etp4/eschanet/trees/v2-0/allTrees_v2_0_2_bkg_NoSys.root')
    parser.add_argument('-input_signal', help='input MC signal trees', default='/project/etp5/SUSYInclusive/trees/v2-0/allTrees_v2_0_2_signal_strong1L_skim.root')
    parser.add_argument('-input_data', help='input data trees', default='/project/etp4/eschanet/trees/v2-0/allTrees_v2_0_data.root')
    # parser.add_argument('-input_data', help='input MC trees', default='/project/etp4/eschanet/trees/v2-0/allTrees_v2_0_tight_badjet_data.root')
    parser.add_argument('-output_path', help='path to plots', default='v2-0-2')
    parser.add_argument('-tag', help='A tag that serves as a subdirectory in the output directory', default='default')
    parser.add_argument('-cut', help='Give a cut expression', default=None)
    parser.add_argument('-add_cut', help='Add a cut to all plotted selections', default=None)
    parser.add_argument('--srs', help='Plot SRs', action='store_true')
    parser.add_argument('--crs', help='Plot CRs', action='store_true')
    parser.add_argument('--vrs', help='Plot VRs', action='store_true')
    parser.add_argument('--crackVeto', help='Veto crack', action='store_true')
    parser.add_argument('--normfactors', help='Include norm factors', action='store_true')
    parser.add_argument('--meffbins', help='Plot each meff bin separately', action='store_true')
    parser.add_argument('-regions', help='Give a list of regions to plot', nargs='+', default=None)
    parser.add_argument('-tower', help='Give a tower to plot', default=None)
    parser.add_argument('-analysis', help='Analysis to consider', default=None)
    parser.add_argument('-normalize', help='Normalize everything', default=False)
    args = parser.parse_args()

    print(args)
    setAtlasStyle()

    gst.mergeCMEIntoLumiLabel = True
    gst.noLinesForBkg = True
    gst.legendXMin = 0.85

    if args.contribution:
        args.output_path+="_contribution"
    if args.dijets:
        args.output_path+="_dijets"
    if args.normfactors:
        args.output_path+="_normfac"
    if args.tag:
        args.output_path+="_"+args.tag

    args.output_path += "_{}".format(args.campaign)

    args.output_path = "/project/etp5/eschanet/data-mc/"+args.output_path+"/"
    args.output_path = args.output_path.replace("//","/")


    regions = {}
    if args.analysis == "1Lbb" or args.analysis == "strong1L" or args.analysis == "alt_strong-1L":

        # if not args.regions:
        #     for key, cuts in me.preselectionsDict.iteritems():
        #         if args.analysis in key:
        #             regions[key] = cuts
        tempDict = {}
        if args.crs: tempDict.update(me.controlregionsDict)
        if args.vrs: tempDict.update(me.validationregionsDict)
        if args.regions:
            tempDict = {}
            for region in args.regions:
                myregion = args.analysis+"_"+region
                if args.analysis+"_"+region in me.controlregionsDict.keys():
                    tempDict[myregion] = me.controlregionsDict[myregion]
                elif args.analysis+"_"+region in me.validationregionsDict.keys():
                    tempDict[myregion] = me.validationregionsDict[myregion]
                elif args.analysis+"_"+region in me.signalregionsDict.keys():
                    tempDict[myregion] = me.signalregionsDict[myregion]
        for region, cuts in tempDict.iteritems():
            if args.analysis in region:
                if args.meffbins:
                    meff_bins = me.alt_meff_binning if args.analysis == "alt_strong-1L" else me.meff_binning
                    for tower,bins in meff_bins.iteritems():
                        if (tower in region) and ((tower == args.tower) or (not args.tower)):
                            print('Tower %s in %s' % (tower,region))
                            tower = tower.replace("SR","").replace("VR","").replace("TR","").replace("WR","")
                            if not (("VR"+tower in region) or ("TR"+tower in region) or ("WR"+tower in region)):
                                continue
                            if (not 'BV' in region) and (not 'BT' in region) and (not 'WR' in region) and (not 'TR' in region):
                                print("DISCARDING " +region)
                                continue

                            #dont differentiate between BT and BV
                            i = 1
                            for (low,high) in ph.pairwise(bins):
                                if high and (not high is bins[-1]) :
                                    regions[region+"_bin"+str(i)] = cuts + " && (meffInc30 >= "+str(low)+ " && meffInc30 < "+str(high)+")"
                                elif (high is bins[-1]):
                                    regions[region+"_bin"+str(i)] = cuts + " && (meffInc30 >= "+str(low)+")"
                                elif not high:
                                    print("We are already past the last one??")
                                    sys.exit(status=None)
                                i += 1
                elif (args.tower == tower) or (not args.tower):
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
        setMoreInfoLabel=region.replace("_"," ")
        if args.campaign: setMoreInfoLabel+= " " + args.campaign
        if args.normalize:
            yTitle = 'Normalized to unit area'

        weights="eventWeight*genWeight*leptonWeight*jvtWeight*pileupWeight*bTagWeight"
        if args.campaign == 'mc16d':
            inputlumi = 44.3 #44.3
            cut+="*(RandomRunNumber >= 324320 && RandomRunNumber <= 337833)"
        elif args.campaign == 'mc16a':
            inputlumi = 36.2
            cut+="*(RandomRunNumber >= 276262 && RandomRunNumber <= 320000)"
        elif args.campaign == 'mc16e':
            inputlumi = 58.5
            cut+="*(RandomRunNumber >= 348885)"
        elif args.campaign == 'combined':
            inputlumi = 139
        if args.crackVeto:
            cut+= "&& ( (AnalysisType==1 && (fabs(lep1Eta)<1.37 || fabs(lep1Eta)>1.52)) || (AnalysisType==2) )"
        if args.add_cut:
            cut += "&& ({})".format(args.add_cut)

        if args.contribution:
            tp = TreePlotter(plotType="BGContributionPlot", weight=weights, cut=cut, inputLumi=0.001*(inputlumi/139), targetLumi=inputlumi, addOverflowToLastBin=False, normStack=args.normalize)#43.5844
        elif args.significance:
            tp = TreePlotter(plotType="SignificanceScanPlot", weight=weights, cut=cut, inputLumi=0.001*(inputlumi/139), targetLumi=inputlumi, addOverflowToLastBin=False, normStack=False)#43.5844
        else:
            tp = TreePlotter(plotType="DataMCRatioPlot", weight=weights, cut=cut, inputLumi=0.001*(inputlumi/139), targetLumi=inputlumi, addOverflowToLastBin=False, normStack=args.normalize)#43.5844
        if args.dijets:
            trees = ["ttbar", "singletop", "wjets", "zjets", "diboson", "ttv", "tth","vh", "multiboson", "dijets"]
        else:
            trees = ["ttbar", "singletop", "wjets", "zjets", "diboson", "ttv", "tth","vh", "multiboson"]

        for treename in trees:
            nf=None
            if args.normfactors and args.meffbins and (treename == "wjets" or treename == "ttbar" or treename == "singletop"):
                # get the normalisation factors for wjets and ttbar
                name = "W" if treename == "wjets" else "Top"
                if not "presel" in region:
                    for tower,bins in meff_bins.iteritems():
                        if tower in region:
                            tower = tower.replace("SR","").replace("VR","").replace("TR","").replace("WR","")
                            mytower=tower
                            continue
                    nf = me.normFactorsDict["mu_"+name+"_"+mytower+"_"+region[-4:]]
            if treename == "wjets":
                #fix eventweights, thanks Sherpa ... :-(
                # evtWeight = "((eventWeight>-100.)*(eventWeight<100.))"
                evtWeight = "(1)"
                tp.addProcessTree(me.names[treename], args.input_bkg, treename+"_NoSys",  scale=nf, cut=evtWeight,style="background", color=me.colors[treename])
            else:
                tp.addProcessTree(me.names[treename], args.input_bkg, treename+"_NoSys",  scale=nf, style="background", color=me.colors[treename])

            if args.significance:
                if args.analysis == "strong1L":
                    signalpoints = [
                        ("2J","GG_oneStep_1100_1060_1020","GG_oneStep_1100_1060_1020"),
                        ("2J","GG_oneStep_1200_1160_1120","GG_oneStep_1200_1160_1120"),
                        ("2J","GG_oneStep_1200_1100_1000","GG_oneStep_1200_1100_1000"),
                        ("2J","SS_oneStep_800_750_700","SS_oneStep_800_750_700"),
                        ("2J","SS_oneStep_700_675_650","SS_oneStep_700_675_650"),
                        ("2J","SS_oneStep_600_575_550","SS_oneStep_600_575_550"),
                        ("4Jlowx","GG_oneStep_2000_960_60","GG_oneStep_2000_960_60"),
                        ("4Jlowx","GG_oneStep_2000_660_60","GG_oneStep_2000_660_60"),
                        ("4Jlowx","GG_oneStep_1800_360_60","GG_oneStep_1800_360_60"),
                        ("4Jlowx","SS_oneStep_1400_260_60","SS_oneStep_1400_260_60"),
                        ("4Jlowx","SS_oneStep_1300_260_60","SS_oneStep_1300_260_60"),
                        ("4Jlowx","SS_oneStep_1400_460_60","SS_oneStep_1400_460_60"),
                        ("4Jhighx","GG_oneStep_2000_1860_60","GG_oneStep_2000_1860_60"),
                        ("4Jhighx","GG_oneStep_1900_1890_60","GG_oneStep_1900_1890_60"),
                        ("4Jhighx","GG_oneStep_1900_1850_60","GG_oneStep_1900_1850_60"),
                        ("4Jhighx","SS_oneStep_1400_1350_60","SS_oneStep_1400_1350_60"),
                        ("4Jhighx","SS_oneStep_1400_1390_60","SS_oneStep_1400_1390_60"),
                        ("4Jhighx","SS_oneStep_1300_1250_60","SS_oneStep_1300_1250_60"),
                        ("6J","GG_oneStep_2000_1012_24","GG_oneStep_2000_1012_24"),
                        ("6J","GG_oneStep_2200_1200_200","GG_oneStep_2200_1200_200"),
                        ("6J","GG_oneStep_2000_1500_1000","GG_oneStep_2000_1500_1000"),
                        ("6J","SS_oneStep_1400_712_24","SS_oneStep_1400_712_24"),
                        ("6J","SS_oneStep_1400_900_400","SS_oneStep_1400_900_400"),
                        ("6J","SS_oneStep_1000_850_700","SS_oneStep_1000_850_700"),
                    ]
                    for tower,name,treename in signalpoints:
                        if tower in region:
                            tp.addProcessTree(name,args.input_signal, treename+"_NoSys", style="signal", lineStyle=1, lineWidth=2)


        data_process = 'data'
        if args.campaign == 'mc16a':
            data_process = 'data 15/16'
        elif args.campaign == 'mc16d':
            data_process = 'data 17'
        elif args.campaign == 'mc16e':
            data_process = 'data 18'

        tp.addProcessTree(data_process, args.input_data, "data", style="data")


        gst.noLinesForBkg = True
        gst.defaultLogyYmin = 0.1

        if 'electron' in region:
            processLabel = 'Electrons only'
        elif 'muon' in region:
            processLabel = 'Muons only'
        else:
            processLabel = ''
        tp.setDefaults(legendOptions=builtins.dict(nColumns=3,forceDynamicFontSize=True, noDynamicFontSize=False, scaleLegend=0.8),infoLabel=setMoreInfoLabel, yTitle=yTitle, processLabel=processLabel)

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
            yMin = 1e-1

            (dict,yMax) = modify_var_dict(dict,varname,region)

            if "presel" in region:
                tp.registerPlot(output_path+"hists/"+varname+".pdf", yMin=yMin, insideTopMargin = 0.35,logy=setLogScale,**dict)
            else:
                tp.registerPlot(output_path+"hists/"+varname+".pdf",insideTopMargin = 0.40,logy=setLogScale,**dict)

        tp.plotAll()


if __name__ == "__main__":
    run()
