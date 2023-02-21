#!/bin/sh

for tweet in /data/Twitter\ dataset/*20-*
do
    nohup ./src/map.py --input_path="$tweet" > outputcheck/$(basename "$tweet"|cut -f 1 -d '.') &
done
