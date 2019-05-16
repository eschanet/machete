import collections


CommonSelection = "&&  nLep_base==1&&nLep_signal==1 && trigMatch_metTrig"
OneEleSelection = "&& (AnalysisType==1 && lep1Pt>7.) "
OneMuoSelection = "&& (AnalysisType==2 && lep1Pt>6.)"
OneLepSelection = "&& ( (AnalysisType==1 && lep1Pt>7.) || (AnalysisType==2 && lep1Pt>6.))"
presel_hard = "nJet30>=4&&lep1Pt>=35&&met>250&&trigMatch_metTrig&&nLep_base==1&&nLep_signal==1"
presel_soft = "nJet30>=2&&lep1Pt<35&&met>250&&trigMatch_metTrig&&nLep_base==1&&nLep_signal==1"
btag = "&&nBJet30_MV2c10>0"
bveto = "&&nBJet30_MV2c10==0"

binnings = collections.OrderedDict()
preselectionsDict = collections.OrderedDict()
signalregionsDict = collections.OrderedDict()
controlregionsDict = collections.OrderedDict()
validationregionsDict = collections.OrderedDict()

binnings["strong_SR_2J_btag"]= [700,1100,1500,1900,2300]
binnings["strong_SR_2J_bveto"]= [700,1100,1500,1900,2300]
binnings["strong_SR_4Jhighx_btag"]= [1000,1500,2000,2500]
binnings["strong_SR_4Jhighx_bveto"]= [1000,1500,2000,2500]
binnings["strong_SR_4Jlowx_btag"]= [1300,1650,2000,2350.]
binnings["strong_SR_4Jlowx_bveto"]= [1300,1650,2000,2350.]
binnings["strong_SR_6J_btag"]= [700,1233.3,1766.6,2300,2833.]
binnings["strong_SR_6J_bveto"]= [700,1233.3,1766.6,2300,2833.]
binnings["strong_SR_9J"]= [1000,1500,2000]



################################################################################################
#
#                       Strong1L
#
################################################################################################

preselectionsDict['strong_presel'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1"
preselectionsDict['strong_presel_electron'] = preselectionsDict['strong_presel'] + OneEleSelection
preselectionsDict['strong_presel_muon'] = preselectionsDict['strong_presel'] + OneMuoSelection

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

strong_preselection = "&&nLep_signal==1&&nLep_base==1&&lep1Pt>35&&(met/sqrt(Ht30))>8&&meffInc30>1000&&met>200"
controlregionsDict["strong_CR_9J_B_btag"] = "mt<100&&nJet30>=5&&nJet30<=6" + strong_preselection
controlregionsDict["strong_CR_9J_B_bveto"] = controlregionsDict["strong_CR_9J_B_btag"]
controlregionsDict['strong_CR_9J_B_bveto'] += bveto
controlregionsDict["strong_CR_9J_B_btag"] += btag

controlregionsDict["strong_CR_9J_A_btag"] = "mt>175&&nJet30>=5&&nJet30<=6" + strong_preselection
controlregionsDict["strong_CR_9J_A_bveto"] = controlregionsDict["strong_CR_9J_A_btag"]
controlregionsDict['strong_CR_9J_A_bveto'] += bveto
controlregionsDict["strong_CR_9J_A_btag"] += btag

controlregionsDict["strong_CR_9J_C_btag"] = "mt<100&&LepAplanarity>0.07&&nJet30>=9" + strong_preselection
controlregionsDict["strong_CR_9J_C_bveto"] = controlregionsDict["strong_CR_9J_C_btag"]
controlregionsDict['strong_CR_9J_C_bveto'] += bveto
controlregionsDict["strong_CR_9J_C_btag"] += btag

controlregionsDict["strong_CR_9J_Cprime_btag"] = "mt<100&&LepAplanarity<0.05&&nJet30>=7&&nJet30<=8" + strong_preselection
controlregionsDict["strong_CR_9J_Cprime_bveto"] = controlregionsDict["strong_CR_9J_Cprime_btag"]
controlregionsDict['strong_CR_9J_Cprime_bveto'] += bveto
controlregionsDict["strong_CR_9J_Cprime_btag"] += btag

controlregionsDict["strong_CR_9J_Aprime_btag"] = "mt>100&&mt<175&&nJet30>=5&&nJet30<=6" + strong_preselection
controlregionsDict["strong_CR_9J_Aprime_bveto"] = controlregionsDict["strong_CR_9J_Aprime_btag"]
controlregionsDict['strong_CR_9J_Aprime_bveto'] += bveto
controlregionsDict["strong_CR_9J_Aprime_btag"] += btag

validationregionsDict['strong_VR_2J_met'] = "lep1Pt<35 && nJet30>=2 && met>430. && mt>40 && mt<100. && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_2J_mt'] = "lep1Pt<35 && nJet30>=2 && met>300 && met<430. && mt>100. && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_4Jhighx_aplanarity'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>50 && mt<150. && LepAplanarity > 0.05 && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_4Jhighx_mt'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>200 && LepAplanarity < 0.01 && (met/meffInc30) > 0.25 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_4Jhighx_hybrid'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>150 && mt<450. && LepAplanarity > 0.01 && LepAplanarity < 0.05 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_4Jlowx_aplanarity'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>50 && mt<150. && LepAplanarity > 0.05 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_4Jlowx_hybrid'] = "lep1Pt>35 && nJet30>=4 && nJet30 <=5 && met>250 && mt>150 && mt<450. && LepAplanarity > 0.01 && LepAplanarity < 0.05 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_6J_aplanarity'] = "lep1Pt>35 && nJet30>=6 && met>350 && mt>50 && mt<175. && LepAplanarity > 0.06 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
validationregionsDict['strong_VR_6J_mt'] = "lep1Pt>35 && nJet30>=6 && met>250 && mt>175 && mt<400. && LepAplanarity < 0.06 && nLep_base==1&&nLep_signal==1 && ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"

