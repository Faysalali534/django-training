from parseCSV import ParseCSV

result_dictionary = {}
EMOJI = '\U0001F600'


class Calculations(ParseCSV):
    def __init__(self, file_name, _args):
        super().__init__(file_name)
        self._args = _args

    def get_information_for_year(self):
        if self._args.year is not None:
            return self._df.loc[self._df['startYear'] == self._args.year]
        else:
            return None

    def get_information_for_genre(self):
        if self._args.genre is not None:
            return self._df.loc[self._df['genres'].str.contains('Comedy')]
        else:
            return None

    def information_for_top_n_ratings(self):
        if self._args.year_rating is not None:
            return self._df.loc[self._df['startYear'] == self._args.year_rating]
        else:
            return None

    def calculate_first_argument_records(self):
        data_frame = self.get_information_for_year()
        if data_frame is not None:
            year_rating = {}
            result = data_frame.loc[data_frame['rating'].idxmax()]
            year_rating['Highest Rated Movie'] = result['originalTitle']
            year_rating['Highest Rating'] = result['rating']
            result = data_frame.loc[data_frame['rating'].idxmin()]
            year_rating['Lowest Rated Movie'] = result['originalTitle']
            year_rating['Lowest Rating'] = result['rating']
            result = data_frame['runtimeMinutes'].mean()
            year_rating['Average mean minutes'] = "{:.2f}".format(result)
            result_dictionary['-r'] = year_rating

    def calculate_second_argument_records(self):
        data_frame = self.get_information_for_genre()
        if data_frame is not None:
            genre_rating = {'Movies Found': len(data_frame),
                            'Average mean Rating': "{:.2f}".format(data_frame['rating'].mean())}
            result_dictionary['-g'] = genre_rating

    def calculate_third_argument_records(self):
        data_frame = self.information_for_top_n_ratings()
        if data_frame is not None:
            top_ratings = {}
            data_frame = data_frame.nlargest(10, ['numVotes'])
            result = data_frame.head(10)
            index = 1
            for name, rating, votes in zip(result['originalTitle'], result['rating'], result['numVotes']):
                top_ratings[index] = name, EMOJI * (int(votes / 80)), rating
                index += 1
            result_dictionary['-v'] = top_ratings
