#!/usr/bin/env python

import os
import numpy as np
import uproot
import pandas

import argparse

import logging
from commonHelpers.logger import logger
logger = logger.getChild("mephisto")

parser = argparse.ArgumentParser(
    description='This script helps in smearing a distribution in a ROOT file.',
    epilog="You beautiful person, you."
)
parser.add_argument('inputdir', help='The directory containing all the ROOT trees')
parser.add_argument('xsecsfile', help='Text file containing the xsecs')
parser.add_argument('--branch-name','-n', help='the branch name to be smeared', default='mbb')
parser.add_argument('--tag','-t', help='tag after name', default='smeared')
args = parser.parse_args()

if not os.path.isdir(args.inputdir):
    logger.error("Provided path does not exist or is not a directory!")
    raise ValueError("Sorry, need to exit here.")


for indx,f in enumerate(os.listdir(args.inputdir)):

    if not f.endswith("update.root"):
        continue

    logger.info("Updating "+f)
    treename = f.replace("_update.root","_NoSys")
    file = uproot.open(os.path.join(args.inputdir,f))
    tree = file[treename]

    df = tree.pandas.df(tree.keys())

    mu, sigma = 0.98, 0.16
    df[args.branch_name] = df[args.branch_name] * np.random.normal(mu, sigma, df[args.branch_name].shape)

    branches = {key : "{}".format(df[key].dtype) for key in tree.keys()}

    with uproot.recreate(os.path.join(args.inputdir,f.replace(".root","_{}.root".format(args.tag)))) as outfile:
        outfile[treename] = uproot.newtree(branches)
        outfile[treename].extend({key:df[key] for key in tree.keys()})
