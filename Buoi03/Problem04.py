import re
email = input()

def checkemail(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

    if re.match(regex, email):
        return True
    else:
        return False
    
if checkemail(email):
    print("Valid")
else:
    print("Invalid")