validationregionsDict["strong_VR_9J_mt"] = "mt>175&&LepAplanarity<0.05&&nJet30>=7&&nJet30<=8" + CommonSelection
validationregionsDict["strong_VR_9J_njet"] = "mt>100&&mt<175&&LepAplanarity<0.05&&nJet30>=9" + CommonSelection

# preselectionsDict['strong_hard_btag_all'] = presel_hard+btag
# preselectionsDict['strong_hard_bveto_all'] = presel_hard+bveto
# preselectionsDict['strong_hard_btag_muon'] = presel_hard+btag+OneMuoSelection
# preselectionsDict['strong_hard_bveto_muon'] = presel_hard+bveto+OneMuoSelection
# preselectionsDict['strong_hard_btag_electron'] = presel_hard+btag+OneEleSelection
# preselectionsDict['strong_hard_bveto_electron'] = presel_hard+bveto+OneEleSelection
#
# preselectionsDict['strong_soft_btag_all'] = presel_soft+btag
# preselectionsDict['strong_soft_bveto_all'] = presel_soft+bveto
# preselectionsDict['strong_soft_btag_muon'] = presel_soft+btag+OneMuoSelection
# preselectionsDict['strong_soft_bveto_muon'] = presel_soft+bveto+OneMuoSelection
# preselectionsDict['strong_soft_btag_electron'] = presel_soft+btag+OneEleSelection
# preselectionsDict['strong_soft_bveto_electron'] = presel_soft+bveto+OneEleSelection


################################################################################################
#
#                       1Lbb
#
################################################################################################


preselectionsDict['1Lbb_presel'] = "trigMatch_metTrig && nJet30>=2 && nJet30<=3 && nBJet30_MV2c10>=1 && met>220 && mt>50 && nLep_base==1 && nLep_signal==1"
preselectionsDict['1Lbb_presel_electron'] = preselectionsDict['1Lbb_presel'] + OneEleSelection
preselectionsDict['1Lbb_presel_muon'] = preselectionsDict['1Lbb_presel'] + OneMuoSelection

