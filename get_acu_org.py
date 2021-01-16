#!/usr/bin/env python3

# Include standard modules
import os
import argparse

# I'm using python 3.8.x
# Grabs serialNumberBrief, Name and ID

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="use -o or --org followed by orgId", required=True)

# Read arguments from the command line
args = parser.parse_args()

if args:
    acus = os.system('op core list-acus %s | ag -A3 "serialNumber" | ag -C1 "id"' % args.org)

print(acus)
