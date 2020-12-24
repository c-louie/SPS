#!/usr/bin/env python3

# I'm using python 3.8.x
# Include standard modules

# Grabs serialNumberBrief, Name and ID
import os
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="use -o or --org followed by orgId")

# Read arguments from the command line
args = parser.parse_args()

if args.org:
    acus = os.system('op core list-acus %s | ag -A3 "serialNumber" | ag -C1 "id"' % args.org)
    print(acus)