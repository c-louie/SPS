 #!/usr/bin/env python3

 
LIST="4046 3628 4039 1876 3778 599 3290 3717 3006"
    export IFS=" "
    for ID in $LIST; do op core list-email-alerts $ID | egrep -A 2 '"id": 10478' | egrep -v 'emailAddresses'; done