#!/usr/bin/python

import os
import re
import pprint
import argparse

import json, ast

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

parser = argparse.ArgumentParser(description='Helper to check cross sections of a list of dsids')
# parser.add_argument('datasets', type=str, help='file containing list of datasets')
parser.add_argument('file', type=argparse.FileType('r'), nargs='+')

args = parser.parse_args()

pmg_xsec = "/cvmfs/atlas.cern.ch/repo/sw/database/GroupData/dev/PMGTools/PMGxsecDB_mc16.txt"

print "INFO  -  Checking xsecs in provided list and PMG xsecDB"
print "INFO  -  Opening pmg xsecs file"

with open(pmg_xsec, 'r') as pmg_xsecs:
    pmg_lines = pmg_xsecs.readlines()
dsid_list = []

for f in args.file:
    print "INFO  -  Checking %s" %f
    for line in f:
        hans = "#lse"
        if not line.startswith("mc15"):
            continue
        dsid = line.split(';')[1]
        xsec = float(line.split(';')[3])
        # print "INFO  -  Checking DSID %s" %dsid

        for l in pmg_lines:
            if line.startswith("dataset"):
                continue
            pmg_dsid = l.split('\t\t')[0]
            # print pmg_dsid
            if pmg_dsid == dsid:
                # print "INFO  -  Found DSID %s in PMG" %dsid
                pmg_xsec = float(l.split('\t\t')[2])*0.001
                if not isclose(pmg_xsec,xsec):
                    print "ERROR  -  Xsec for %s is not the same: %.10f and %.10f" %(dsid,xsec,pmg_xsec)
                    dsid_list.append(dsid)
                # else:
                #     print "INFO  -  Xsec for %s matches: %.10f and %.10f" %(dsid,xsec,pmg_xsec)
                continue

# print the entire list to append it to a ticket
print(dsid_list)
