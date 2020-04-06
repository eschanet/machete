#!/usr/bin/env python
import ROOT
import os

def is_comment(s):
    """ function to check if a line
         starts with some character.
         Here # for comment
    """
    # return true if a line starts with #
    return s.startswith('#')

def list_treenames(file):
    tf = ROOT.TFile.Open(file,"READ") if isinstance(file,basestring) else file
    trees_list = []
    for key in tf.GetListOfKeys():
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

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

from itertools import tee
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
