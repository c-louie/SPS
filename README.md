# SPS
Simple Python Scripts for info via the opCLI and cleaning up the output a bit with 'ag'

Info:

You will need the opCLI installed to use any of these. 

I also make use of 'ag' instead of grep. More info about that here:
    https://github.com/ggreer/the_silver_searcher

Scripts use command line arugments, can use --help for more information.

admin_email_info - Script to get admin emails from orgId.

user_info - Uses MasterMode query to filter identities via email.

get_acu_org - get a list of the ACUs, id, and serialNumberBrief for specific orgId.

org_readers - get a list of readers for specific org

shadow_info - combo of above and also spit shadow info out on acu to see if it is down