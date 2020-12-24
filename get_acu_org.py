#!/usr/bin/python

# I'm using python 3.8.x
# Include standard modules
import os
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="use -o or --org followed by orgId")

# Read arguments from the command line
args = parser.parse_args()

if args.org:
    acus = os.system('op core list-acus %s | ag -C "serialNumber" | ag -C "id"' % args.org)
    print(acus)