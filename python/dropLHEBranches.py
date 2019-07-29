#!/usr/bin/env python

import ROOT

import sys,glob

for f in glob.glob("/project/etp6/eschanet/bachelor_2019/ntuples/mc16e/v0-2-bachelor-2019/merged/*merged_processed.root"):
    print f
    if ("C1C1" in f) or ("C1N2" in f):
        continue
    rfile = ROOT.TFile.Open(f)
    outfile = ROOT.TFile.Open(f.replace(".root","noLHE.root"), "recreate")
    for tf in rfile.GetListOfKeys():
        print tf
        t = rfile.Get(tf.GetName())
        t.SetBranchStatus('*',1)
        for branch in t.GetListOfBranches():
            if "LHE3Weight" in branch.GetName():
                t.SetBranchStatus(branch.GetName(),0)

        newtree = t.CloneTree()
        # newtree.Write()
    outfile.Write()
