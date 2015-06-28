import argparse
import collections
import csv
import data


def print_users():
    for name, business_unit in data.users:
        print ("Name: '{0}' Business Unit: '{1}'".format(name, business_unit))


def business_unit_for_user(user_name):
    for name, business_unit in data.users:
        if user_name == name:
            return business_unit


def sorted_business_units():
    return sorted(set([business_unit for users, business_unit in data.users]))


#yield [(user, service), (user, service),...]
#http://stackoverflow.com/questions/17444679/reading-a-huge-csv-in-python
def read_input(input_file): #[CRP]
    with open(input_file) as csvfile:

        # Check file for header (Read initial line, and reset read position)
        has_header = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)

        datareader = csv.reader(csvfile)

        # Skip header row
        if has_header:
            next(datareader)

        for user, service in datareader:
            yield (business_unit_for_user(user).strip(),service.strip())


#return {service, {business unit, count}, {business unit, count},...} [LR]
def services_by_business_unit(service_log): #[LR]
    def empty_business_unit_summary():
       return collections.defaultdict(int)

    service_summary = collections.defaultdict(empty_business_unit_summary)
    for business_unit, service in service_log:
        bu_dict = service_summary[service]
        bu_dict[business_unit] += 1

    return service_summary   


def write_report(service_log, output_file): #[CRP]

    service_summary = services_by_business_unit(service_log)

    with open(output_file, 'w') as csvfile:
        datawriter = csv.writer(csvfile)
        #datawriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')

        totals = 0
        totals_by_business_unit = {}
        for unit in sorted_business_units():
            totals_by_business_unit[unit] = 0

        #Header
        datawriter.writerow(['Service'] + list(sorted_business_units()) + ['Subtotals'])

        #Rows
        for service in sorted(service_summary):
            rowdata = [service]
            service_subtotal = 0

            for unit in sorted(service_summary[service].keys()):
                rowdata.append(service_summary[service][unit])
                service_subtotal += service_summary[service][unit]
                totals_by_business_unit[unit] += service_summary[service][unit]

            rowdata.append(service_subtotal)
            totals += service_subtotal

            datawriter.writerow(rowdata)

        #Footer
        rowdata = ['Totals']
        for key in totals_by_business_unit:
            rowdata.append(totals_by_business_unit[key])
        rowdata.append(totals)

        datawriter.writerow(rowdata)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('input')
    parser.add_argument('--output')
    parser.add_argument('--logging')

    args = parser.parse_args()

    write_report(read_input(args.input), args.output)
