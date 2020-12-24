# Include standard modules
import os
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="set output width")

# Read arguments from the command line
args = parser.parse_args()

# Check for org
if args.org:
    org_info = os.system('op core describe-org %s | egrep -a "(name|parent)"| egrep -v "(Users|Lockdown Plans|Directory Sync|Sub-Orgs|Unlimited Entries|Unlimited Entries|Elevator I/O Boards|v20")' % args.org)
    print(org_info)