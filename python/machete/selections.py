import collections

btag = "&&nBJet30_MV2c10>0"
bveto = "&&nBJet30_MV2c10==0"

binnings = collections.OrderedDict()
binnings["strong_SR_2J_btag"]= [700,1100,1500,1900,2300]
binnings["strong_SR_2J_bveto"]= [700,1100,1500,1900,2300]
binnings["strong_SR_4Jhighx_btag"]= [1000,1500,2000,2500]
binnings["strong_SR_4Jhighx_bveto"]= [1000,1500,2000,2500]
binnings["strong_SR_4Jlowx_btag"]= [1300,1650,2000,2350.]
binnings["strong_SR_4Jlowx_bveto"]= [1300,1650,2000,2350.]
binnings["strong_SR_6J_btag"]= [700,1233.3,1766.6,2300,2833.]
binnings["strong_SR_6J_bveto"]= [700,1233.3,1766.6,2300,2833.]
binnings["strong_SR_9J"]= [1000,1500,2000]

presel_hard = "nJet30>=4&&lep1Pt>=35&&met>250&&trigMatch_metTrig&&nLep_base==1&&nLep_signal==1"
presel_soft = "nJet30>=2&&lep1Pt<35&&met>250&&trigMatch_metTrig&&nLep_base==1&&nLep_signal==1"
electron = "&&AnalysisType==1"
muon = "&&AnalysisType==2"

preselectionsDict = collections.OrderedDict()
preselectionsDict['1Lbb_presel'] = "(trigWeight_singleLepTrig)*(trigMatch_singleLepTrig&&nJet30>=2 && nJet30<=3 && lep1Pt>=27 && nBJet30_MV2c10>1 && met>100 && mt>40 && mbb>50 && nLep_base==1&&nLep_signal==1)"
preselectionsDict['strong_presel'] = "trigMatch_metTrig&&nJet30>=2&&met>250&&nLep_base==1&&nLep_signal==1"
preselectionsDict['weak_presel'] = "(trigWeight_singleLepTrig)*(trigMatch_singleLepTrig&&nJet30>=2 && nJet30<=3 && met>150 && nLep_base==1&&nLep_signal==1)"
preselectionsDict['1Lbb_presel_electron'] = "(trigWeight_singleLepTrig)*(trigMatch_singleLepTrig&&nJet30>=2 && nJet30<=3 && lep1Pt>=27 && nBJet30_MV2c10>1 && met>100 && mt>40 && mbb>50 && nLep_base==1&&nLep_signal==1&&AnalysisType==1)"
preselectionsDict['1Lbb_presel_muon'] = "(trigWeight_singleLepTrig)*(trigMatch_singleLepTrig&&nJet30>=2 && nJet30<=3 && lep1Pt>=27 && nBJet30_MV2c10>1 && met>100 && mt>40 && mbb>50 && nLep_base==1&&nLep_signal==1&&AnalysisType==2)"
preselectionsDict['strong_presel_electron'] = "trigMatch_metTrig&&nJet30>=2&&met>250&&nLep_base==1&&nLep_signal==1&&AnalysisType==1"
preselectionsDict['strong_presel_muon'] = "trigMatch_metTrig&&nJet30>=2&&met>250&&nLep_base==1&&nLep_signal==1&&AnalysisType==2"
preselectionsDict['weak_presel_electron'] = "(trigWeight_singleLepTrig)*(trigMatch_singleLepTrig&&nJet30>=2 && nJet30<=3 && met>150 && nLep_base==1&&nLep_signal==1 && AnalysisType==1)"
preselectionsDict['weak_presel_muon'] = "(trigWeight_singleLepTrig)*(trigMatch_singleLepTrig&&nJet30>=2 && nJet30<=3 && met>150 && nLep_base==1&&nLep_signal==1 && AnalysisType==2)"

