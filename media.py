

# Simple class with 4 instance variable
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer