# Include standard modules
import os
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="use --org or -o followed by orgIdh")

# Read arguments from the command line
args = parser.parse_args()

# Check for org
if args.org:
    admin = os.system('op core describe-org %s' % args.org)
    print(admin)



