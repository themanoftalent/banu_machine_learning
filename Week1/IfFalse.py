is_hot = False
is_cold = True

if is_hot:
    print('Leave your coat home wear something thin')
elif is_cold:
    print("Wear your coat")
else:
    print("Don't leave home")

print("############################")

x = 30

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


print("############################")

has_good_credit= True
has_criminal_record= False

if has_good_credit and not has_criminal_record:
    print("clean")
elif has_criminal_record and has_good_credit:
    print('Not good not bad')
else:
    print('No entrance for default')
