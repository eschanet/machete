#!/usr/bin/env python
import ROOT
import os

def list_treenames(file, match):
    try:
        basestring
    except NameError:
        basestring = str
    
    tf = ROOT.TFile.Open(file,"READ") if isinstance(file,basestring) else file
    trees_list = []
    for key in tf.GetListOfKeys():
        if str(match) in key.GetName():
            trees_list.append(key.GetName())
    tf.Close()
    return trees_list

def list_branches(file,tree):
    tf = ROOT.TFile.Open(file,"READ") if isinstance(file,basestring) else file
    tree = tf.Get(tree)
    branches_list = []
    for key in tree.GetListOfBranches():
        branches_list.append(key.GetName())
    tf.Close()
    return branches_list
