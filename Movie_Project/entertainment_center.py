import media
import fresh_tomatoes

#importing python modules to organise code logically

    # This is where new objects of the class Movie are created and are given respective values.

    #fast_and_furious: movie title, movie storyline, Poster Image path, Youtube Trailer URL
fast_and_furious = media.Movie("Fast and Furious",
                               "The story of a family of friends who are best at driving cars",
                               r"img\ff.jpg",
                               "https://www.youtube.com/watch?v=N0ITWaDAcME")

    #harry_potter: movie title, movie storyline, Poster Image path, Youtube Trailer URL
harry_potter = media.Movie("Harry Potter",
                           "The story of a boy who survived and then studied magic in the Hogwarts",
                           r"img\hp.jpg",
                           "https://www.youtube.com/watch?v=K1KPcXRMMo4")

    #lakshya: movie title, movie storyline, Poster Image path, Youtube Trailer URL
lakshya = media.Movie("Lakshya",
                      "This is a story about the Indian soldiers",
                      r"img\l.jpg",
                      "https://www.youtube.com/watch?v=XVu5126oPqU")   

    #border: movie title, movie storyline, Poster Image path, Youtube Trailer URL
border = media.Movie("Border",
                     "This movie is based on a true story of a Indo-Pak war.",
                     r"img\b.jpg",
                     "https://www.youtube.com/watch?v=aJ-sxaxkoD4")

    #sarkar_3: movie title, movie storyline, Poster Image path, Youtube Trailer URL
sarkar_3 = media.Movie("Sarkar 3",
                     "Real power does not come out of fear , it comes out of respect",
                     r"img\s.jpg",
                     "https://www.youtube.com/watch?v=B27zvZRfeSo")

    #iron_man: movie title, movie storyline, Poster Image path, Youtube Trailer URL
iron_man = media.Movie("Sarkar 3",
                       "The story of a super genius who made some suits full of weapons",
                       r"img\im.jpg",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

#creating an array of movies
movies = [fast_and_furious , harry_potter , lakshya , border , sarkar_3 , iron_man]
fresh_tomatoes.open_movies_page(movies)