preselectionsDict['strong_hard_btag_all'] = presel_hard+btag
preselectionsDict['strong_hard_bveto_all'] = presel_hard+bveto
preselectionsDict['strong_hard_btag_muon'] = presel_hard+btag+muon
preselectionsDict['strong_hard_bveto_muon'] = presel_hard+bveto+muon
preselectionsDict['strong_hard_btag_electron'] = presel_hard+btag+electron
preselectionsDict['strong_hard_bveto_electron'] = presel_hard+bveto+electron

preselectionsDict['strong_soft_btag_all'] = presel_soft+btag
preselectionsDict['strong_soft_bveto_all'] = presel_soft+bveto
preselectionsDict['strong_soft_btag_muon'] = presel_soft+btag+muon
preselectionsDict['strong_soft_bveto_muon'] = presel_soft+bveto+muon
preselectionsDict['strong_soft_btag_electron'] = presel_soft+btag+electron
preselectionsDict['strong_soft_bveto_electron'] = presel_soft+bveto+electron


signalregionsDict = collections.OrderedDict()
signalregionsDict["strong_SR_2J_btag"] = "lep1Pt<35 && nJet30>=2 && met>430. && mt>100. && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
signalregionsDict["strong_SR_2J_bveto"] = signalregionsDict["strong_SR_2J_btag"]
signalregionsDict["strong_SR_2J_btag"] += btag
signalregionsDict["strong_SR_2J_bveto"] += bveto
signalregionsDict["strong_SR_4Jhighx_btag"] = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>450 && LepAplanarity>0.01 && met/meffInc30>0.25&&  nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
signalregionsDict["strong_SR_4Jhighx_bveto"] = signalregionsDict["strong_SR_4Jhighx_btag"]
signalregionsDict["strong_SR_4Jhighx_bveto"] += bveto
signalregionsDict["strong_SR_4Jhighx_btag"] += btag
signalregionsDict["strong_SR_4Jlowx_btag"] = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>250 && mt>150 && mt<450 && LepAplanarity>0.05&&  nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
signalregionsDict["strong_SR_4Jlowx_bveto"] = signalregionsDict["strong_SR_4Jlowx_btag"]
signalregionsDict["strong_SR_4Jlowx_bveto"] += bveto
signalregionsDict["strong_SR_4Jlowx_btag"] += btag
signalregionsDict["strong_SR_6J_btag"] = "lep1Pt>35 && nJet30>=6 && met>350. && mt>175.&& LepAplanarity>0.06&&  nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
# orthogonalise with 9J SR
#signalregionsDict["SR_6J_btag"] += "&&nJet30<=8"
signalregionsDict["strong_SR_6J_bveto"] = signalregionsDict["strong_SR_6J_btag"]
signalregionsDict["strong_SR_6J_bveto"] += bveto
signalregionsDict["strong_SR_6J_btag"] += btag
signalregionsDict["strong_SR_9J"] = "mt>175&&LepAplanarity>0.07&&nJet30>=9&&nLep_signal==1&&nLep_base==1&&lep1Pt>35&&(met/sqrt(Ht30))>8&&meffInc30>1000&&met>200"
# signalregionsDict["strong_SR_9J_lowmet"] = signalregionsDict["strong_SR_9J"] + "&&met<350"


oneleptonbbCommonSelection = "&&  nLep_base==1&&nLep_signal==1 && trigMatch_metTrig"
oneleptonbbSRSelection = "nJet25>=2 && nJet25<=2 && nBJet25_MV2c10==2 && mbb>105. && mbb<135. && mct2>180."
signalregionsDict["1lbb_SRLM"]=  oneleptonbbSRSelection + "&& mt>=100. && mt<140. && met>200." + oneleptonbbCommonSelection
signalregionsDict["1lbb_SRMM"]=  oneleptonbbSRSelection + "&& mt>=140. && mt<200. && met>200." + oneleptonbbCommonSelection
signalregionsDict["1lbb_SRHM"]=  oneleptonbbSRSelection + "&& mt>=200. && met>200." + oneleptonbbCommonSelection

