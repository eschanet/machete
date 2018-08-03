#!/usr/bin/python

import ROOT
from MPF.atlasStyle import setAtlasStyle
from MPF import globalStyle as gst
import collections

gst.drawATLASLabel = False
gst.mergeCMEIntoLumiLabel = True
# gst.CMELabelY = 0.9
# gst.CMELabelX = gst.CMELabelX + 0.02
gst.lumiLabelY = 0.88
gst.infoLabelY = 0.84
gst.lumiLabelX = 0.2
gst.infoLabelX = 0.2
gst.noLinesForBkg = True
gst.legendXMin = 0.76
gst.cutLineArrows = True
#gst.cutLineColor = 8
gst.cutLineStyle = 1
gst.cutLineWidth = 3

tstyle_signalnames = {}
tstyle_signalnames["C1C1_WW_200p0_80p0"] = "(200,80)"
tstyle_signalnames["C1C1_WW_250p0_60p0"] = "(250,60)"
tstyle_signalnames["C1C1_WW_300p0_0p0"] = "(300,0)"
tstyle_signalnames["C1C1_WW_400p0_0p0"] = "(400,0)"
tstyle_signalnames["C1C1_WW_500p0_0p0"] = "(500,0)"
tstyle_signalnames["C1N2_WZ_200p0_50p0"] = "(200,50)"
tstyle_signalnames["C1N2_WZ_240p0_110p0"] = "(240,110)"
tstyle_signalnames["C1N2_WZ_250p0_50p0"] = "(250,50)"
tstyle_signalnames["C1N2_WZ_300p0_50p0"] = "(300,50)"
tstyle_signalnames["C1N2_WZ_500p0_0p0"] = "(500,0)"

tstyle_processnames = collections.OrderedDict()
tstyle_processnames["ttbar"] = "t#bar{t}"
tstyle_processnames["singletop"] = "Single top"
tstyle_processnames["wjets"] = "W+jets"
tstyle_processnames["wjets_Sherpa221"] = "W+jets"
tstyle_processnames["zjets"] = "Z+jets"
tstyle_processnames["zjets_Sherpa221"] = "Z+jets"
tstyle_processnames["diboson"] = "Diboson"
tstyle_processnames["diboson_Sherpa221"] = "Diboson"
tstyle_processnames["ttv"] = "t#bar{t}+V"
tstyle_processnames["dijets"] = "Dijets"
tstyle_processnames["multiboson"] = "Multiboson"
tstyle_processnames["ttX"] = "t#bar{t}+X"

tstyle_colors = {}
tstyle_colors["ttbar"] = ROOT.TColor.GetColor("#9AFF99")
tstyle_colors["singletop"] = ROOT.TColor.GetColor("#019900")
tstyle_colors["wjets"] = ROOT.TColor.GetColor("#3399FF")
tstyle_colors["zjets"] = ROOT.TColor.GetColor("#FFCC00")
tstyle_colors["wjets_Sherpa221"] = ROOT.TColor.GetColor("#3399FF")
tstyle_colors["zjets_Sherpa221"] = ROOT.TColor.GetColor("#FFCC00")
tstyle_colors["diboson"] = ROOT.TColor.GetColor("#9965CC")
tstyle_colors["diboson_Sherpa221"] = ROOT.TColor.GetColor("#9965CC")
tstyle_colors["ttv"] = ROOT.TColor.GetColor("#99CCCC")
tstyle_colors["dijets"] = ROOT.TColor.GetColor("#CCCCCC")
tstyle_colors["dijets_fixed"] = ROOT.TColor.GetColor("#CCCCCC")
tstyle_colors["multiboson"] = ROOT.TColor.GetColor("#dc322f")
tstyle_colors["C1C1_WW_200p0_80p0"] = ROOT.TColor.GetColor("#9965CC")
tstyle_colors["C1C1_WW_250p0_60p0"] = ROOT.TColor.GetColor("#1ddf47")
tstyle_colors["C1C1_WW_300p0_0p0"] = ROOT.TColor.GetColor("#182fee")
tstyle_colors["C1C1_WW_400p0_0p0"] = ROOT.TColor.GetColor("#ed0909")
tstyle_colors["C1C1_WW_500p0_0p0"] = ROOT.TColor.GetColor("#ff9900")
tstyle_colors["C1N2_WZ_200p0_50p0"] = ROOT.TColor.GetColor("#b747bd")
tstyle_colors["C1N2_WZ_240p0_110p0"] = ROOT.TColor.GetColor("#8316b6")
tstyle_colors["C1N2_WZ_250p0_50p0"] = ROOT.TColor.GetColor("#19d6e2")
tstyle_colors["C1N2_WZ_300p0_50p0"] = ROOT.TColor.GetColor("#97c31a")
tstyle_colors["C1N2_WZ_500p0_0p0"] = ROOT.TColor.GetColor("#1f6e6b")


