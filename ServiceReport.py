import data

def print_users():
    for name, business_unit in data.users:
        print ("Name: '{0}' Business Unit: '{1}'".format(name, business_unit))
        
def business_unit_for_user(user_name):
    for name, business_unit in data.users:
        if user_name == name:
            return business_unit

#return [(business unit, service), (business unit, service), ...]
def read_input(input_file): #[CRP]
    pass

#return {service, {business unit, count}, {business unit, count},...} [LR]
def services_by_business_unit(): #[LR]
    pass

def write_report(output_file): #[CRP]
    pass