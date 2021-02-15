from parseCSV import ParseCSV
import operator
from statistics import mean

result_dictionary = {}
EMOJI = '\U0001F600'


class Calculations(ParseCSV):
    def __init__(self, file_name, _args):
        super().__init__(file_name)
        self._args = _args

    def movie_with_year(self, year):
        movie_with_year_data = [(dic['originalTitle'], dic['rating']) for dic in self.movies_information
                                if dic['startYear'] == str(year)]
        return movie_with_year_data

    def movie_with_genre(self, genre):
        movie_with_year_data = [(dic['originalTitle'], dic['rating']) for dic in self.movies_information
                                if genre in dic['genres']]
        return movie_with_year_data

    def movie_with_max_rating(self, year):
        return max(self.movie_with_year(year))

    def movie_with_min_rating(self, year):
        movie_with_year_data = self.movie_with_year(year)
        movie_with_year_data.sort(key=operator.itemgetter(1))
        return movie_with_year_data[0]

    def movie_with_avg_runtime(self, year):
        movie_with_year_data = [(dic['originalTitle'], dic['runtimeMinutes']) for dic in self.movies_information
                                if dic['startYear'] == str(year)]
        return mean([_tuple[1] for _tuple in movie_with_year_data])

    def top_n_highest_rated(self, year):
        movie_with_year_data = [(dic['originalTitle'], dic['numVotes']) for dic in self.movies_information
                                if dic['startYear'] == str(year)]
        movie_with_year_data.sort(key=operator.itemgetter(1))
        return movie_with_year_data[::-1][:10]

    def movie_with_genre_avg_rating(self, genre):
        movies_with_genre_data = self.movie_with_genre(genre)
        return len(movies_with_genre_data), mean([_tuple[1] for _tuple in movies_with_genre_data])

    def store_calculations_results(self):
        if self._args.year is not None:
            year_rating = {}
            result = self.movie_with_max_rating(self._args.year)
            year_rating['Highest Rated Movie'] = result[0]
            year_rating['Highest Rating'] = result[1]
            result = self.movie_with_min_rating(self._args.year)
            year_rating['Lowest Rated Movie'] = result[0]
            year_rating['Lowest Rating'] = result[1]
            result = self.movie_with_avg_runtime(self._args.year)
            year_rating['Average mean minutes'] = "{:.2f}".format(result)
            result_dictionary['-r'] = year_rating
        if self._args.genre is not None:
            genre_rating = {}
            movies_found, result = self.movie_with_genre_avg_rating(self._args.genre)
            genre_rating['Movies Found'] = movies_found
            genre_rating['Average mean Rating'] = "{:.2f}".format(result)
            result_dictionary['-g'] = genre_rating
        if self._args.year_rating is not None:
            top_ratings = {}
            result = self.top_n_highest_rated(self._args.year_rating)
            for index, _tuple in enumerate(result):
                top_ratings[index] = _tuple[0], EMOJI * (int(_tuple[1] / 80)), _tuple[1]
            result_dictionary['-v'] = top_ratings

    def print_calculations_results(self):
        if self._args.year is not None:
            print('--------------------\n')
            result = self.movie_with_max_rating(self._args.year)
            print(f"Highest Rating : {result[1]} - {result[0]}")
            result = self.movie_with_min_rating(self._args.year)
            print(f"Lowest Rating : {result[1]} - {result[0]}")
            result = self.movie_with_avg_runtime(self._args.year)
            print(f"Average mean minutes : " + "{:.2f}".format(result))
        if self._args.genre is not None:
            print('--------------------\n')
            movies_found, result = self.movie_with_genre_avg_rating(self._args.genre)
            print(f"Average mean Rating : " + "{:.2f}".format(result))
        if self._args.year_rating is not None:
            print('--------------------\n')
            result = self.top_n_highest_rated(self._args.year_rating)
            for index, _tuple in enumerate(result):
                print(_tuple[0], ' ', _tuple[1])
