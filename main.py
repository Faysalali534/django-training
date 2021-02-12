import os
import timeit
import json
import argparse

from calculations import *

os.environ['csv_filename'] = '/Users/alsyketechnologies/PycharmProjects/pythonProject/Movies dataset - title.basics.csv'


if __name__ == '__main__':
    start = timeit.timeit()
    parser = argparse.ArgumentParser(description='Fetch movies information')
    parser.add_argument('-r', '--year', type=int, help='Movie start Year')
    parser.add_argument('-g', '--genre', type=str, help='Movie Genre')
    parser.add_argument('-v', '--year_rating', type=int, help='High rated movie of year')
    args = parser.parse_args()
    csv_reading = Calculations(os.environ.get('csv_filename'), args)
    csv_reading.create_file_reader()
    csv_reading.set_correct_data_types()
    csv_reading.calculate_first_argument_records()
    csv_reading.calculate_second_argument_records()
    csv_reading.calculate_third_argument_records()
    print(json.dumps(result_dictionary, indent=4, ensure_ascii=False))
    csv_reading.close_file()
    end = timeit.timeit()
    print(start - end)

