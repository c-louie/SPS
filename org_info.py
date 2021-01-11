#!/usr/bin/env python3

# Include standard modules
import os
import argparse

# I'm using python 3.8.x

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="use --org or -o followed by orgId", required=True)

# Read arguments from the command line
args = parser.parse_args()

# Check for org
if args.org:
    org_info = os.system('op core describe-org %s | egrep -a "(name|parent)"| egrep -v "(Users|Lockdown Plans|Directory Sync|Sub-Orgs| \
        Unlimited Entries|Unlimited Entries|Elevator I/O Boards|v20)"' % args.org)
    
print(org_info)



