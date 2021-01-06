# Build script with these to gather user info


#   op core list-user-entries <orgId> <userId>                                  list a user's entries
#   op core list-user-acus <orgId> <userId>                                     list a user's ACUs
#   op core list-user-roles <orgId> <userId>                                    list a user's roles
#   op core list-user-zone-users <orgId> <userId>                               list a user's zoneUsers
#   op core list-user-groups <orgId> <userId>                                   list a user's groups

#!/usr/bin/env python3

# Include standard modules
import os
import argparse

# I'm using python 3.8.x

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--org", "-o", help="use --org or -o followed by orgId", required=True)
parser.add_argument("--user", "-I", help="use --user or -I followed by acuId", required=True)


# Read arguments from the command line
# for testing - my userId 1522935
args = parser.parse_args()

if args:
    print("Roles for the user\n")
    role_info = os.system('op core list-user-roles %s %s |ag -A "id|name"' % (args.org, args.user))
    print(role_info)


    print("Entries for the user\n")
    org_info = os.system('op core list-user-entries %s %s | ag -A1 "id"' % (args.org, args.user))
    print(org_info)

    # op core list-user-zone-users <orgId> <userId>
    print("Zones for the user\n")
    zone_info = os.system('op core list-user-zone-users %s %s |ag -A1 "id|name|schedule"' % (args.org, args.user))
    print(zone_info)
    
    # op core list-user-groups <orgId> <userId>
    print("Groups for the user\n")
    group_info = os.system('op core list-user-groups %s %s | ag -A1 "id|name"' % (args.org, args.user))
    print(group_info)