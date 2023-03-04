#!/usr/bin/env python3

import matplotlib

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
parser.add_argument('--output_folder',default='plots')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# matplotlib fonts

font_paths = ['/home/Sophia.Huang.24/twitter_coronavirus/NotoSansTC-Regular.otf', '/home/Sophia.Huang.24/twitter_coronavirus/NotoSansKR-Regular.otf', '/home/Sophia.Huang.24/twitter_coronavirus/NotoSansJP-Regular.otf']

properties = []
for path in font_paths:
    properties.append(FontProperties(fname=path))

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
topten = sorted(sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:10], key=lambda x: x[1])
print("Top 10=", topten)

key = []
value = []

for k, v in topten:
    key.append(k)
    value.append(v)

print("Key=", key)
print("Value=", value)

plt.bar(key, value, color = 'maroon', width = 0.5)


# Checking Language

if "コロナウイルス" in os.path.basename(args.key):
    language = "Japanese"
elif "冠状病毒" in os.path.basename(args.key):
    language = "Chinese"
elif "코로나바이러" in os.path.basename(args.key):
    language = "Korean"
else:
    language = "English"

# Depending on whether the input path is for countries or languages, decide what to name x axis and title of plot
if args.input_path == "reduced.country":
    plt.xlabel("Country")
    plt.ylabel("Num")
    if language == "English":
        plt.title("Usage of " + args.key + " in Countries")
    elif language == "Japanese":
        plt.title("Usage of " + args.key + " in Countries", fontproperties=properties[2])
    elif language == "Korean":
        plt.title("Usage of " + args.key + " in Countries", fontproperties=properties[1])
    else:
        plt.title("Usage of " + args.key + " in Countries", fontproperties=properties[0])
else:
    plt.xlabel("Language")
    plt.ylabel("Num")
    plt.title("Usage of " + args.key + " in Languages")

try:
    os.makedirs(args.output_folder)
except FileExistsError:
    pass

# Create files in plots folder for each hashtag
output_path_base = os.path.join(args.output_folder,os.path.basename(args.input_path) + '.' + os.path.basename(args.key))

print("output_path_base=", output_path_base)


# Saving plot to plots folder
try:
    plt.savefig(output_path_base+'.png')
except:
    print("HAVING ERROR SAVING")
