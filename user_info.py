#!/usr/bin/env python3

# Include standard modules
import os
import argparse

# I'm using python 3.8.x

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--email", "-m", help="use --email or -m followed by email address")

# Read arguments from the command line
args = parser.parse_args()

# Check for org
if args.email:
    user_info = os.system('op mm list-identities --filter email:%s' % args.email)
    print(user_info)


