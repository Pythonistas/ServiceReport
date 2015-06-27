import argparse
import csv
import data


def print_users():
    for name, business_unit in data.users:
        print ("Name: '{0}' Business Unit: '{1}'".format(name, business_unit))
        
def business_unit_for_user(user_name):
    for name, business_unit in data.users:
        if user_name == name:
            return business_unit

#yield [(user, service), (user, service),...]
#http://stackoverflow.com/questions/17444679/reading-a-huge-csv-in-python
def read_input(input_file): #[CRP]
    with open(input_file) as csvfile:
        
        # Check file for header (Read initial line, and reset read position)
        has_header = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        
        datareader = csv.reader(csvfile, delimiter=',')

        # Skip header row
        if has_header:
            next(datareader)  

        for row in datareader:
            yield row

#yield [(business unit, service), (business unit, service), ...]
def build_business_unit_service(input_file):
    for user, service in read_input(input_file):
        yield (business_unit_for_user(user),service)

#return {service, {business unit, count}, {business unit, count},...} [LR]
def services_by_business_unit(): #[LR]
    pass

def write_report(output_file): #[CRP]
    pass

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('input')

    args = parser.parse_args()

    x = [reportdata for reportdata in build_business_unit_service(args.input)]
    print(x)