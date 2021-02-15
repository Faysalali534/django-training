import csv
from movie_store import MovieStore


class ParseCSV:
    def __init__(self, file_name):
        self.file_reader = ''
        print('Opening {} for reading'.format(file_name))
        self.csv_file = open(file_name, mode='r')
        self.movies_information = []

    def create_file_reader(self):
        self.file_reader = csv.reader(self.csv_file, delimiter=',')

    def store_information(self):
        index = 0
        for csv_row in self.file_reader:
            if index == 0:
                index += 1
            else:
                self.movies_information.append(
                    MovieStore(csv_row[0], csv_row[1], csv_row[2], csv_row[3], csv_row[4],
                               csv_row[5], csv_row[6], csv_row[7]))

    def close_file(self):
        self.csv_file.close()

    def display(self):
        print(len(self.movies_information))
        for _object in self.movies_information:
            _object.print_information()
