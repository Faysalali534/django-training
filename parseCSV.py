
import csv


class ParseCSV:
    def __init__(self, file_name):
        self.file_reader = ''
        print('Opening {} for reading'.format(file_name))
        self.csv_file = open(file_name, mode='r')
        self.movies_information = []

    def create_file_reader(self):
        self.file_reader = csv.reader(self.csv_file, delimiter=',')

    def store_information(self):
        row_num = 0
        column_names = []
        for row in self.file_reader:
            movie_dict = {}
            if row_num == 0:
                [column_names.append(row[index]) for index in range(len(row))]
                row_num += 1
            else:
                for i in range(len(row)):
                    movie_dict[column_names[i]] = row[i]
                self.movies_information.append(movie_dict)

    def print_information(self):
        for _dict in self.movies_information:
            for key, value in _dict.items():
                print(len(key), ' : ', value)

    def close_file(self):
        self.csv_file.close()