tstyle_varsDict = {}
tstyle_varsDict['met'] = vars.met
tstyle_varsDict['hardmet'] = vars.hardmet
tstyle_varsDict['lep1Pt'] = vars.lep1Pt
tstyle_varsDict['lep1Pt_soft'] = vars.lep1Pt_soft
tstyle_varsDict['lep1Eta'] = vars.lep1Eta
tstyle_varsDict['jet1Eta'] = vars.jet1Eta
tstyle_varsDict['meff'] = vars.meff
tstyle_varsDict['met_over_meff'] = vars.met_over_meff
tstyle_varsDict['ht'] = vars.ht
tstyle_varsDict['jet1Pt'] = vars.jet1Pt
tstyle_varsDict['jet2Pt'] = vars.jet2Pt
tstyle_varsDict['jet3Pt'] = vars.jet3Pt
tstyle_varsDict['jet4Pt'] = vars.jet4Pt
tstyle_varsDict['mt'] = vars.mt
tstyle_varsDict['mt_soft'] = vars.mt_soft
tstyle_varsDict['njet'] = vars.njet
# varsDict['nbjet25'] = vars.nbjet25
tstyle_varsDict['njet4'] = vars.njet4
tstyle_varsDict['aplanarity'] = vars.aplanarity
tstyle_varsDict['mu'] = vars.mu
tstyle_varsDict['nVtx'] = vars.nVtx
tstyle_varsDict['ptmetlep'] = vars.ptmetlep
# varsDict['mct'] = vars.mct
# varsDict['mbb'] = vars.mbb
tstyle_varsDict['meff_all'] = vars.meff_all
tstyle_varsDict['met_Sig'] = vars.metsig

tstyle_binnings = collections.OrderedDict()
tstyle_binnings["strong_SR_2J_btag"]= [700,1100,1500,1900,2300]
tstyle_binnings["strong_SR_2J_bveto"]= [700,1100,1500,1900,2300]
tstyle_binnings["strong_SR_4Jhighx_btag"]= [1000,1500,2000,2500]
tstyle_binnings["strong_SR_4Jhighx_bveto"]= [1000,1500,2000,2500]
tstyle_binnings["strong_SR_4Jlowx_btag"]= [1300,1650,2000,2350.]
tstyle_binnings["strong_SR_4Jlowx_bveto"]= [1300,1650,2000,2350.]
tstyle_binnings["strong_SR_6J_btag"]= [700,1233.3,1766.6,2300,2833.]
tstyle_binnings["strong_SR_6J_bveto"]= [700,1233.3,1766.6,2300,2833.]
tstyle_binnings["strong_SR_9J"]= [1000,1500,2000]

btag = "&&nBJet30_MV2c10>0"
bveto = "&&nBJet30_MV2c10==0"

tstyle_presel_hard = "nJet30>=4&&lep1Pt>=35&&met>250&&trigMatch_metTrig&&nLep_base==1&&nLep_signal==1"
tstyle_presel_soft = "nJet30>=2&&lep1Pt<35&&met>250&&trigMatch_metTrig&&nLep_base==1&&nLep_signal==1"
tstyle_electron = "&&AnalysisType==1"
tstyle_muon = "&&AnalysisType==2"

