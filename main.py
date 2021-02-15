import os
import timeit
import json
import argparse
from calculations import *


def argument_parser():
    """
        Argparse makes Validation easy if we enter argument of type other than we
        we have already defined it will throw error
    """
    parser = argparse.ArgumentParser(description='Fetch movies information')
    parser.add_argument('-r', '--year', type=int, help='Movie start Year')
    parser.add_argument('-g', '--genre', type=str, help='Movie Genre')
    parser.add_argument('-v', '--year_rating', type=int, help='High rated movie of year')
    return parser.parse_args()


if __name__ == '__main__':
    start = timeit.timeit()
    args = argument_parser()
    csv_reading = Calculations(os.environ['CSV_FILE'], args)
    csv_reading.create_file_reader()
    csv_reading.store_information()
    csv_reading.store_calculations_results()
    print(json.dumps(result_dictionary, indent=4, ensure_ascii=False))
    csv_reading.close_file()
    end = timeit.timeit()
    print(start - end)
