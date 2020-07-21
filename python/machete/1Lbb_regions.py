import collections

OneEleSelection = "&& (AnalysisType==1 && lep1Pt>7.) "
OneMuoSelection = "&& (AnalysisType==2 && lep1Pt>6.)"
OneLepSelection = "&& ( (AnalysisType==1 && lep1Pt>7.) || (AnalysisType==2 && lep1Pt>6.))"

CommonSelection = "&&  nLep_base==1&&nLep_signal==1 && trigMatch_metTrig" + OneLepSelection

btag = "&&nBJet30_MV2c10>0"
bveto = "&&nBJet30_MV2c10==0"

regions = collections.OrderedDict()

################################################################################################
#
#                       1Lbb
#
################################################################################################


# regions['presel'] = "trigMatch_metTrig && nJet30>=2 && nJet30<=3 && nBJet30_MV2c10>=1 && met>220 && mt>50 && nLep_base==1 && nLep_signal==1"
# regions['presel_electron'] = preselectionsDict['presel'] + OneEleSelection
# regions['presel_muon'] = preselectionsDict['presel'] + OneMuoSelection

SRSelection        = "met>240. && nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && mbb>100. && mbb<140."

regions["SRLM_low_mct"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>180. && mct2<=230." + CommonSelection
regions["SRLM_high_mct"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>230. && mct2<=280." + CommonSelection
regions["SRLM_med_mct"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>280." + CommonSelection

regions["SRMM_low_mct"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>180. && mct2<=230." + CommonSelection
regions["SRMM_med_mct"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>230. && mct2<=280." + CommonSelection
regions["SRMM_high_mct"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>280." + CommonSelection

regions["SRHM_low_mct"]=  SRSelection + "&& mt>=240. && mct2>180. && mct2<=230. && mlb1>120." + CommonSelection
regions["SRHM_med_mct"]=  SRSelection + "&& mt>=240. && mct2>230. && mct2<=280. && mlb1>120." + CommonSelection
regions["SRHM_high_mct"]=  SRSelection + "&& mt>=240. && mct2>280. && mlb1>120." + CommonSelection

regions["SRLM_disc"]=  SRSelection + "&& mt>=100. && mct2>180." + CommonSelection
regions["SRMM_disc"]=  SRSelection + "&& mt>=160. && mct2>180." + CommonSelection
regions["SRHM_disc"]=  SRSelection + "&& mt>=240. && mct2>180. && mlb1>120." + CommonSelection

TRSelection        = "nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && ((mbb>=50 && mbb<=100.) || mbb>=140.) && mct2<=180."

regions["TRLM"]=  TRSelection + "&& mt>=100 && mt<160 && met>240" + CommonSelection
regions["TRMM"]=  TRSelection + "&& mt>=160 && mt<240 && met>240" + CommonSelection
regions["TRHM"]=  TRSelection + "&& mt>=240 && met>240 && mlb1>120." + CommonSelection
regions["WR"] = "nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && mbb>=50. && mbb<=80. && mct2>180. && mt>50. && mt<100. && met>240." + CommonSelection
regions["STCR"] = "nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && mbb>195. && mct2>180. && mt>=100. && met>240." + CommonSelection

VRSelection        = "nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && mct2>180."

regions["VRtt1off"] =   VRSelection + "&& mt>=100. && mt<160. && met>220. && ((mbb>=50 && mbb<=80.) || (mbb>=160. && mbb < 195.)) " + CommonSelection
regions["VRtt2off"]=  VRSelection + "&& mt>=160. && mt<240. && met>240. && ((mbb>=50 && mbb<=80.) || (mbb>=160. && mbb < 195.)) " + CommonSelection
regions["VRtt3off"]=  VRSelection + "&& mt>=240. && met>220. && ((mbb>=50 && mbb<=75.) || (mbb>=165. && mbb < 195.)) " + CommonSelection + "&& eventWeight > -105"

VRSelection2        = "nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && (mbb>100. && mbb<140.) && mct2<=180."

regions["VRtt1on"] =   VRSelection2 + "&& mt>=100. && mt<160. && met>240." + CommonSelection
regions["VRtt2on"]=  VRSelection2 + "&& mt>=160. && mt<240. && met>240." + CommonSelection
regions["VRtt3on"]=  VRSelection2 + "&& mt>=240. && met>220." + CommonSelection
