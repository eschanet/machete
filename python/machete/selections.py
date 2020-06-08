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
alt_meff_binning = collections.OrderedDict()
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
# meff_binning["2J"] = [750.,1050.,1350.,1650.,1950.]
meff_binning["4Jlowx"] = [1000.,1600.,2200.,2800.]
meff_binning["4Jhighx"] = [1000.,1600.,2200.,2800.]
meff_binning["6J"] = [700.,1400,2100,2800,3500.]

# preselectionsDict['strong1L_presel'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1"
# preselectionsDict['strong1L_presel_electron'] = preselectionsDict['strong1L_presel'] + OneEleSelection
# preselectionsDict['strong1L_presel_muon'] = preselectionsDict['strong1L_presel'] + OneMuoSelection

preselectionsDict['alt_strong-1L_presel'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1"
preselectionsDict['alt_strong-1L_presel_BT'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1" + btag
preselectionsDict['alt_strong-1L_presel_BV'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1" + bveto
# preselectionsDict['alt_strong-1L_presel_electron'] = preselectionsDict['alt_strong-1L_presel'] + OneEleSelection
# preselectionsDict['alt_strong-1L_presel_muon'] = preselectionsDict['alt_strong-1L_presel'] + OneMuoSelection

# preselectionsDict['alt_strong-1L_presel_ptW-slice-1'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1 && sqrt(pow(lep1Pt*cos(lep1Phi)+met*cos(met_Phi), 2)+pow(lep1Pt*sin(lep1Phi)+met*sin(met_Phi), 2)) < 70"
# preselectionsDict['alt_strong-1L_presel_ptW-slice-2'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1 && sqrt(pow(lep1Pt*cos(lep1Phi)+met*cos(met_Phi), 2)+pow(lep1Pt*sin(lep1Phi)+met*sin(met_Phi), 2)) >= 70 && sqrt(pow(lep1Pt*cos(lep1Phi)+met*cos(met_Phi), 2)+pow(lep1Pt*sin(lep1Phi)+met*sin(met_Phi), 2)) < 140"
# preselectionsDict['alt_strong-1L_presel_ptW-slice-3'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1 && sqrt(pow(lep1Pt*cos(lep1Phi)+met*cos(met_Phi), 2)+pow(lep1Pt*sin(lep1Phi)+met*sin(met_Phi), 2)) >= 140 && sqrt(pow(lep1Pt*cos(lep1Phi)+met*cos(met_Phi), 2)+pow(lep1Pt*sin(lep1Phi)+met*sin(met_Phi), 2)) < 280"
# preselectionsDict['alt_strong-1L_presel_ptW-slice-4'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1 && sqrt(pow(lep1Pt*cos(lep1Phi)+met*cos(met_Phi), 2)+pow(lep1Pt*sin(lep1Phi)+met*sin(met_Phi), 2)) >= 280 && sqrt(pow(lep1Pt*cos(lep1Phi)+met*cos(met_Phi), 2)+pow(lep1Pt*sin(lep1Phi)+met*sin(met_Phi), 2)) < 500"
# preselectionsDict['alt_strong-1L_presel_ptW-slice-5'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1 && sqrt(pow(lep1Pt*cos(lep1Phi)+met*cos(met_Phi), 2)+pow(lep1Pt*sin(lep1Phi)+met*sin(met_Phi), 2)) >= 500 && sqrt(pow(lep1Pt*cos(lep1Phi)+met*cos(met_Phi), 2)+pow(lep1Pt*sin(lep1Phi)+met*sin(met_Phi), 2)) < 1000"
# preselectionsDict['alt_strong-1L_presel_ptW-slice-6'] = "trigMatch_metTrig && nJet30>=2 && met>250 && mt>50 && nLep_base==1&&nLep_signal==1 && sqrt(pow(lep1Pt*cos(lep1Phi)+met*cos(met_Phi), 2)+pow(lep1Pt*sin(lep1Phi)+met*sin(met_Phi), 2)) >= 1000"


# ------- 2J region --------------------------------------------------------------------------- #
SR2JSelection        = "lep1Pt<35 && nJet30>=2 && met>400 && mt>100. && met/meffInc30>0.35 && (nJet30/lep1Pt)>0.1"
signalregionsDict["strong1L_SR2J"]=  SR2JSelection + CommonSelection
signalregionsDict["strong1L_SR2JBV"]=SR2JSelection +"&& nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["strong1L_SR2JBT"]=SR2JSelection +"&& nBJet30_MV2c10>0" + CommonSelection

signalregionsDict["strong1L_SR2JBTnomet"]="meffInc30>700. && lep1Pt<35 && nJet30>=2 && mt>100. && (met/meffInc30) > 0.35 && (nJet30/lep1Pt)>0.1 && nBJet30_MV2c10>0" + CommonSelection
signalregionsDict["strong1L_SR2JBTnomt"]="meffInc30>700. && lep1Pt<35 && nJet30>=2 && met>400. && (met/meffInc30) > 0.35 && (nJet30/lep1Pt)>0.1 && nBJet30_MV2c10>0" + CommonSelection
signalregionsDict["strong1L_SR2JBVnomet"]="meffInc30>700. && lep1Pt<35 && nJet30>=2 && mt>100. && (met/meffInc30) > 0.35 && (nJet30/lep1Pt)>0.1 && nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["strong1L_SR2JBVnomt"]="meffInc30>700. && lep1Pt<35 && nJet30>=2 && met>400. && (met/meffInc30) > 0.35 && (nJet30/lep1Pt)>0.1 && nBJet30_MV2c10==0" + CommonSelection

CR2JSelection        = "lep1Pt<35 && nJet30>=2 && met>300 &&met<400 && mt>50 &&mt<100 && (met/meffInc30)>0.15 && (nJet30/lep1Pt)>0.1"
controlregionsDict["strong1L_TR2J"]=CR2JSelection +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["strong1L_WR2J"]=CR2JSelection +" && nBJet30_MV2c10==0" + CommonSelection

CR2JSelection_new       = "lep1Pt<35 && nJet30>=2 && met>400 && mt>50 &&mt<75 && (met/meffInc30)>0.35 && (nJet30/lep1Pt)>0.1"
controlregionsDict["strong1L_TR2J_new"]=CR2JSelection_new +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["strong1L_WR2J_new"]=CR2JSelection_new +" && nBJet30_MV2c10==0" + CommonSelection

VR2JmtSelection_new      = "lep1Pt<35 && nJet30>=2 && met>400 && mt>75 && mt<100 && (met/meffInc30)>0.35 && (nJet30/lep1Pt)>0.1"
validationregionsDict["strong1L_VR2JmtBT_new"]=VR2JmtSelection_new + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["strong1L_VR2JmtBV_new"]=VR2JmtSelection_new + "&& nBJet30_MV2c10==0" + CommonSelection


VR2JmtSelection      = "lep1Pt<35 && nJet30>=2 && met>300 && met<400  && mt>100 && (met/meffInc30)>0.10 && (nJet30/lep1Pt)>0.1"
VR2JmetSelection      = "lep1Pt<35 && nJet30>=2 && met>400  && mt>50 &&mt<100 && (met/meffInc30)>0.35 && (nJet30/lep1Pt)>0.1"
VR2JnometSelection="lep1Pt<35 && nJet30>=2 && mt>50 &&mt<100 && (met/meffInc30)>0.35 && (nJet30/lep1Pt)>0.1"
VR2JnomtSelection= "lep1Pt<35 && nJet30>=2 && met>300 && met<400 && (met/meffInc30)>0.10 && (nJet30/lep1Pt)>0.1"
validationregionsDict["strong1L_VR2Jmet"]=VR2JmetSelection + CommonSelection
validationregionsDict["strong1L_VR2Jmt"]=VR2JmtSelection + CommonSelection
validationregionsDict["strong1L_VR2JmetBT"]=VR2JmetSelection + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["strong1L_VR2JmetBV"]=VR2JmetSelection + "&& nBJet30_MV2c10==0" + CommonSelection
validationregionsDict["strong1L_VR2JmtBT"]=VR2JmtSelection + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["strong1L_VR2JmtBV"]=VR2JmtSelection + "&& nBJet30_MV2c10==0" + CommonSelection
# validationregionsDict["strong1L_VR2JmtBVsecondbin"]=VR2JmtSelection + "&& nBJet30_MV2c10==0 && meffInc30 > 1150. && meffInc30 < 1600." + CommonSelection
validationregionsDict["strong1L_VR2Jnomet"]=VR2JnometSelection+ CommonSelection
validationregionsDict["strong1L_VR2Jnomt"]=VR2JnomtSelection + CommonSelection
# validationregionsDict["strong1L_VR2JmtBVthirdbin"]=VR2JmtSelection + "&& nBJet30_MV2c10==0 && meffInc30 > 1600. && meffInc30 < 2050." + CommonSelection

# validationregionsDict["strong1L_VR2JmtBVthirdbin_loose1"]="lep1Pt<35 && nJet30>=2 && met>250 && mt>100 && (met/meffInc30)>0.10 && (nJet30/lep1Pt)>0.1 && nBJet30_MV2c10==0 && meffInc30 > 1600. && meffInc30 < 2050." + "&& nBJet30_MV2c10==0" + CommonSelection
# validationregionsDict["strong1L_VR2JmtBVthirdbin_loose2"]="lep1Pt<35 && nJet30>=2 && met>250 && mt>75 && (met/meffInc30)>0.10 && (nJet30/lep1Pt)>0.1 && nBJet30_MV2c10==0 && meffInc30 > 1600. && meffInc30 < 2050." + "&& nBJet30_MV2c10==0" + CommonSelection
# validationregionsDict["strong1L_VR2JmtBVthirdbin_loose3"]="lep1Pt<35 && nJet30>=2 && met>240 && mt>60 && (met/meffInc30)>0.0 && (nJet30/lep1Pt)>0.1 && nBJet30_MV2c10==0 && meffInc30 > 1600. && meffInc30 < 2050." + "&& nBJet30_MV2c10==0" + CommonSelection


# ------- 4J regions for gluino gridx high x--------------------------------------------------------------------------- #
SR4JhighxSelection   = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>520 && LepAplanarity>0.01 && met/meffInc30>0.20"
signalregionsDict["strong1L_SR4Jhighx"]=  SR4JhighxSelection + CommonSelection
signalregionsDict["strong1L_SR4JhighxBV"]=SR4JhighxSelection +"&& nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["strong1L_SR4JhighxBT"]=SR4JhighxSelection +"&& nBJet30_MV2c10>0" + CommonSelection

signalregionsDict["strong1L_SR4JhighxBTnomet"]="meffInc30>1000. && lep1Pt>35 && nJet30>=4 && nJet30<6 && mt>520 && LepAplanarity>0.03 && met/meffInc30>0.2 && nBJet30_MV2c10>0" + CommonSelection
signalregionsDict["strong1L_SR4JhighxBTnomt"]="meffInc30>1000. && lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && LepAplanarity>0.03 && met/meffInc30>0.2 && nBJet30_MV2c10>0" + CommonSelection
signalregionsDict["strong1L_SR4JhighxBVnomet"]="meffInc30>1000. && lep1Pt>35 && nJet30>=4 && nJet30<6 && mt>520 && LepAplanarity>0.03 && met/meffInc30>0.2 && nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["strong1L_SR4JhighxBVnomt"]="meffInc30>1000. && lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && LepAplanarity>0.03 && met/meffInc30>0.2 && nBJet30_MV2c10==0" + CommonSelection


CR4JhighxSelection   = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>50 && mt<520 && LepAplanarity<0.01 && met/meffInc30>0.2"
controlregionsDict["strong1L_TR4Jhighx"]=CR4JhighxSelection +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["strong1L_WR4Jhighx"]=CR4JhighxSelection +" && nBJet30_MV2c10==0" + CommonSelection

#VR proposal preliminary
VR4JhighxaplSelection ="lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>50  && mt<150 && LepAplanarity>0.03 && met/meffInc30>0.2"
VR4JhighxmtSelection = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>250 &&met<500 && mt>520 && LepAplanarity<0.01 && met/meffInc30>0.1"
VR4JhighxhybridSelection  = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>250 && mt>150 && mt<520 && LepAplanarity>0.01 && LepAplanarity<0.03" ## VR4Jhybrid
VR4JhighxnoaplSelection ="lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>50  && mt<150 && met/meffInc30>0.2"
VR4JhighxnomtSelection = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>250 && met<500 && LepAplanarity<0.01 && met/meffInc30>0.1"
validationregionsDict["strong1L_VR4Jhighxapl"]=VR4JhighxaplSelection + CommonSelection
validationregionsDict["strong1L_VR4Jhighxmt"]=VR4JhighxmtSelection + CommonSelection
validationregionsDict["strong1L_VR4Jhighxhybrid"]=VR4JhighxhybridSelection + CommonSelection ## VR4Jhybrid
validationregionsDict["strong1L_VR4JhighxaplBT"]=VR4JhighxaplSelection + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["strong1L_VR4JhighxaplBV"]=VR4JhighxaplSelection + "&& nBJet30_MV2c10==0" + CommonSelection
validationregionsDict["strong1L_VR4JhighxmtBT"]=VR4JhighxmtSelection + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["strong1L_VR4JhighxmtBV"]=VR4JhighxmtSelection + "&& nBJet30_MV2c10==0" + CommonSelection
validationregionsDict["strong1L_VR4JhighxhybridBT"]=VR4JhighxhybridSelection + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["strong1L_VR4JhighxhybridBV"]=VR4JhighxhybridSelection + "&& nBJet30_MV2c10==0" + CommonSelection
validationregionsDict["strong1L_VR4Jhighxnoapl"]=VR4JhighxnoaplSelection+ CommonSelection
validationregionsDict["strong1L_VR4Jhighxnomt"]=VR4JhighxnomtSelection+ CommonSelection

validationregionsDict["strong1L_VR4JhighxmtBVbin2"]="lep1Pt>35 && nJet30>=4 && nJet30<6 && met>250 &&met<500 && mt>520 && LepAplanarity<0.01 && met/meffInc30>0.1 && meffInc30 > 1600. && meffInc30 < 2200." + "&& nBJet30_MV2c10==0" + CommonSelection
validationregionsDict["strong1L_VR4JhighxmtBVbin2_loose1"]="lep1Pt>35 && nJet30>=4 && nJet30<6 && met>240 && mt>520 && LepAplanarity<0.01 && met/meffInc30>0.1 && meffInc30 > 1600. && meffInc30 < 2200." + "&& nBJet30_MV2c10==0" + CommonSelection
validationregionsDict["strong1L_VR4JhighxmtBVbin2_loose2"]="lep1Pt>35 && nJet30>=4 && nJet30<6 && met>240 && mt>480 && LepAplanarity<0.01 && met/meffInc30>0.1 && meffInc30 > 1600. && meffInc30 < 2200." + "&& nBJet30_MV2c10==0" + CommonSelection
validationregionsDict["strong1L_VR4JhighxmtBVbin2_loose3"]="lep1Pt>35 && nJet30>=4 && nJet30<6 && met>220 && mt>350 && LepAplanarity<0.01 && met/meffInc30>0.1 && meffInc30 > 1600. && meffInc30 < 2200." + "&& nBJet30_MV2c10==0" + CommonSelection


# ------- 4J regions for gluino gridx low x--------------------------------------------------------------------------- #
SR4JlowxSelection    = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>400 && mt>150 && mt<520 && LepAplanarity>0.03"
signalregionsDict["strong1L_SR4Jlowx"]=  SR4JlowxSelection + CommonSelection
signalregionsDict["strong1L_SR4JlowxBV"]=SR4JlowxSelection +"&& nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["strong1L_SR4JlowxBT"]=SR4JlowxSelection +"&& nBJet30_MV2c10>0" + CommonSelection

signalregionsDict["strong1L_SR4JlowxBVnomet"]="meffInc30>1000. && lep1Pt>35 && nJet30>=4 && nJet30<6 && mt>150 && mt<520 && LepAplanarity>0.03 && nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["strong1L_SR4JlowxBVnomt"]="meffInc30>1000. && lep1Pt>35 && nJet30>=4 && nJet30<6 && met>400 && LepAplanarity>0.03 && nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["strong1L_SR4JlowxBTnomet"]="meffInc30>1000. && lep1Pt>35 && nJet30>=4 && nJet30<6 && mt>150 && mt<520 && LepAplanarity>0.03 && nBJet30_MV2c10>0" + CommonSelection
signalregionsDict["strong1L_SR4JlowxBTnomt"]="meffInc30>1000. && lep1Pt>35 && nJet30>=4 && nJet30<6 && met>400 && LepAplanarity>0.03 && nBJet30_MV2c10>0" + CommonSelection


CR4JlowxSelection    = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>400 && mt>50  && mt<150 && LepAplanarity>0.01 && LepAplanarity<0.03"
controlregionsDict["strong1L_TR4Jlowx"]=CR4JlowxSelection +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["strong1L_WR4Jlowx"]=CR4JlowxSelection +" && nBJet30_MV2c10==0" + CommonSelection

#VR proposal preliminary
VR4JlowxaplSelection = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>50  && mt<150 && LepAplanarity>0.03"
VR4JlowxhybridSelection  = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>250 && mt>150 && mt<520 && LepAplanarity>0.01 && LepAplanarity<0.03" ## VR4Jhybrid
VR4JlowxnoaplSelection = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>300 && mt>50  && mt<520"
VR4JlowxnomtSelection  = "lep1Pt>35 && nJet30>=4 && nJet30<6 && met>250 && LepAplanarity>0.01 && LepAplanarity<0.03"
validationregionsDict["strong1L_VR4Jlowxapl"]=VR4JlowxaplSelection+ CommonSelection
validationregionsDict["strong1L_VR4Jlowxhybrid"]=VR4JlowxhybridSelection+ CommonSelection  ## VR4Jhybrid
validationregionsDict["strong1L_VR4JlowxaplBT"]=VR4JlowxaplSelection + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["strong1L_VR4JlowxaplBV"]=VR4JlowxaplSelection + "&& nBJet30_MV2c10==0" + CommonSelection
validationregionsDict["strong1L_VR4JlowxhybridBT"]=VR4JlowxhybridSelection + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["strong1L_VR4JlowxhybridBV"]=VR4JlowxhybridSelection + "&& nBJet30_MV2c10==0" + CommonSelection
validationregionsDict["strong1L_VR4Jlowxnoapl"]=VR4JlowxnoaplSelection+ CommonSelection
validationregionsDict["strong1L_VR4Jlowxnomt"]=VR4JlowxnomtSelection+ CommonSelection


# ------- 6J regions --------------------------------------------------------------------------- #
SR6JSelection        = "lep1Pt>35 && nJet30>=6 && met>300. && mt>225.&& LepAplanarity>0.05"
signalregionsDict["strong1L_SR6J"]= SR6JSelection + CommonSelection
signalregionsDict["strong1L_SR6JBV"]=SR6JSelection +"&& nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["strong1L_SR6JBT"]=SR6JSelection +"&& nBJet30_MV2c10>0" + CommonSelection

signalregionsDict["strong1L_SR6JBTnomet"]="meffInc30>700. && lep1Pt>35 && nJet30>=6 && mt>225.&& LepAplanarity>0.05 && nBJet30_MV2c10>0" + CommonSelection
signalregionsDict["strong1L_SR6JBTnomt"]="meffInc30>700. && lep1Pt>35 && nJet30>=6 && met>300. && LepAplanarity>0.05 && nBJet30_MV2c10>0" + CommonSelection
signalregionsDict["strong1L_SR6JBVnomet"]="meffInc30>700. && lep1Pt>35 && nJet30>=6 && mt>225.&& LepAplanarity>0.05 && nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["strong1L_SR6JBVnomt"]="meffInc30>700. && lep1Pt>35 && nJet30>=6 && met>300. && LepAplanarity>0.05 && nBJet30_MV2c10==0" + CommonSelection

CR6JSelection        = "lep1Pt>35 && nJet30>=6 && met>300. && mt>50. && mt<225. && LepAplanarity<0.05"
controlregionsDict["strong1L_TR6J"]=CR6JSelection +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["strong1L_WR6J"]=CR6JSelection +" && nBJet30_MV2c10==0" + CommonSelection

VR6JaplSelection     = "lep1Pt>35 && nJet30>=6 && met>300. && mt>50. && mt<225 && LepAplanarity>0.05"
VR6JmtSelection      = "lep1Pt>35 && nJet30>=6 && met>250. && mt>225. && mt<400 && LepAplanarity<0.05"
VR6JnoaplSelection     = "lep1Pt>35 && nJet30>=6 && met>300. && mt>50. && mt<225"
VR6JnomtSelection      = "lep1Pt>35 && nJet30>=6 && met>250. && LepAplanarity<0.05"
validationregionsDict["strong1L_VR6Japl"]=VR6JaplSelection+ CommonSelection
validationregionsDict["strong1L_VR6Jmt"]=VR6JmtSelection+ CommonSelection
validationregionsDict["strong1L_VR6JaplBT"]=VR6JaplSelection + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["strong1L_VR6JaplBV"]=VR6JaplSelection + "&& nBJet30_MV2c10==0" + CommonSelection
validationregionsDict["strong1L_VR6JmtBT"]=VR6JmtSelection + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["strong1L_VR6JmtBV"]=VR6JmtSelection + "&& nBJet30_MV2c10==0" + CommonSelection
validationregionsDict["strong1L_VR6Jnoapl"]=VR6JnoaplSelection+CommonSelection
validationregionsDict["strong1L_VR6Jnomt"]=VR6JnomtSelection+ CommonSelection


################################################################################################
#
#                       ALTERNATIVE STRONG1L MT STRATEGY
#
################################################################################################

alt_meff_binning["2J"] = [700.,1300.,1900.,2500.]
alt_meff_binning["4J"] = [1000.,1600.,2200.,2800.]
alt_meff_binning["SR6J"] = [700.,1400,2100,2800,3500.]
alt_meff_binning["TR6J"] = [700.,1400,2100,2800.,3500.]
alt_meff_binning["WR6J"] = [700.,1400,2100,2800.,3500.]
alt_meff_binning["VR6J"] = [700.,1400,2100,2800.]

#first part: common selections, SR, CR, VR
CommonSelection = "&&  nLep_base==1&&nLep_signal==1 && trigMatch_metTrig"## TSTcleaning here
OneEleSelection = "&& (AnalysisType==1 && lep1Pt>7) "
OneMuoSelection = "&& (AnalysisType==2 && lep1Pt>6)"
OneLepSelection = "&& ( (AnalysisType==1 && lep1Pt>7) || (AnalysisType==2 && lep1Pt>6))"
TwoLepSelection = "&&  nLep_base>=2 && nLep_signal>=2 && trigMatch_metTrig"

# ------- 2J region --------------------------------------------------------------------------- #
SR2JSelection        = "lep1Pt<25 && nJet30>=2 && met>400. && mt>100. && (met/meffInc30) > 0.25 && (nJet30/lep1Pt)>0.1"
signalregionsDict["alt_strong-1L_SR2J"]=  SR2JSelection + CommonSelection
signalregionsDict["alt_strong-1L_SR2JBV"]=SR2JSelection +"&& nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["alt_strong-1L_SR2JBT"]=SR2JSelection +"&& nBJet30_MV2c10>0" + CommonSelection

CR2JSelection        = "lep1Pt<25 && nJet30>=2 && met>400 && mt>50 &&mt<80. && (met/meffInc30)>0.25 && (nJet30/lep1Pt)>0.1"
controlregionsDict["alt_strong-1L_TR2J"]=CR2JSelection +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["alt_strong-1L_WR2J"]=CR2JSelection +" && nBJet30_MV2c10==0" + CommonSelection

VR2JmetSelection      = "lep1Pt<25 && nJet30>=2 && met>400.  && mt>80. &&mt<100 && (met/meffInc30)>0.25 && (nJet30/lep1Pt)>0.1"

validationregionsDict["alt_strong-1L_VR2J"]=VR2JmetSelection + CommonSelection
validationregionsDict["alt_strong-1L_VR2JBT"]=VR2JmetSelection + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["alt_strong-1L_VR2JBV"]=VR2JmetSelection + "&& nBJet30_MV2c10==0" + CommonSelection

# ------- 4J regions --------------------------------------------------------------------------- #
SR4JhighxSelection   = "lep1Pt>25 && nJet30>=4 && nJet30<6 && met>300 && mt>520 && LepAplanarity>0.01 && met/meffInc30>0.20"
signalregionsDict["alt_strong-1L_SR4Jhighx"]=  SR4JhighxSelection + CommonSelection
signalregionsDict["alt_strong-1L_SR4JhighxBV"]=SR4JhighxSelection +"&& nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["alt_strong-1L_SR4JhighxBT"]=SR4JhighxSelection +"&& nBJet30_MV2c10>0" + CommonSelection


CR4JhighxSelection   = "lep1Pt>25 && nJet30>=4 && nJet30<6 && met>300 && mt>50 && mt<90 && LepAplanarity>0.01 && met/meffInc30>0.2"
controlregionsDict["alt_strong-1L_TR4J"]=CR4JhighxSelection +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["alt_strong-1L_WR4J"]=CR4JhighxSelection +" && nBJet30_MV2c10==0" + CommonSelection

#VR
VR4JhighxSelection ="lep1Pt>25 && nJet30>=4 && nJet30<6 && met>300 && mt>90  && mt<150 && LepAplanarity>0.01 && met/meffInc30>0.2"

validationregionsDict["alt_strong-1L_VR4J"]=VR4JhighxSelection + CommonSelection
validationregionsDict["alt_strong-1L_VR4JBT"]=VR4JhighxSelection + "&& nBJet30_MV2c10>0" + CommonSelection
validationregionsDict["alt_strong-1L_VR4JBV"]=VR4JhighxSelection + "&& nBJet30_MV2c10==0" + CommonSelection

SR4JlowxSelection    = "lep1Pt>25 && nJet30>=4 && nJet30<6 && met>300 && mt>150 && mt<520 && LepAplanarity>0.01 && met/meffInc30>0.2"
signalregionsDict["alt_strong-1L_SR4Jlowx"]=  SR4JlowxSelection + CommonSelection
signalregionsDict["alt_strong-1L_SR4JlowxBV"]=SR4JlowxSelection +"&& nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["alt_strong-1L_SR4JlowxBT"]=SR4JlowxSelection +"&& nBJet30_MV2c10>0" + CommonSelection

# ------- 6J regions --------------------------------------------------------------------------- #
SR6JSelection        = "lep1Pt>25 && nJet30>=6 && met>300. && mt>225.&& LepAplanarity>0.05"
signalregionsDict["alt_strong-1L_SR6J"]= SR6JSelection + CommonSelection
signalregionsDict["alt_strong-1L_SR6JBV"]=SR6JSelection +"&& nBJet30_MV2c10==0" + CommonSelection
signalregionsDict["alt_strong-1L_SR6JBT"]=SR6JSelection +"&& nBJet30_MV2c10>0" + CommonSelection

CR6JSelection        = "lep1Pt>25 && nJet30>=6 && met>250. && mt>50. && mt<100. && LepAplanarity>0.05"
controlregionsDict["alt_strong-1L_TR6J"]=CR6JSelection +" && nBJet30_MV2c10>0" + CommonSelection
controlregionsDict["alt_strong-1L_WR6J"]=CR6JSelection +" && nBJet30_MV2c10==0" + CommonSelection

VR6JSelection     = "lep1Pt>25 && nJet30>=6 && met>250. && mt>100. && mt<225. && LepAplanarity>0.05"

validationregionsDict["alt_strong-1L_VR6J"]=VR6JSelection+ CommonSelection
validationregionsDict["alt_strong-1L_VR6JBT"]=VR6JSelection + "&& nBJet30_MV2c10>0 && meffInc30<2800." + CommonSelection
validationregionsDict["alt_strong-1L_VR6JBV"]=VR6JSelection + "&& nBJet30_MV2c10==0 && meffInc30<2800." + CommonSelection


################################################################################################
#
#                       1Lbb
#
################################################################################################


# preselectionsDict['1Lbb_presel'] = "trigMatch_metTrig && nJet30>=2 && nJet30<=3 && nBJet30_MV2c10>=1 && met>220 && mt>50 && nLep_base==1 && nLep_signal==1"
# preselectionsDict['1Lbb_presel_electron'] = preselectionsDict['1Lbb_presel'] + OneEleSelection
# preselectionsDict['1Lbb_presel_muon'] = preselectionsDict['1Lbb_presel'] + OneMuoSelection

SRSelection        = "met>240. && nJet30>=2 && nJet30<=3 && nBJet30_MV2c10==2 && mbb>100. && mbb<140."
signalregionsDict["1Lbb_SRLMincl"]=  SRSelection + "&& mt>=100. && mct2>180." + CommonSelection
signalregionsDict["1Lbb_SRLM_low_mct"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>180. && mct2<=230." + CommonSelection
signalregionsDict["1Lbb_SRLM_med_mct"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>230. && mct2<=280." + CommonSelection
signalregionsDict["1Lbb_SRLM_high_mct"]=  SRSelection + "&& mt>=100. && mt<160. && mct2>280." + CommonSelection
signalregionsDict["1Lbb_SRMMincl"]=  SRSelection + "&& mt>=160. && mct2>180." + CommonSelection
signalregionsDict["1Lbb_SRMM_low_mct"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>180. && mct2<=230." + CommonSelection
signalregionsDict["1Lbb_SRMM_med_mct"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>230. && mct2<=280." + CommonSelection
signalregionsDict["1Lbb_SRMM_high_mct"]=  SRSelection + "&& mt>=160. && mt<240. && mct2>280." + CommonSelection
signalregionsDict["1Lbb_SRHMincl"]=  SRSelection + "&& mt>=240. && mct2>180. && mlb1>120." + CommonSelection
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

# preselectionsDict['weak_presel'] = "trigMatch_metTrig && nJet30>=2 && nJet30<=3 && met>220 && mt>50 && nLep_base==1 && nLep_signal==1"
# preselectionsDict['weak_presel_electron'] =  preselectionsDict['weak_presel'] + OneEleSelection
# preselectionsDict['weak_presel_muon'] = preselectionsDict['weak_presel'] + OneLepSelection


################################################################################################
#
#                       2L0J
#
################################################################################################

Common = "nLeps==2 && L2nCentralBJet==0 && MET>110000 && METsig>10"
DFSelection = Common + " && L2isEMU && L2Mll>100000"
SFSelection = Common + " && (L2isMUMU || L2isEMU) && L2Mll>121200"
ZeroJet = " && L2nCentralLightJet==0"
OneJet = " && L2nCentralLightJet==1"

signalregionsDict["EwkTwoLeptonZeroJet2018__DF_0J_a"] = DFSelection + ZeroJet + " && L2MT2>100000 && L2MT2<=105000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_0J_b"] = DFSelection + ZeroJet + " && L2MT2>105000 && L2MT2<=110000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_0J_c"] = DFSelection + ZeroJet + " && L2MT2>110000 && L2MT2<=120000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_0J_d"] = DFSelection + ZeroJet + " && L2MT2>120000 && L2MT2<=140000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_0J_e"] = DFSelection + ZeroJet + " && L2MT2>140000 && L2MT2<=160000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_0J_f"] = DFSelection + ZeroJet + " && L2MT2>160000 && L2MT2<=180000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_0J_g"] = DFSelection + ZeroJet + " && L2MT2>180000 && L2MT2<=220000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_0J_h"] = DFSelection + ZeroJet + " && L2MT2>220000 && L2MT2<=260000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_0J_i"] = DFSelection + ZeroJet + " && L2MT2>260000"

