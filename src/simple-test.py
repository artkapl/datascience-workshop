#!/usr/bin/env python3.4

import csv
import ipaddress

with open('../example-data/simple-test-example-bgp-announcements.csv') as csvfile:
    r = csv.reader(csvfile, delimiter=',', dialect='excel')
    next(r)         # skip header
    for row in r:
        try:
            ts=int(row[0])
        except:
            print("Warning. ignoring line %d ('%s')" %(r.line_num, row))
            continue
        try:
            prefix=ipaddress.ip_network(row[1])
        except:
            print("Warning. Prefix should be an valid prefix. But found ('%s'). Ignoring line %d" %(row[1], r.line_num))
            continue
        try:
            asn=int(row[2])
        except:
            print("Warning. ASN should be an int. But found ('%s'). Ignoring line %d" %(row[2], r.line_num))
            continue
        print("ts: %d, prefix=%s, asn=%s" %(ts, prefix, asn))
