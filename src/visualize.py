#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')

hashtags = [
    '#코로나바이러스',  # korean
    '#コロナウイルス',  # japanese
    '#冠状病毒',        # chinese
    '#covid2019',
    '#covid-2019',
    '#covid19',
    '#covid-19',
    '#coronavirus',
    '#corona',
    '#virus',
    '#flu',
    '#sick',
    '#cough',
    '#sneeze',
    '#hospital',
    '#nurse',
    '#doctor',
    ]

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# plotting
topten = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse = True)[:10]
print("TOP 10=", topten)

key = []
value = []

for k, v in topten:
    key.append(k)
    value.append(v)

print("KEY=", key)
print("VALUE=", value)

plt.bar(key, sorted(value), color = 'maroon', width = 0.5)

plt.xlabel("Language")
plt.ylabel("Y Value")

plt.savefig('코로나바이러스_language.png')

