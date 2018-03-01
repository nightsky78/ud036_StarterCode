# Project: Movie Website
# Date Started: 1/1/2018
# Date Completed: pending
# Submitted by: Johannes Hettig

# Description: This file instantiates the class Movie to be used in the
# fresh_tomatoes.py html generator. The main source for the structure of
# the file was obtained from Udacity FDND Course

import media
import fresh_tomatoes


# List of Movies
# It actually better to get this from a database

# Instantiating class movie for movie "Star Trek XI"
StarTrekXI = media.Movie('Star Trek XI',
                         'Bad guy comes from the future and changes the past',
                         'https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg',
                         'https://www.youtube.com/watch?v=3PM1pvOzn_w')

# Instantiating class movie for movie "Star Trek XII"
StarTrekXII = media.Movie('Star Trek XII',
                          'Strong guys wants to get his family back - and rule \
                           the world',
                          'https://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg',
                          'https://www.youtube.com/watch?v=r5gdbUC9mWU')

# Instantiating class movie for movie "Star Trek XIII"
StarTrekXIII = media.Movie('Star Trek XIII',
                           'Stranded on a lost planet fighting the way back out',
                           'https://upload.wikimedia.org/wikipedia/en/b/ba/Star_Trek_Beyond_poster.jpg',
                           'https://www.youtube.com/watch?v=fLVPfbs19kc')

# Create array with the instances as values
movies = [StarTrekXI, StarTrekXII, StarTrekXIII]

# call fresh_tomato html generator
# Actually stroryline is not used. If I have time I add it later.;-)
fresh_tomatoes.open_movies_page(movies)
