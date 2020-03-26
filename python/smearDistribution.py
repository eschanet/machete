#!/usr/bin/env python

import os
import numpy as np
import uproot
import pandas

from scipy.stats import skewnorm

import argparse

import logging
from commonHelpers.logger import logger
logger = logger.getChild("mephisto")

parser = argparse.ArgumentParser(
    description='This script helps in smearing a distribution in a ROOT file with a gaussian',
    epilog="You beautiful person, you."
)
parser.add_argument('inputdir', help='The directory containing all the ROOT trees')
parser.add_argument('--branch-name','-n', help='the branch name to be smeared', default='mbb')
parser.add_argument('--tag','-t', help='tag after name', default='smeared')
parser.add_argument('--loc','-l', help='mu of the gaussian', default=1.0)
parser.add_argument('--scale','-a', help='mu of the gaussian', default=0.5)
parser.add_argument('--skew','-k', help='mu of the gaussian', default=0)
parser.add_argument('--mu','-m', help='mu of the gaussian', default=1.0)
parser.add_argument('--sigma','-s', help='sigma of the gaussian', default=0.5)
parser.add_argument('--method','-m', help='norm or skewnorm', default='norm')
parser.add_argument('--seed',  help='seed for random numbers', default=1234)
args = parser.parse_args()

if not args.method in ['norm', 'skewnorm']:
    logger.error("Provided smearing method not implemented!")
    raise ValueError("Sorry, need to exit here.")

if not os.path.isdir(args.inputdir):
    logger.error("Provided path does not exist or is not a directory!")
    raise ValueError("Sorry, need to exit here.")

np.random.seed(args.seed)

for indx,f in enumerate(os.listdir(args.inputdir)):

    if not f.endswith("update.root"):
        continue

    logger.info("Updating "+f)
    treename = f.replace("_update.root","_NoSys")
    file = uproot.open(os.path.join(args.inputdir,f))
    tree = file[treename]

    df = tree.pandas.df(tree.keys())

    if args.method == 'skewnorm':
        distribution = skewnorm(args.skew, loc=args.loc,scale=args.scale)
        df[args.branch_name] = df[args.branch_name] * distribution.rvs(size=df[args.branch_name].shape)
    else:
        df[args.branch_name] = df[args.branch_name] * np.random.normal(float(args.mu), float(args.sigma), df[args.branch_name].shape)

    branches = {key : "{}".format(df[key].dtype) for key in tree.keys()}

    with uproot.recreate(os.path.join(args.inputdir,f.replace(".root","_{}.root".format(args.tag)))) as outfile:
        outfile[treename] = uproot.newtree(branches)
        outfile[treename].extend({key:df[key] for key in tree.keys()})
