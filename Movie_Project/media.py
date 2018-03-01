class Movie:
    """Class to store movies"""

    
    def __init__(self , movie_title,movie_about,movie_poster,movie_trailor):
        """Constructor method to store data in the objects created in entertainment_center.py"""
        self.title = movie_title                #The movie title is stored in 'self.title' for the object being given values
        self.storyline = movie_about            #The 'self.storyline' stores some information about story of the movie
        self.poster_image_url = movie_poster    #The URL for movie poster image is stored in 'self.poster_image_url' for the object being given values
        self.trailer_youtube_url = movie_trailor#The URL for movie youtube trailer is stored in 'self.trailer_youtube_url' for the object being given values

