import argparse
import collections
import csv
import data
import pprint

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

        for user, service in datareader:
            yield (business_unit_for_user(user),service)

#return {service, {business unit, count}, {business unit, count},...} [LR]
def services_by_business_unit(service_log): #[LR]
    def empty_business_unit_summary():
       return collections.defaultdict(int)

    service_summary = collections.defaultdict(empty_business_unit_summary)
    for business_unit, service in service_log:
        bu_dict = service_summary[service]
        bu_dict[business_unit] += 1

    return service_summary   

        

def write_report(output_file): #[CRP]
    pass

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('input')

    args = parser.parse_args()

    test_dict = services_by_business_unit(read_input(args.input))
    pprint.pprint(test_dict)
    
