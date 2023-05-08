class Manga():

    def __init__(self, id, title, released, author, sinopsis, review, likes , score, points, categories) -> None:
        self.id = id
        self.title = title
        self.released = released
        self.author = author
        self.sinopsis = sinopsis 
        self.review = review 
        self.likes = likes 
        self.score = score
        self.points = points
        self.categories = categories

    def to_JSON(self):
        return {
            "id":self.id,
            "title": self.title,
            "released": self.released,
            "author": self.author,
            "sinopsis": self.sinopsis,
            "review": self.review,
            "likes": self.likes,
            "score": self.score,
            "points": self.points,
            "categories": self.categories
        }
    
    