# preselectionsDict = collections.OrderedDict()
# # preselectionsDict['1Lbb_presel'] = "nJet30>=2 && nJet30<=3 && lep1Pt>=27 && nBJet30_MV2c10>1 && met>100 && mt>40 && mbb>50 && nLep_base==1&&nLep_signal==1"
# preselectionsDict['strong_presel'] = "nJet30>=2&&met>250&&nLep_base==1&&nLep_signal==1"
# # preselectionsDict['weak_presel'] = "nJet30>=2 && nJet30<=3 && met>150 && nLep_base==1&&nLep_signal==1 && nBJet30_MV2c10==0"
# # preselectionsDict['1Lbb_presel_electron'] = "nJet30>=2 && nJet30<=3 && lep1Pt>=27 && nBJet30_MV2c10>1 && met>100 && mt>40 && mbb>50 && nLep_base==1&&nLep_signal==1&&AnalysisType==1"
# # preselectionsDict['1Lbb_presel_muon'] = "nJet30>=2 && nJet30<=3 && lep1Pt>=27 && nBJet30_MV2c10>1 && met>100 && mt>40 && mbb>50 && nLep_base==1&&nLep_signal==1&&AnalysisType==2"
# preselectionsDict['strong_presel_electron'] = "nJet30>=2&&met>250&&nLep_base==1&&nLep_signal==1&&AnalysisType==1"
# preselectionsDict['strong_presel_muon'] = "nJet30>=2&&met>250&&nLep_base==1&&nLep_signal==1&&AnalysisType==2"
# # preselectionsDict['weak_presel_electron'] = "nJet30>=2 && nJet30<=3 && met>150 && nLep_base==1&&nLep_signal==1 && nBJet30_MV2c10==0&&AnalysisType==1"
# # preselectionsDict['weak_presel_muon'] = "nJet30>=2 && nJet30<=3 && met>150 && nLep_base==1&&nLep_signal==1 && nBJet30_MV2c10==0&&AnalysisType==2"
#
# # preselectionsDict['strong_hard_btag_all'] = presel_hard+btag
# # preselectionsDict['strong_hard_bveto_all'] = presel_hard+bveto
# # preselectionsDict['strong_hard_btag_muon'] = presel_hard+btag+muon
# # preselectionsDict['strong_hard_bveto_muon'] = presel_hard+bveto+muon
# # preselectionsDict['strong_hard_btag_electron'] = presel_hard+btag+electron
# # preselectionsDict['strong_hard_bveto_electron'] = presel_hard+bveto+electron
# #
# # preselectionsDict['strong_soft_btag_all'] = presel_soft+btag
# # preselectionsDict['strong_soft_bveto_all'] = presel_soft+bveto
# # preselectionsDict['strong_soft_btag_muon'] = presel_soft+btag+muon
# # preselectionsDict['strong_soft_bveto_muon'] = presel_soft+bveto+muon
# # preselectionsDict['strong_soft_btag_electron'] = presel_soft+btag+electron
# # preselectionsDict['strong_soft_bveto_electron'] = presel_soft+bveto+electron
#
#
# signalregionsDict = collections.OrderedDict()
# signalregionsDict["strong_SR_2J_btag"] = "lep1Pt<35 && nJet30>=2 && met>430. && mt>100. && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# signalregionsDict["strong_SR_2J_bveto"] = signalregionsDict["strong_SR_2J_btag"]
# signalregionsDict["strong_SR_2J_btag"] += btag
# signalregionsDict["strong_SR_2J_bveto"] += bveto
# signalregionsDict["strong_SR_4Jhighx_btag"] = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>450 && LepAplanarity>0.01 && met/meffInc30>0.25&&  nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# signalregionsDict["strong_SR_4Jhighx_bveto"] = signalregionsDict["strong_SR_4Jhighx_btag"]
# signalregionsDict["strong_SR_4Jhighx_bveto"] += bveto
# signalregionsDict["strong_SR_4Jhighx_btag"] += btag
# signalregionsDict["strong_SR_4Jlowx_btag"] = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>250 && mt>150 && mt<450 && LepAplanarity>0.05&&  nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# signalregionsDict["strong_SR_4Jlowx_bveto"] = signalregionsDict["strong_SR_4Jlowx_btag"]
# signalregionsDict["strong_SR_4Jlowx_bveto"] += bveto
# signalregionsDict["strong_SR_4Jlowx_btag"] += btag
# signalregionsDict["strong_SR_6J_btag"] = "lep1Pt>35 && nJet30>=6 && met>350. && mt>175.&& LepAplanarity>0.06&&  nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# # orthogonalise with 9J SR
# #signalregionsDict["SR_6J_btag"] += "&&nJet30<=8"
# signalregionsDict["strong_SR_6J_bveto"] = signalregionsDict["strong_SR_6J_btag"]
# signalregionsDict["strong_SR_6J_bveto"] += bveto
# signalregionsDict["strong_SR_6J_btag"] += btag
# signalregionsDict["strong_SR_9J"] = "mt>175&&LepAplanarity>0.07&&nJet30>=9&&nLep_signal==1&&nLep_base==1&&lep1Pt>35&&(met/sqrt(Ht30))>8&&meffInc30>1000&&met>200"
# # signalregionsDict["strong_SR_9J_lowmet"] = signalregionsDict["strong_SR_9J"] + "&&met<350"
#
# controlregionsDict = collections.OrderedDict()
# controlregionsDict['strong_CR_2J_bveto'] = "lep1Pt<35 && nJet30>=2 && met>300 && met<430. && mt>40 && mt<100. && (met/meffInc30) > 0.15 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# controlregionsDict['strong_CR_2J_btag'] = controlregionsDict['strong_CR_2J_bveto']
# controlregionsDict['strong_CR_2J_bveto'] += bveto
# controlregionsDict['strong_CR_2J_btag'] += btag
# controlregionsDict['strong_CR_4Jhighx_bveto'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>300 && mt>50 && mt<200. && LepAplanarity < 0.01 && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# controlregionsDict['strong_CR_4Jhighx_btag'] = controlregionsDict['strong_CR_4Jhighx_bveto']
# controlregionsDict['strong_CR_4Jhighx_bveto'] += bveto
# controlregionsDict['strong_CR_4Jhighx_btag'] += btag
# controlregionsDict['strong_CR_4Jlowx_bveto'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>50 && mt<150. && LepAplanarity > 0.01 && LepAplanarity < 0.05 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# controlregionsDict['strong_CR_4Jlowx_btag'] = controlregionsDict['strong_CR_4Jlowx_bveto']
# controlregionsDict['strong_CR_4Jlowx_bveto'] += bveto
# controlregionsDict['strong_CR_4Jlowx_btag'] += btag
# controlregionsDict['strong_CR_6J_bveto'] = "lep1Pt>35 && nJet30>=6 && met>350 && mt>50 && mt<175. && LepAplanarity < 0.06 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# controlregionsDict['strong_CR_6J_btag'] = controlregionsDict['strong_CR_6J_bveto']
# controlregionsDict['strong_CR_6J_bveto'] += bveto
# controlregionsDict['strong_CR_6J_btag'] += btag
#
# preselection = "&&nLep_signal==1&&nLep_base==1&&lep1Pt>35&&(met/sqrt(Ht30))>8&&meffInc30>1000&&met>200"
# controlregionsDict["strong_CR_9J_B_btag"] = "mt<100&&nJet30>=5&&nJet30<=6" + preselection
# controlregionsDict["strong_CR_9J_B_bveto"] = controlregionsDict["strong_CR_9J_B_btag"]
# controlregionsDict['strong_CR_9J_B_bveto'] += bveto
# controlregionsDict["strong_CR_9J_B_btag"] += btag
#
# controlregionsDict["strong_CR_9J_A_btag"] = "mt>175&&nJet30>=5&&nJet30<=6" + preselection
# controlregionsDict["strong_CR_9J_A_bveto"] = controlregionsDict["strong_CR_9J_A_btag"]
# controlregionsDict['strong_CR_9J_A_bveto'] += bveto
# controlregionsDict["strong_CR_9J_A_btag"] += btag
#
# controlregionsDict["strong_CR_9J_C_btag"] = "mt<100&&LepAplanarity>0.07&&nJet30>=9" + preselection
# controlregionsDict["strong_CR_9J_C_bveto"] = controlregionsDict["strong_CR_9J_C_btag"]
# controlregionsDict['strong_CR_9J_C_bveto'] += bveto
# controlregionsDict["strong_CR_9J_C_btag"] += btag
#
# controlregionsDict["strong_CR_9J_Cprime_btag"] = "mt<100&&LepAplanarity<0.05&&nJet30>=7&&nJet30<=8" + preselection
# controlregionsDict["strong_CR_9J_Cprime_bveto"] = controlregionsDict["strong_CR_9J_Cprime_btag"]
# controlregionsDict['strong_CR_9J_Cprime_bveto'] += bveto
# controlregionsDict["strong_CR_9J_Cprime_btag"] += btag
#
# controlregionsDict["strong_CR_9J_Aprime_btag"] = "mt>100&&mt<175&&nJet30>=5&&nJet30<=6" + preselection
# controlregionsDict["strong_CR_9J_Aprime_bveto"] = controlregionsDict["strong_CR_9J_Aprime_btag"]
# controlregionsDict['strong_CR_9J_Aprime_bveto'] += bveto
# controlregionsDict["strong_CR_9J_Aprime_btag"] += btag
#
# # controlregionsDict['1Lbb_CR_ttbar_incl'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && (mbb<105 || mbb>135) && mt>100 && met>190"
# # controlregionsDict['1Lbb_CR_ttbar_low'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && (mbb<105 || mbb>135) && mt>100 && mt<140 && met>190"
# # controlregionsDict['1Lbb_CR_ttbar_medium'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && (mbb<105 || mbb>135) && mt>140 && mt<200 && met>200"
# # controlregionsDict['1Lbb_CR_ttbar_high'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && (mbb<105 || mbb>135) && mt>200 && met>210"
# # controlregionsDict['1Lbb_CR_wjets'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && mbb<80 && mt>40 && mt<100 && met>190"
# # controlregionsDict['1Lbb_CR_singletop'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && mbb>195 && mt>100 && met>190"
#
# validationregionsDict = collections.OrderedDict()
# validationregionsDict['strong_VR_2J_met'] = "lep1Pt<35 && nJet30>=2 && met>430. && mt>40 && mt<100. && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# validationregionsDict['strong_VR_2J_mt'] = "lep1Pt<35 && nJet30>=2 && met>300 && met<430. && mt>100. && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# validationregionsDict['strong_VR_4Jhighx_aplanarity'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>50 && mt<150. && LepAplanarity > 0.05 && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# validationregionsDict['strong_VR_4Jhighx_mt'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>200 && LepAplanarity < 0.01 && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# validationregionsDict['strong_VR_4Jhighx_hybrid'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>150 && mt<450. && LepAplanarity > 0.01 && LepAplanarity < 0.05 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# validationregionsDict['strong_VR_4Jlowx_aplanarity'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>50 && mt<150. && LepAplanarity > 0.05 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# validationregionsDict['strong_VR_4Jlowx_hybrid'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>150 && mt<450. && LepAplanarity > 0.01 && LepAplanarity < 0.05 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# validationregionsDict['strong_VR_6J_aplanarity'] = "lep1Pt>35 && nJet30>=6 && met>350 && mt>50 && mt<175. && LepAplanarity > 0.06 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# validationregionsDict['strong_VR_6J_mt'] = "lep1Pt>35 && nJet30>=6 && met>250 && mt>175 && mt<400. && LepAplanarity < 0.06 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
#
# validationregionsDict["strong_VR_9J_mt"] = "mt>175&&LepAplanarity<0.05&&nJet30>=7&&nJet30<=8" + preselection
# validationregionsDict["strong_VR_9J_njet"] = "mt>100&&mt<175&&LepAplanarity<0.05&&nJet30>=9" + preselection
#
# # validationregionsDict['1Lbb_VR_ttbar_incl'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && mbb>105 && mbb<135 && mt>100 && met>190"
# # validationregionsDict['1Lbb_VR_ttbar_low'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && mbb>105 && mbb<135 && mt>100 && mt<140 && met>190"
# # validationregionsDict['1Lbb_VR_ttbar_medium'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && mbb>105 && mbb<135 && mt>140 && mt<200 && met>200"
# # validationregionsDict['1Lbb_VR_ttbar_high'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && mbb>105 && mbb<135 && mt>200 && met>210"
# #
# # validationregionsDict['1Lbb_VR_bbsideband_incl'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && (mbb<105 || (mbb>135&&mbb<195)) && mt>100 && met>190"
# # validationregionsDict['1Lbb_VR_bbsideband_low'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && (mbb<105 || (mbb>135&&mbb<195)) && mt>100 && mt<140 && met>190"
# # validationregionsDict['1Lbb_VR_bbsideband_medium'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && (mbb<105 || (mbb>135&&mbb<195)) && mt>140 && mt<200 && met>200"
# # validationregionsDict['1Lbb_VR_bbsideband_high'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && (mbb<105 || (mbb>135&&mbb<195)) && mt>200 && met>210"
