met = {
    "varexp" : "met",
    "xmin" : 100,
    "xmax" : 1000,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "E_{T}^{miss}",
}

hardmet = {
    "varexp" : "met",
    "xmin" : 200,
    "xmax" : 1000,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "E_{T}^{miss}",
}

lep1Pt = {
    "varexp" : "lep1Pt",
    "xmin" : 35,
    "xmax" : 1035,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "p_{T}^{lep}",
}

lep1Pt_soft = {
    "varexp" : "lep1Pt",
    "xmin" : 6,
    "xmax" : 35,
    "nbins" : 29,
    "unit" : "GeV",
    "xTitle" : "p_{T}^{lep}",
}

lep1Eta = {
    "varexp" : "lep1Eta",
    "xmin" : -2.5,
    "xmax" : 2.5,
    "nbins" : 20,
    "unit" : None,
    "xTitle" : "Leading lepton #eta",
}

jet1Eta = {
    "varexp" : "jet1Eta",
    "xmin" : -2.8,
    "xmax" : 2.8,
    "nbins" : 20,
    "unit" : None,
    "xTitle" : "Leading jet #eta",
}

meff = {
    "varexp" : "meffInc30",
    "xmin" : 400,
    "xmax" : 3000,
    "nbins" : 26,
    "unit" : "GeV",
    "xTitle" : "m_{eff}",
}

meff_all = {
    "varexp" : "meffInc30",
    "xmin" : 0,
    "xmax" : 2500,
    "nbins" : 25,
    "unit" : "GeV",
    "xTitle" : "m_{eff}",
}

met_over_meff = {
    "varexp" : "met/meffInc30",
    "xmin" : 0.,
    "xmax" : 0.6,
    "nbins" : 10,
    "unit" : None,
    "xTitle" : "E_{T}^{miss}/m_{eff}",
}

ht = {
    "varexp" : "Ht30",
    "xmin" : 120,
    "xmax" : 3020,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "H_{T}",
}

jet1Pt = {
    "varexp" : "jet1Pt",
    "xmin" : 30,
    "xmax" : 2030,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "p_{T}^{jet1}",
}

jet2Pt = {
    "varexp" : "jet2Pt",
    "xmin" : 25,
    "xmax" : 1000,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "p_{T}^{jet2}",
}

jet3Pt = {
    "varexp" : "jet3Pt",
    "xmin" : 25,
    "xmax" : 600,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "p_{T}^{jet3}",
}

jet4Pt = {
    "varexp" : "jet4Pt",
    "xmin" : 25,
    "xmax" : 600,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "p_{T}^{jet4}",
}

mt = {
    "varexp" : "mt",
    "xmin" : 0,
    "xmax" : 600,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "m_{T}",
}

mt_soft = {
    "varexp" : "mt",
    "xmin" : 0,
    "xmax" : 300,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "m_{T}",
}

njet = {
   "varexp" : "nJet30",
    "xmin" : 1.5,
    "xmax" : 11.5,
    "nbins" : 10,
    "xTitle" : "N_{jet}",
    "unit" : None,
}

nbjet25 = {
   "varexp" : "nBJet25_MV2c10",
    "xmin" : 0.5,
    "xmax" : 4.5,
    "nbins" : 4,
    "xTitle" : "N_{bjet}^{25}",
    "unit" : None,
}

njet4 = {
   "varexp" : "nJet30",
    "xmin" : 3.5,
    "xmax" : 11.5,
    "nbins" : 8,
    "xTitle" : "N_{jet}",
    "unit" : None,
}

aplanarity = {
   "varexp" : "LepAplanarity",
    "xmin" : 0.0001,
    "xmax" : 0.2,
    "nbins" : 20,
    "xTitle" : "Aplanarity",
}

mu = {
    "varexp" : "mu",
    "xmin" : 0,
    "xmax" : 80,
    "nbins" : 80,
    "xTitle" : "average #mu",
    "unit" : None,
}

nVtx = {
    "varexp" : "nVtx",
    "xmin" : 0,
    "xmax" : 80,
    "nbins" : 80,
    "xTitle" : "Number of primary vertices",
    "unit" : None,
}

ptmetlep = {
    "varexp" : "sqrt(pow(lep1Pt*cos(lep1Phi)+met*cos(met_Phi), 2)+pow(lep1Pt*sin(lep1Phi)+met*sin(met_Phi), 2))",
    "xmin" : 0,
    "xmax" : 2000,
    "nbins" : 50,
    "xTitle" : "p_{T}(E_{T}^{miss}, l)",
    "unit" : "GeV",
}

mct = {
    "varexp" : "mct",
    "xmin" : 0,
    "xmax" : 600,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "m_{CT}",
}

mbb = {
    "varexp" : "mbb",
    "xmin" : 0,
    "xmax" : 500,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "m_{bb}",
}

mjj = {
    "varexp" : "sqrt(2*jet1Pt*jet2Pt*(cosh(jet1Eta-jet2Eta)-cos(jet1Phi-jet2Phi)))",
    "xmin" : 0,
    "xmax" : 200,
    "nbins" : 20,
    "unit" : "GeV",
    "xTitle" : "m_{jj}",
}

dRJet = {
    "varexp" : "dRJet",
    "xmin" : 0,
    "xmax" : 10,
    "nbins" : 10,
    "unit" : None,
    "xTitle" : "#Delta R(jet1, jet2)",
}

dphimetlep = {
    "varexp" : "abs(TVector2::Phi_mpi_pi(lep1Phi-met_Phi))",
    "xmin" : 0,
    "xmax" : 3.15,
    "nbins" : 15,
    "unit" : None,
    "xTitle" : "#Delta#phi(#bf{p}_{T}^{lep},#bf{p}_{T}^{miss})",
}

metsig = {
    "varexp" : "met_Signif",
    "xmin" : 0,
    "xmax" : 100,
    "nbins" : 50,
    "xTitle" : "E_{T}^{miss} significance",
    "unit" : "GeV",
}


varsDict = {}
varsDict['met'] = met
# varsDict['hardmet'] = hardmet
varsDict['lep1Pt'] = lep1Pt
# varsDict['lep1Pt_soft'] = lep1Pt_soft
varsDict['lep1Eta'] = lep1Eta
varsDict['jet1Eta'] = jet1Eta
varsDict['meff'] = meff
varsDict['met_over_meff'] = met_over_meff
varsDict['ht'] = ht
varsDict['jet1Pt'] = jet1Pt
varsDict['jet2Pt'] = jet2Pt
varsDict['jet3Pt'] = jet3Pt
varsDict['jet4Pt'] = jet4Pt
varsDict['mt'] = mt
varsDict['mct'] = mct
# varsDict['mt_soft'] = mt_soft
varsDict['njet'] = njet
varsDict['nbjet25'] = nbjet25
# varsDict['njet4'] = njet4
varsDict['aplanarity'] = aplanarity
varsDict['mu'] = mu
varsDict['nVtx'] = nVtx
varsDict['ptmetlep'] = ptmetlep
varsDict['meff_all'] = meff_all
varsDict['met_Sig'] = metsig
varsDict['mjj'] = mjj
varsDict['mbb'] = mbb
varsDict['dRJet'] = dRJet
varsDict['dphimetlep'] = dphimetlep
