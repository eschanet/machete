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
parser.add_argument('inputfiles', help='The input files', nargs='+')
parser.add_argument('--branch-name','-n', help='the branch name to be smeared', default='mbb')
parser.add_argument('--tag','-t', help='tag after name', default='smeared')
parser.add_argument('--loc','-l', help='loc of the skewnorm', default=1.0)
parser.add_argument('--scale','-a', help='scale of the skewnorm', default=0.5)
parser.add_argument('--skew','-k', help='skew of the skewnorm', default=0)
parser.add_argument('--mu','-m', help='mu of the gaussian', default=1.0)
parser.add_argument('--sigma','-s', help='sigma of the gaussian', default=0.5)
parser.add_argument('--method','-e', help='norm or skewnorm', default='norm')
parser.add_argument('--seed',  help='seed for random numbers', default=1234)
args = parser.parse_args()

if not args.method in ['norm', 'skewnorm']:
    logger.error("Provided smearing method not implemented!")
    raise ValueError("Sorry, need to exit here.")

# if not os.path.isdir(args.inputdir):
#     logger.error("Provided path does not exist or is not a directory!")
#     raise ValueError("Sorry, need to exit here.")

np.random.seed(args.seed)

for indx,f in enumerate(args.inputfiles):

    if not f.endswith("update.root"):
        continue

    logger.info("Updating "+f)
    treename = f.replace("_update.root","_NoSys")
    file = uproot.open(os.path.join(f))
    tree = file[treename]

    df = tree.pandas.df(tree.keys())

    if args.method == 'skewnorm':
        distribution = skewnorm(float(args.skew), loc=float(args.loc),scale=float(args.scale))
        df[args.branch_name] = df[args.branch_name] * distribution.rvs(size=df[args.branch_name].shape)
    else:
        df[args.branch_name] = df[args.branch_name] * np.random.normal(float(args.mu), float(args.sigma), df[args.branch_name].shape)

    branches = {key : "{}".format(df[key].dtype) for key in tree.keys()}

    with uproot.recreate(os.path.join(f.replace(".root","_{}.root".format(args.tag)))) as outfile:
        outfile[treename] = uproot.newtree(branches)
        outfile[treename].extend({key:df[key] for key in tree.keys()})
