#!/usr/bin/env python

"""
Wrapper around csv for even simpler reading
"""

from collections import OrderedDict
import csv

cacheName=""
cacheValue=""

def read(csvName,idxCol=0):
    global cacheName
    global cacheValue
    if csvName==cacheName: #sometime we process the same file multiple times...
        return cacheValue
    with open(csvName, 'rb') as f:
        reader = csv.reader(f)
        results=OrderedDict()
        try:
            header=reader.next()
        except StopIteration:
            return {}
        for col in header:
            if header.index(col)==idxCol: continue
            results[col]=OrderedDict()
        for row in reader:
            for col in range(0,len(row)):
                if col==idxCol: continue
                try:
                    results[header[col]][row[idxCol]]=row[col]
                except IndexError:
                    print "Exception in %s" % csvName
                    print "Row: ", row
                    print "Length: %d - expected: %d" % (len(row),len(header))
                    raise
    cacheName=csvName
    cacheValue=results
    return results