controlregionsDict = collections.OrderedDict()
controlregionsDict['strong_CR_2J_bveto'] = "lep1Pt<35 && nJet30>=2 && met>300 && met<430. && mt>40 && mt<100. && (met/meffInc30) > 0.15 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
controlregionsDict['strong_CR_2J_btag'] = controlregionsDict['strong_CR_2J_bveto']
controlregionsDict['strong_CR_2J_bveto'] += bveto
controlregionsDict['strong_CR_2J_btag'] += btag
controlregionsDict['strong_CR_4Jhighx_bveto'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>300 && mt>50 && mt<200. && LepAplanarity < 0.01 && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
controlregionsDict['strong_CR_4Jhighx_btag'] = controlregionsDict['strong_CR_4Jhighx_bveto']
controlregionsDict['strong_CR_4Jhighx_bveto'] += bveto
controlregionsDict['strong_CR_4Jhighx_btag'] += btag
controlregionsDict['strong_CR_4Jlowx_bveto'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>50 && mt<150. && LepAplanarity > 0.01 && LepAplanarity < 0.05 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
controlregionsDict['strong_CR_4Jlowx_btag'] = controlregionsDict['strong_CR_4Jlowx_bveto']
controlregionsDict['strong_CR_4Jlowx_bveto'] += bveto
controlregionsDict['strong_CR_4Jlowx_btag'] += btag
controlregionsDict['strong_CR_6J_bveto'] = "lep1Pt>35 && nJet30>=6 && met>350 && mt>50 && mt<175. && LepAplanarity < 0.06 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
controlregionsDict['strong_CR_6J_btag'] = controlregionsDict['strong_CR_6J_bveto']
controlregionsDict['strong_CR_6J_bveto'] += bveto
controlregionsDict['strong_CR_6J_btag'] += btag

preselection = "&&nLep_signal==1&&nLep_base==1&&lep1Pt>35&&(met/sqrt(Ht30))>8&&meffInc30>1000&&met>200"
controlregionsDict["strong_CR_9J_B_btag"] = "mt<100&&nJet30>=5&&nJet30<=6" + preselection
controlregionsDict["strong_CR_9J_B_bveto"] = controlregionsDict["strong_CR_9J_B_btag"]
controlregionsDict['strong_CR_9J_B_bveto'] += bveto
controlregionsDict["strong_CR_9J_B_btag"] += btag

controlregionsDict["strong_CR_9J_A_btag"] = "mt>175&&nJet30>=5&&nJet30<=6" + preselection
controlregionsDict["strong_CR_9J_A_bveto"] = controlregionsDict["strong_CR_9J_A_btag"]
controlregionsDict['strong_CR_9J_A_bveto'] += bveto
controlregionsDict["strong_CR_9J_A_btag"] += btag

controlregionsDict["strong_CR_9J_C_btag"] = "mt<100&&LepAplanarity>0.07&&nJet30>=9" + preselection
controlregionsDict["strong_CR_9J_C_bveto"] = controlregionsDict["strong_CR_9J_C_btag"]
controlregionsDict['strong_CR_9J_C_bveto'] += bveto
controlregionsDict["strong_CR_9J_C_btag"] += btag

controlregionsDict["strong_CR_9J_Cprime_btag"] = "mt<100&&LepAplanarity<0.05&&nJet30>=7&&nJet30<=8" + preselection
controlregionsDict["strong_CR_9J_Cprime_bveto"] = controlregionsDict["strong_CR_9J_Cprime_btag"]
controlregionsDict['strong_CR_9J_Cprime_bveto'] += bveto
controlregionsDict["strong_CR_9J_Cprime_btag"] += btag

controlregionsDict["strong_CR_9J_Aprime_btag"] = "mt>100&&mt<175&&nJet30>=5&&nJet30<=6" + preselection
controlregionsDict["strong_CR_9J_Aprime_bveto"] = controlregionsDict["strong_CR_9J_Aprime_btag"]
controlregionsDict['strong_CR_9J_Aprime_bveto'] += bveto
controlregionsDict["strong_CR_9J_Aprime_btag"] += btag

# controlregionsDict['1Lbb_CR_ttbar_incl'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && (mbb<105 || mbb>135) && mt>100 && met>190"
# controlregionsDict['1Lbb_CR_ttbar_low'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && (mbb<105 || mbb>135) && mt>100 && mt<140 && met>190"
# controlregionsDict['1Lbb_CR_ttbar_medium'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && (mbb<105 || mbb>135) && mt>140 && mt<200 && met>200"
# controlregionsDict['1Lbb_CR_ttbar_high'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && (mbb<105 || mbb>135) && mt>200 && met>210"
# controlregionsDict['1Lbb_CR_wjets'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && mbb<80 && mt>40 && mt<100 && met>190"
# controlregionsDict['1Lbb_CR_singletop'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && mbb>195 && mt>100 && met>190"

validationregionsDict = collections.OrderedDict()
validationregionsDict['strong_VR_2J_met'] = "lep1Pt<35 && nJet30>=2 && met>430. && mt>40 && mt<100. && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_2J_mt'] = "lep1Pt<35 && nJet30>=2 && met>300 && met<430. && mt>100. && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_4Jhighx_aplanarity'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>50 && mt<150. && LepAplanarity > 0.05 && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_4Jhighx_mt'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>200 && LepAplanarity < 0.01 && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_4Jhighx_hybrid'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>150 && mt<450. && LepAplanarity > 0.01 && LepAplanarity < 0.05 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_4Jlowx_aplanarity'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>50 && mt<150. && LepAplanarity > 0.05 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_4Jlowx_hybrid'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>150 && mt<450. && LepAplanarity > 0.01 && LepAplanarity < 0.05 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_6J_aplanarity'] = "lep1Pt>35 && nJet30>=6 && met>350 && mt>50 && mt<175. && LepAplanarity > 0.06 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_6J_mt'] = "lep1Pt>35 && nJet30>=6 && met>250 && mt>175 && mt<400. && LepAplanarity < 0.06 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"

validationregionsDict["strong_VR_9J_mt"] = "mt>175&&LepAplanarity<0.05&&nJet30>=7&&nJet30<=8" + preselection
validationregionsDict["strong_VR_9J_njet"] = "mt>100&&mt<175&&LepAplanarity<0.05&&nJet30>=9" + preselection

# validationregionsDict['1Lbb_VR_ttbar_incl'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && mbb>105 && mbb<135 && mt>100 && met>190"
# validationregionsDict['1Lbb_VR_ttbar_low'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && mbb>105 && mbb<135 && mt>100 && mt<140 && met>190"
# validationregionsDict['1Lbb_VR_ttbar_medium'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && mbb>105 && mbb<135 && mt>140 && mt<200 && met>200"
# validationregionsDict['1Lbb_VR_ttbar_high'] = preselectionsDict['1Lbb_presel'] + "&& mct<160 && mbb>105 && mbb<135 && mt>200 && met>210"
#
# validationregionsDict['1Lbb_VR_bbsideband_incl'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && (mbb<105 || (mbb>135&&mbb<195)) && mt>100 && met>190"
# validationregionsDict['1Lbb_VR_bbsideband_low'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && (mbb<105 || (mbb>135&&mbb<195)) && mt>100 && mt<140 && met>190"
# validationregionsDict['1Lbb_VR_bbsideband_medium'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && (mbb<105 || (mbb>135&&mbb<195)) && mt>140 && mt<200 && met>200"
# validationregionsDict['1Lbb_VR_bbsideband_high'] = preselectionsDict['1Lbb_presel'] + "&& mct>160 && (mbb<105 || (mbb>135&&mbb<195)) && mt>200 && met>210"
