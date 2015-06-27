import data

def print_users():
    for name, business_unit in data.users:
        print ("Name: '{0}' Business Unit: '{1}'".format(name, business_unit))
        
def business_unit_for_user(user_name):
    for name, business_unit in data.users:
        if name == user_name:
            return business_unit

