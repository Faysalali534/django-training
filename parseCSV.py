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
        next(self.file_reader)
        for csv_row in self.file_reader:
            self.movies_information.append(
                MovieStore(*csv_row))

    def close_file(self):
        self.csv_file.close()

    def display(self):
        for movie_record in self.movies_information:
            movie_record.print_information()
