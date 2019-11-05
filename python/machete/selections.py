import collections


OneEleSelection = "&& (AnalysisType==1 && lep1Pt>7.) "
OneMuoSelection = "&& (AnalysisType==2 && lep1Pt>6.)"
OneLepSelection = "&& ( (AnalysisType==1 && lep1Pt>7.) || (AnalysisType==2 && lep1Pt>6.))"
presel_hard = "nJet30>=4&&lep1Pt>=35&&met>250&&trigMatch_metTrig&&nLep_base==1&&nLep_signal==1"
presel_soft = "nJet30>=2&&lep1Pt<35&&met>250&&trigMatch_metTrig&&nLep_base==1&&nLep_signal==1"

CommonSelection = "&&  nLep_base==1&&nLep_signal==1 && trigMatch_metTrig" + OneLepSelection

btag = "&&nBJet30_MV2c10>0"
bveto = "&&nBJet30_MV2c10==0"

meff_binning = collections.OrderedDict()
preselectionsDict = collections.OrderedDict()
signalregionsDict = collections.OrderedDict()
controlregionsDict = collections.OrderedDict()
validationregionsDict = collections.OrderedDict()


################################################################################################
#
#                       Strong1L
#
################################################################################################

meff_binning["2J"] = [700.,1150.,1600.,2050.,2500.]
meff_binning["4Jlowx"] = [1000.,1600.,2200.,2800.]
meff_binning["4Jhighx"] = [1000.,1600.,2200.,2800.]
meff_binning["6J"] = [700.,1400,2100,2800,3500.]

