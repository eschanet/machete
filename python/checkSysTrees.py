#!/usr/bin/env python

'''
This script checks if all processes in a root file have the same trees. You don't want to miss one of the input trees, e.g. one of the 10 bazillions of systematic trees.
'''
from __future__ import print_function

import ROOT

import os, subprocess
import sys, re
import argparse

import logging
from commonHelpers.logger import logger
logger = logger.getChild("mephisto")

parser = argparse.ArgumentParser(description='This script checks if all processes in a root file have the same trees. You do not want to miss one of the input trees, e.g. one of the 10 bazillions of systematic trees.')
parser.add_argument('file', help='ROOT file that you want to check')
parser.add_argument('-p', '--processes', nargs='+', help='List of processes', default=["ttbar", "wjets", "zjets", "vh", "tth", "diboson", "multiboson", "singletop", "ttv"])

args = parser.parse_args()

cmd = "rootls {}".format(args.file)
process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

trees = output.split()


raw_names = ["_".join(fullname.split("_")[:5]) for fullname in trees]

unique_names = list(set(raw_names))

split_trees = [[t for t in trees if b in t] for b in unique_names]

for (l,bkg) in zip(split_trees,unique_names):
    logger.info("For process {}: {} trees".format(bkg, len(l)))
