class MovieStore:
    def __init__(self, _id, title_type, original_title, start_year, runtime_minutes, genres, rating, num_votes):
        self.id = _id
        self.titleType = title_type
        self.originalTitle = original_title
        self.startYear = start_year
        if runtime_minutes == '\\N':
            self.runtimeMinutes = 0
        else:
            self.runtimeMinutes = int(runtime_minutes)
        self.genres = genres
        if rating == '\\N':
            self.rating = 0
        else:
            self.rating = float(rating)
        self.numVotes = int(num_votes)

    def __getitem__(self, item):
        return getattr(self, item)

    def print_information(self):
        print(self.id, ' ', self.titleType, ' ', type(self.numVotes))
