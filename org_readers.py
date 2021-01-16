#!/usr/bin/env python3

# Include standard modules
import os
import argparse

# I'm using python 3.8.x
# Grabs readers for specific org

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="use -o or --org followed by orgId", required=True)

# Read arguments from the command line
args = parser.parse_args()

if args.org:
    acus = os.system(' op core list-readers %s |ag -A3 "entries"' % args.org)
    print(acus)