signalregionsDict["EwkTwoLeptonZeroJet2018__SF_0J_a"] = SFSelection + ZeroJet + " && L2MT2>100000 && L2MT2<=105000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_0J_b"] = SFSelection + ZeroJet + " && L2MT2>105000 && L2MT2<=110000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_0J_c"] = SFSelection + ZeroJet + " && L2MT2>110000 && L2MT2<=120000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_0J_d"] = SFSelection + ZeroJet + " && L2MT2>120000 && L2MT2<=140000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_0J_e"] = SFSelection + ZeroJet + " && L2MT2>140000 && L2MT2<=160000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_0J_f"] = SFSelection + ZeroJet + " && L2MT2>160000 && L2MT2<=180000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_0J_g"] = SFSelection + ZeroJet + " && L2MT2>180000 && L2MT2<=220000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_0J_h"] = SFSelection + ZeroJet + " && L2MT2>220000 && L2MT2<=260000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_0J_i"] = SFSelection + ZeroJet + " && L2MT2>260000"

signalregionsDict["EwkTwoLeptonZeroJet2018__DF_1J_a"] = DFSelection + OneJet + " && L2MT2>100000 && L2MT2<=105000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_1J_b"] = DFSelection + OneJet + " && L2MT2>105000 && L2MT2<=110000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_1J_c"] = DFSelection + OneJet + " && L2MT2>110000 && L2MT2<=120000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_1J_d"] = DFSelection + OneJet + " && L2MT2>120000 && L2MT2<=140000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_1J_e"] = DFSelection + OneJet + " && L2MT2>140000 && L2MT2<=160000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_1J_f"] = DFSelection + OneJet + " && L2MT2>160000 && L2MT2<=180000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_1J_g"] = DFSelection + OneJet + " && L2MT2>180000 && L2MT2<=220000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_1J_h"] = DFSelection + OneJet + " && L2MT2>220000 && L2MT2<=260000"
signalregionsDict["EwkTwoLeptonZeroJet2018__DF_1J_i"] = DFSelection + OneJet + " && L2MT2>260000"

signalregionsDict["EwkTwoLeptonZeroJet2018__SF_1J_a"] = SFSelection + OneJet + " && L2MT2>100000 && L2MT2<=105000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_1J_b"] = SFSelection + OneJet + " && L2MT2>105000 && L2MT2<=110000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_1J_c"] = SFSelection + OneJet + " && L2MT2>110000 && L2MT2<=120000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_1J_d"] = SFSelection + OneJet + " && L2MT2>120000 && L2MT2<=140000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_1J_e"] = SFSelection + OneJet + " && L2MT2>140000 && L2MT2<=160000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_1J_f"] = SFSelection + OneJet + " && L2MT2>160000 && L2MT2<=180000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_1J_g"] = SFSelection + OneJet + " && L2MT2>180000 && L2MT2<=220000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_1J_h"] = SFSelection + OneJet + " && L2MT2>220000 && L2MT2<=260000"
signalregionsDict["EwkTwoLeptonZeroJet2018__SF_1J_i"] = SFSelection + OneJet + " && L2MT2>260000"
