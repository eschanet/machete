#!/usr/bin/env python
import ROOT
import os
import argparse
import pprint

import logging
from commonHelpers.logger import logger
logger = logger.getChild("machete")

parser = argparse.ArgumentParser(description="""
Sanity check ROOT tree
""")
parser.add_argument("-file", help="ROOT file")
parser.add_argument('--signal', help='Use signal', action='store_true')

args = parser.parse_args()

tf = ROOT.TFile.Open(args.file,"READ") if isinstance(args.file,basestring) else args.file

trees_list = []
checklist = []
processes = []

for key in tf.GetListOfKeys():
    trees_list.append(key.GetName())

logger.info("{} trees in {}".format(len(trees_list),args.file))

for treename in trees_list:
    # logger.info("Opening {}".format(treename))
    tree = tf.Get(treename)

    if not args.signal:
        processname = treename.split("_")[0]
    else:
        processname = "_".join(treename.split("_", 4)[:4])


    if not processname in processes:
        processes.append(processname)

    mc16a = 0
    mc16d = 0
    mc16e = 0

    mc16a = tree.GetEntries("(RandomRunNumber >= 276262 && RandomRunNumber <= 320000)")
    mc16d = tree.GetEntries("(RandomRunNumber >= 324320 && RandomRunNumber <= 337833)")
    mc16e = tree.GetEntries("(RandomRunNumber >= 348885)")

    if not mc16a > 0:
        logger.error("No MC16A in {}".format(tree))
    if not mc16d > 0:
        logger.error("No MC16D in {}".format(tree))
    if not mc16e > 0:
        logger.error("No MC16E in {}".format(tree))

logger.info("Checking for same amount of trees per process now.")

for process in processes:
    i = 0
    for treename in trees_list:
        if process in treename:
            i += 1
    logger.info("{} has {} trees".format(process, i))


tf.Close()
# pprint.pprint(branches_list)
