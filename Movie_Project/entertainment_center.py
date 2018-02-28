import media , fresh_tomatoes

fast_and_furious = media.Movie("Fast and Furious",
                               "The story of a family of friends who are best at driving cars",
                               r"C:\Users\Hp\Desktop\repos\Full_Stack_Web_Developer_1_Nanodegree\Movie_Project\img\ff.jpg",
                               "https://www.youtube.com/watch?v=N0ITWaDAcME")
harry_potter = media.Movie("Harry Potter",
                           "The story of a boy who survived and then studied magic in the Hogwarts",
                           r"C:\Users\Hp\Desktop\repos\Full_Stack_Web_Developer_1_Nanodegree\Movie_Project\img\hp.jpg",
                           "https://www.youtube.com/watch?v=K1KPcXRMMo4")
lakshya = media.Movie("Lakshya",
                      "This is a story about the Indian soldiers",
                      r"C:\Users\Hp\Desktop\repos\Full_Stack_Web_Developer_1_Nanodegree\Movie_Project\img\l.jpg",
                      "https://www.youtube.com/watch?v=XVu5126oPqU")   
border = media.Movie("Border",
                     "This movie is based on a true story of a Indo-Pak war.",
                     r"C:\Users\Hp\Desktop\repos\Full_Stack_Web_Developer_1_Nanodegree\Movie_Project\img\b.jpg",
                     "https://www.youtube.com/watch?v=aJ-sxaxkoD4")
sarkar_3 = media.Movie("Sarkar 3",
                     "Real power does not come out of fear , it comes out of respect",
                     r"C:\Users\Hp\Desktop\repos\Full_Stack_Web_Developer_1_Nanodegree\Movie_Project\img\s.jpg",
                     "https://www.youtube.com/watch?v=B27zvZRfeSo")
iron_man = media.Movie("Sarkar 3",
                       "The story of a super genius who made some suits full of weapons",
                       r"C:\Users\Hp\Desktop\repos\Full_Stack_Web_Developer_1_Nanodegree\Movie_Project\img\im.jpg",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

movies = {fast_and_furious , harry_potter , lakshya , border , sarkar_3 , iron_man}
fresh_tomatoes.open_movies_page(movies)
