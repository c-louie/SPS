#!/usr/bin/env python3

# Include standard modules
import os
import argparse


# Initiate the parser
parser = argparse.ArgumentParser()


# Add long and short argument
parser.add_argument("--org", "-o", help="use --org or -o followed by orgId", required=True)
parser.add_argument("--email", "-m", help="use --email or -m followed by email address", required=True)

print("ABC Template Info")
 
args = parser.parse_args()

if args:
    user_info = os.system('op core list-users %s --filter identity.email:%s | ag -i "(email|name)" | \
    ag -v "(fullName|isEmailVerified|namespace|nickname|Local|modelName)"' % (args.org, args.email))

print(user_info)


