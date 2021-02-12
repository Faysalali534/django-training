import pandas as pd


class ParseCSV:
    def __init__(self, file_name):
        self._df = pd.DataFrame()
        print('Opening {} for reading'.format(file_name))
        self.csv_file = open(file_name, mode='r')
        self.movies_information = []

    def create_file_reader(self):
        self._df = pd.read_csv(self.csv_file)

    def replace_null_values(self):
        self._df = self._df.replace(r'\\N', 0, regex=True)
        self._df['genres'] = self._df['genres'].replace(0, ' ')

    def set_correct_data_types(self):
        self.replace_null_values()
        self._df["runtimeMinutes"] = pd.to_numeric(self._df['runtimeMinutes'])

    def close_file(self):
        self.csv_file.close()
