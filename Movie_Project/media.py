import webbrowser

class Movie:
    def __init__(self , movie_title,movie_about,movie_poster,movie_trailor):
        self.title = movie_title
        self.storyline = movie_about
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailor
    def show_trailor(self):
        webbrowser.open(self.trailer_youtube_url)
