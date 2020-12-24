#!/usr/bin/env python3

# Include standard modules
import os
import argparse

# I'm using python 3.8.x
# Script to get admin emails from org

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="use --org or -o followed by orgId")

# Read arguments from the command line
args = parser.parse_args()

# Check for org
if args.org:
    admin = os.system('op core list-role-users %s 5 | ag -i "email"' % args.org)
    print(admin)
else:
    print("You need to add -o <orgId> as argument")