SRSelection        = "met>240. && nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && mbb>100. && mbb<140."
signalregionsDict["1Lbb_SRLM"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>180." + CommonSelection
signalregionsDict["1Lbb_SRLM1"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>180. && mct2<=230." + CommonSelection
signalregionsDict["1Lbb_SRLM2"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>230. && mct2<=280." + CommonSelection
signalregionsDict["1Lbb_SRLM3"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>280." + CommonSelection
signalregionsDict["1Lbb_SRMM"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>180." + CommonSelection
signalregionsDict["1Lbb_SRMM1"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>180. && mct2<=230." + CommonSelection
signalregionsDict["1Lbb_SRMM2"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>230. && mct2<=280." + CommonSelection
signalregionsDict["1Lbb_SRMM3"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>280." + CommonSelection
signalregionsDict["1Lbb_SRHM"]=  SRSelection + "&& mt>=240. && mct2>180. && mlb1>120." + CommonSelection
signalregionsDict["1Lbb_SRHM1"]=  SRSelection + "&& mt>=240. && mct2>180. && mct2<=230. && mlb1>120." + CommonSelection
signalregionsDict["1Lbb_SRHM2"]=  SRSelection + "&& mt>=240. && mct2>230. && mct2<=280. && mlb1>120." + CommonSelection
signalregionsDict["1Lbb_SRHM3"]=  SRSelection + "&& mt>=240. && mct2>280. && mlb1>120." + CommonSelection

TRSelection        = "nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && ((mbb>=50 && mbb<=100.) || mbb>=140.) && mct2<=180."
controlregionsDict["1Lbb_TRLM"]=  TRSelection + "&& mt>=100 && mt<160 && met>240" + CommonSelection
controlregionsDict["1Lbb_TRMM"]=  TRSelection + "&& mt>=160 && mt<240 && met>240" + CommonSelection
controlregionsDict["1Lbb_TRHM"]=  TRSelection + "&& mt>=240 && met>240 && mlb1>120." + CommonSelection
#configMgr.cutsDict["TR"]=  TRSelection + "&& mt>=100. && met>190." + CommonSelection
controlregionsDict["1Lbb_WR"] = "nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && mbb>=50. && mbb<=80. && mct2>180. && mt>50. && mt<100. && met>240." + CommonSelection
controlregionsDict["1Lbb_STCR"] = "nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && mbb>195. && mct2>180. && mt>=100. && met>240." + CommonSelection

VRSelection        = "nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && mct2>180."

validationregionsDict["1Lbb_VRtt1off"] =   VRSelection + "&& mt>=100. && mt<160. && met>220. && ((mbb>=50 && mbb<=80.) || (mbb>=160. && mbb < 195.)) " + CommonSelection
validationregionsDict["1Lbb_VRtt2off"]=  VRSelection + "&& mt>=160. && mt<240. && met>240. && ((mbb>=50 && mbb<=80.) || (mbb>=160. && mbb < 195.)) " + CommonSelection
validationregionsDict["1Lbb_VRtt3off"]=  VRSelection + "&& mt>=240. && met>220. && ((mbb>=50 && mbb<=75.) || (mbb>=165. && mbb < 195.)) " + CommonSelection + "&& eventWeight > -105"

VRSelection2        = "nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && (mbb>100. && mbb<140.) && mct2<=180."

validationregionsDict["1Lbb_VRtt1on"] =   VRSelection2 + "&& mt>=100. && mt<160. && met>240." + CommonSelection
validationregionsDict["1Lbb_VRtt2on"]=  VRSelection2 + "&& mt>=160. && mt<240. && met>240." + CommonSelection
validationregionsDict["1Lbb_VRtt3on"]=  VRSelection2 + "&& mt>=240. && met>220." + CommonSelection

################################################################################################
#
#                       WW
#
################################################################################################

preselectionsDict['weak_presel'] = "trigMatch_metTrig && nJet30>=2 && nJet30<=3 && met>220 && mt>50 && nLep_base==1 && nLep_signal==1"
preselectionsDict['weak_presel_electron'] =  preselectionsDict['weak_presel'] + OneEleSelection
preselectionsDict['weak_presel_muon'] = preselectionsDict['weak_presel'] + OneLepSelection
