

lst = "4046,3628,4039,1876,3778,599,3290,3717,3006"

for id_num in lst:
    do: {"op core list-email-alerts %id_num | grep -A2 'id:10478' | egrep -v 'emailAddresses'"}
