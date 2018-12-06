#!/usr/bin/python

import os
import re
import pyAMI.client
import argparse

parser = argparse.ArgumentParser(description='Helper to get information about a list of datasets')
parser.add_argument('datasets', type=str, help='file containing list of datasets')

args = parser.parse_args()

client = pyAMI.client.Client(
  'atlas'
 )

with open (args.datasets) as datafile:
    print "Did not find the following datasets:"
    for dataset in datafile:
        dataset = dataset.rstrip()
        if dataset[:1] == '#':
            continue
        if dataset[:2] == 'mc':
            ds = "-logicalDatasetName=%s" % dataset
            result = client.execute(['GetDatasetInfo', ds])
            if re.search(r'error', result):
                print dataset
