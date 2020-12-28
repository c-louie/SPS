#!/usr/bin/env python3

# Include standard modules
import os
import argparse
import json

# I'm using python 3.8.x

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="use --org or -o followed by orgId", required=True)
parser.add_argument("--acu", "-a", help="use --acu or -a followed by acuId", required=True)


# Read arguments from the command line
args = parser.parse_args()

# Check for org
if args:
    org_info = os.system('op core describe-org %s | ag -a "(name|parent)"| ag -v "(Users|Lockdown Plans|Directory Sync|Sub-Orgs|Unlimited Entries|Unlimited Entries|Elevator I/O Boards|v20)"' % args.org)
    print(org_info)

    # Check for ACU status
    shadow = os.system('op core describe-acu %s %s --options withShadows | jq .shadow.state.reported.nova.lastAlertedConnectivityStatus' % (args.org, args.acu))
    print(shadow)

    # List Admin users emails
    admin = os.system('op core list-role-users %s 5 | ag -i "email"' % args.org)
    print(admin)

    # List all ACUs associated with org
    acus = os.system('op core list-acus %s | ag -A3 "serialNumber" | ag -C1 "id"' % args.org)
    print(acus)


    os._exit(-1)



