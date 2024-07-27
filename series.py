class Series:
    def __init__(self, name : str, seasons : int, genres : list):
        self.name = name
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        self.title = name
#constructor
    def rate(self, rating: int):
        self.ratings.append(rating)
#adds the rating to the ratings list
    def __str__(self):
        gnr = ", ".join(self.genres)
        if len(self.ratings) == 0:
            strd = "no ratings"
        else:
            strd = f"{len(self.ratings)} ratings, average {round(sum(self.ratings)/len(self.ratings),1)} points"
        return f"{self.name} ({self.seasons} seasons)\ngenres: {gnr}\n{strd}"
# prints out everything using __str__ 
def minimum_grade(rating: float, series_list: list):
    return [x for x in series_list if sum(x.ratings)/len(x.ratings) >= rating]
# returns a filtered list if the mean of the rating is equal or above the specified rating
def includes_genre(genre: str, series_list: list):
    return list(filter(lambda x :genre in x.genres,series_list))
# returns a filtered list using lambda if the specified genre is in the list of the object's genres


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)