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
    tf = ROOT.TFile.Open(file)
    trees_list = []
    for key in tf.GetListOfKeys():
        trees_list.append(key.GetName())
    tf.Close()
    return trees_list

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)
