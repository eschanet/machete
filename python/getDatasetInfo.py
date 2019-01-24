#!/usr/bin/python

import os
import re
import pprint
import pyAMI.client
import pyAMI.atlas.api as AtlasAPI
import argparse

import json, ast

parser = argparse.ArgumentParser(description='Helper to get information about a list of datasets')
# parser.add_argument('datasets', type=str, help='file containing list of datasets')
parser.add_argument('file', type=argparse.FileType('r'), nargs='+')

args = parser.parse_args()

client = pyAMI.client.Client(
  'atlas'
 )

print "INFO  -  Checking AMI status of datasets"

for f in args.file:
    print "INFO  -  Checking %s" %f

    for dataset in f:
        dataset = dataset.rstrip()
        if dataset[:1] == '#':
            continue
        if dataset[:2] == 'mc':
            try:
                result = AtlasAPI.get_dataset_info(client, dataset = dataset)
                result = ast.literal_eval(json.dumps(result))
                if not result[0]['prodsysStatus'] =='ALL EVENTS AVAILABLE':
                    print("WARNING  -  Not ready yet - %s" %dataset)
            except:
                print("ERROR  -  Not in AMI - %s" %dataset)
