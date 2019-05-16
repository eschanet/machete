import ROOT

import sys,glob

for f in glob.glob("/project/etp3/eschanet/trees/v2-0/merged/bkg/vh*NoSys.root"):
# for f in glob.glob("/project/etp4/eschanet/ntuples/common/mc16d/1Lbb_v2-0-6/merged/vh*NoSys.root.done"):

    rfile = ROOT.TFile.Open(f)
    outfile = ROOT.TFile.Open(f.replace(".root","")+"_noLHE.root", "recreate")
    for tf in rfile.GetListOfKeys():
        print tf
        t = rfile.Get(tf.GetName())
        t.SetBranchStatus('*',1)
        for branch in t.GetListOfBranches():
            if "LHE3Weight" in branch.GetName():
                t.SetBranchStatus(branch.GetName(),0)

        newtree = t.CloneTree()
        newtree.Write()
    outfile.Write()