preselectionsDict['strong1L_presel'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1"
preselectionsDict['strong1L_presel_electron'] = preselectionsDict['strong1L_presel'] + OneEleSelection
preselectionsDict['strong1L_presel_muon'] = preselectionsDict['strong1L_presel'] + OneMuoSelection


# ------- 2J region --------------------------------------------------------------------------- #
SR2JSelection        = "lep1Pt<35 && nJet30>=2 && met>400. && mt>100. && (met/meffInc30) > 0.35 && (nJet30/lep1Pt)>0.1"
signalregionsDict["strong1L_SR2J"]=  SR2JSelection + CommonSelection
# signalregionsDict["strong1L_SR2JBV"]=SR2JSelection +"&& nBJet30_MV2c10==0" + CommonSelection
# signalregionsDict["strong1L_SR2JBT"]=SR2JSelection +"&& nBJet30_MV2c10>0" + CommonSelection

CR2JSelection        = "lep1Pt<35 && nJet30>=2 && met>300 &&met<400 && mt>50 &&mt<100 && (met/meffInc30)>0.15 && (nJet30/lep1Pt)>0.1"
controlregionsDict["strong1L_TR2J"]=CR2JSelection +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["strong1L_WR2J"]=CR2JSelection +" && nBJet30_MV2c10==0" + CommonSelection

VR2JmtSelection      = "lep1Pt<35 && nJet30>=2 && met>300 && met<400  && mt>100 && (met/meffInc30)>0.10 && (nJet30/lep1Pt)>0.1"
VR2JmetSelection      = "lep1Pt<35 && nJet30>=2 && met>400  && mt>50 &&mt<100 && (met/meffInc30)>0.35 && (nJet30/lep1Pt)>0.1"
validationregionsDict["strong1L_VR2Jmet"]=VR2JmetSelection + CommonSelection
validationregionsDict["strong1L_VR2Jmt"]=VR2JmtSelection + CommonSelection


# ------- 4J regions for gluino gridx high x--------------------------------------------------------------------------- #
SR4JhighxSelection   = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>520 && LepAplanarity>0.01 && met/meffInc30>0.20"
signalregionsDict["strong1L_SR4Jhighx"]=  SR4JhighxSelection + CommonSelection
# signalregionsDict["strong1L_SR4JhighxBV"]=SR4JhighxSelection +"&& nBJet30_MV2c10==0" + CommonSelection
# signalregionsDict["strong1L_SR4JhighxBT"]=SR4JhighxSelection +"&& nBJet30_MV2c10>0" + CommonSelection

CR4JhighxSelection   = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>50 && mt<520 && LepAplanarity<0.01 && met/meffInc30>0.2"
controlregionsDict["strong1L_TR4Jhighx"]=CR4JhighxSelection +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["strong1L_WR4Jhighx"]=CR4JhighxSelection +" && nBJet30_MV2c10==0" + CommonSelection

#VR proposal preliminary
VR4JhighxaplSelection ="lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>50  && mt<150 && LepAplanarity>0.03 && met/meffInc30>0.2"
VR4JhighxmtSelection = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>250 &&met<500 && mt>520 && LepAplanarity<0.01 && met/meffInc30>0.1"
VR4JhighxhybridSelection  = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>250 && mt>150 && mt<520 && LepAplanarity>0.01 && LepAplanarity<0.03" ## VR4Jhybrid
validationregionsDict["strong1L_VR4Jhighxapl"]=VR4JhighxaplSelection + CommonSelection
validationregionsDict["strong1L_VR4Jhighxmt"]=VR4JhighxmtSelection + CommonSelection
validationregionsDict["strong1L_VR4Jhighxhybrid"]=VR4JhighxhybridSelection+ CommonSelection  ## VR4Jhybrid


# ------- 4J regions for gluino gridx low x--------------------------------------------------------------------------- #
SR4JlowxSelection    = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>400 && mt>150 && mt<520 && LepAplanarity>0.03"
signalregionsDict["strong1L_SR4Jlowx"]=  SR4JlowxSelection + CommonSelection
# signalregionsDict["strong1L_SR4JlowxBV"]=SR4JlowxSelection +"&& nBJet30_MV2c10==0" + CommonSelection
# signalregionsDict["strong1L_SR4JlowxBT"]=SR4JlowxSelection +"&& nBJet30_MV2c10>0" + CommonSelection

CR4JlowxSelection    = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>400 && mt>50  && mt<150 && LepAplanarity>0.01 && LepAplanarity<0.03"
controlregionsDict["strong1L_TR4Jlowx"]=CR4JlowxSelection +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["strong1L_WR4Jlowx"]=CR4JlowxSelection +" && nBJet30_MV2c10==0" + CommonSelection

#VR proposal preliminary
VR4JlowxaplSelection = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>50  && mt<150 && LepAplanarity>0.03"
VR4JlowxhybridSelection  = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>250 && mt>150 && mt<520 && LepAplanarity>0.01 && LepAplanarity<0.03" ## VR4Jhybrid
validationregionsDict["strong1L_VR4Jlowxapl"]=VR4JlowxaplSelection+ CommonSelection
validationregionsDict["strong1L_VR4Jlowxhybrid"]=VR4JlowxhybridSelection+ CommonSelection  ## VR4Jhybrid


# ------- 6J regions --------------------------------------------------------------------------- #
SR6JSelection        = "lep1Pt>35 && nJet30>=6 && met>300. && mt>225.&& LepAplanarity>0.05"
signalregionsDict["strong1L_SR6J"]= SR6JSelection + CommonSelection
# signalregionsDict["strong1L_SR6JBV"]=SR6JSelection +"&& nBJet30_MV2c10==0" + CommonSelection
# signalregionsDict["strong1L_SR6JBT"]=SR6JSelection +"&& nBJet30_MV2c10>0" + CommonSelection

CR6JSelection        = "lep1Pt>35 && nJet30>=6 && met>300. && mt>50. && mt<225. && LepAplanarity<0.05"
controlregionsDict["strong1L_TR6J"]=CR6JSelection +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["strong1L_WR6J"]=CR6JSelection +" && nBJet30_MV2c10==0" + CommonSelection

VR6JaplSelection     = "lep1Pt>35 && nJet30>=6 && met>300. && mt>50. && mt<225 && LepAplanarity>0.05"
VR6JmtSelection      = "lep1Pt>35 && nJet30>=6 && met>250. && mt>225. && mt<400 && LepAplanarity<0.05"
validationregionsDict["strong1L_VR6Japl"]=VR6JaplSelection+ CommonSelection
validationregionsDict["strong1L_VR6Jmt"]=VR6JmtSelection+ CommonSelection


################################################################################################
#
#                       1Lbb
#
################################################################################################


preselectionsDict['1Lbb_presel'] = "trigMatch_metTrig && nJet30>=2 && nJet30<=3 && nBJet30_MV2c10>=1 && met>220 && mt>50 && nLep_base==1 && nLep_signal==1"
preselectionsDict['1Lbb_presel_electron'] = preselectionsDict['1Lbb_presel'] + OneEleSelection
preselectionsDict['1Lbb_presel_muon'] = preselectionsDict['1Lbb_presel'] + OneMuoSelection

SRSelection        = "met>240. && nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && mbb>100. && mbb<140."
# signalregionsDict["1Lbb_SRLMincl"]=  SRSelection + "&& mt>=100. && mct2>180." + CommonSelection
signalregionsDict["1Lbb_SRLM_low_mct"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>180. && mct2<=230." + CommonSelection
signalregionsDict["1Lbb_SRLM_high_mct"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>230. && mct2<=280." + CommonSelection
signalregionsDict["1Lbb_SRLM_med_mct"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>280." + CommonSelection
# signalregionsDict["1Lbb_SRMMincl"]=  SRSelection + "&& mt>=160. && mct2>180." + CommonSelection
signalregionsDict["1Lbb_SRMM_low_mct"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>180. && mct2<=230." + CommonSelection
signalregionsDict["1Lbb_SRMM_med_mct"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>230. && mct2<=280." + CommonSelection
signalregionsDict["1Lbb_SRMM_high_mct"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>280." + CommonSelection
# signalregionsDict["1Lbb_SRHMincl"]=  SRSelection + "&& mt>=240. && mct2>180. && mlb1>120." + CommonSelection
signalregionsDict["1Lbb_SRHM_low_mct"]=  SRSelection + "&& mt>=240. && mct2>180. && mct2<=230. && mlb1>120." + CommonSelection
signalregionsDict["1Lbb_SRHM_med_mct"]=  SRSelection + "&& mt>=240. && mct2>230. && mct2<=280. && mlb1>120." + CommonSelection
signalregionsDict["1Lbb_SRHM_high_mct"]=  SRSelection + "&& mt>=240. && mct2>280. && mlb1>120." + CommonSelection

signalregionsDict["1Lbb_SRLM_disc"]=  SRSelection + "&& mt>=100. && mct2>180." + CommonSelection
signalregionsDict["1Lbb_SRMM_disc"]=  SRSelection + "&& mt>=160. && mct2>180." + CommonSelection
signalregionsDict["1Lbb_SRHM_disc"]=  SRSelection + "&& mt>=240. && mct2>180. && mlb1>120." + CommonSelection


TRSelection        = "nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && ((mbb>=50 && mbb<=100.) || mbb>=140.) && mct2<=180."
controlregionsDict["1Lbb_TRLM"]=  TRSelection + "&& mt>=100 && mt<160 && met>240" + CommonSelection
controlregionsDict["1Lbb_TRMM"]=  TRSelection + "&& mt>=160 && mt<240 && met>240" + CommonSelection
controlregionsDict["1Lbb_TRHM"]=  TRSelection + "&& mt>=240 && met>240 && mlb1>120." + CommonSelection
# controlregionsDict["1Lbb_TRincl"]=  TRSelection + "&& mt>=100. && met>240." + CommonSelection
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
