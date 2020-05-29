#!/usr/bin/env python
import ROOT
import os
import argparse
import pprint

parser = argparse.ArgumentParser(description="""
List branches in ROOT tree
""")
parser.add_argument("-file", help="ROOT file")
parser.add_argument("-tree", help="Tree name")

args = parser.parse_args()

tf = ROOT.TFile.Open(args.file,"READ") if isinstance(args.file,basestring) else args.file
tree = tf.Get(args.tree)
branches_list = []
for key in tree.GetListOfBranches():
    branches_list.append(key.GetName())
tf.Close()
pprint.pprint(branches_list)
