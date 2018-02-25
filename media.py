##########################################
# Project: Movie Website
# Date Started: 1/1/2018
# Date Completed: pending
# Submitted by: Johannes Hettig
##########################################

######################################## Media File ####################################################
# Description: This file creates the class Movie to allow for instances of this class to be used in the
#              entertainment.py file. This definition of the class Movie was obtained through the course
########################################################################################################


class Movie():
    """
    The class Movie lets other functions use four class variables:

    At this point no further fuctions are implemented in this class.

    Args:
        movie_title: The title of the movie.
        movie_storyline: The storyline of the movie.
        poster_image: The URL to the image of the movie.
        movie_trailer: The URL to the trailer video of the movie.

    Returns:
        no returns

    Raises:
        no execptions
    """
    def __init__(self, movie_title, movie_storyline, poster_image, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer