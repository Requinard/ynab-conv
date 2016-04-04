import argparse
import csv
import sys

import ing
import knab

"""
Example format: Date,Payee,Category,Memo,Outflow,Inflow
"""


def get_arg_parser():
    parser = argparse.ArgumentParser(description="Translate bank statements into YNAB statements")
    parser.add_argument("-v", "--verbose", help="Show verbose text messages", action="store_true")
    parser.add_argument("-o", "--output", help="File to write to", default="ynab.csv")
    parser.add_argument("bank", type=str, help="Bank format to use")
    parser.add_argument("input", type=str, help="Input file")

    return parser


def write_output(output_file, output_array):
    # Write header

    output_file.write("Date,Payee,Category,Memo,Outflow,Inflow\r")

    for row in output_array:
        output_file.write(",".join(row))
        output_file.write("\r")


def open_file(input_file, input_file_string, delimiter=","):
    try:
        input_file = csv.reader(open(input_file_string, "r"), delimiter=delimiter, quotechar="|")
    except Exception as e:
        print("Could not open input file" + str(e))
        return 3

    return input_file


def main(*args, **kwargs):
    # Parse args
    parser = get_arg_parser()
    parsed = parser.parse_args()

    verbose = parsed.verbose

    input_file_string = parsed.input
    output_file_string = parsed.output
    bank = parsed.bank.lower()

    if input_file_string == "" or bank == "":
        return 2

    if (verbose):
        print(
            "Verbose: {0}\rInput file: {1}\rOutput file: {2}\rBank: {3}".format(verbose, input_file_string,
                                                                                output_file_string, bank))

    # Prepare variables

    print("Preparing variables")

    input_file = {}
    output_file = {}
    output_array = []

    # Open files

    print("Opening files")

    try:
        output_file = open(output_file_string, "w")
    except Exception as e:
        print("Could not open output file")
        print(e)
        return 4

    # Transform inputs

    print("Starting transformations")

    if bank == "ing":
        input_file = open_file(input_file, input_file_string, ",")

        print("Transforming from ING")

        ing.transform(input_file, output_array)
    elif bank == "knab":
        input_file = open_file(input_file, input_file_string, ";")

        print("Transforming from Knab")

        knab.transform(input_file, output_array)

    if verbose:
        print(output_array)

    if len(output_array) > 0:
        print("Writing output")
        write_output(output_file, output_array)

    output_file.close()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
