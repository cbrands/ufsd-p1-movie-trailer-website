import fresh_tomatoes
import media


# Define the six movies
movie_1_poster = "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
movie_1_trailer = "https://www.youtube.com/watch?v=vwyZH85NQC4"
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    movie_1_poster,
    movie_1_trailer)

movie_2_poster = "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/dunkirk-poster.jpg"
movie_2_trailer = "https://www.youtube.com/watch?v=F-eMt3SrfFU"
dunkirk = media.Movie(
    "Dunkirk",
    "A movie about the battle of Dunkirk",
    movie_2_poster,
    movie_2_trailer)

movie_3_poster = "https://image.tmdb.org/t/p/original/7j3xCcZZUDTPuOt6KIVDy7xsMyq.jpg"
movie_3_trailer = "https://www.youtube.com/watch?v=IeOxo7o9T8Q"
jobs = media.Movie(
    "Steve Jobs",
    "A movie about Steve Jobs",
    movie_3_poster,
    movie_3_trailer)

movie_4_poster = "http://www.superheromovies.net/img/p/6v0OGYaB8510nH0zcKH0ZWP8HWD.jpg"
movie_4_trailer = "https://www.youtube.com/watch?v=xEvV3OsE2WM"
spiderman = media.Movie(
    "Spiderman",
    "A movie about spiderman",
    movie_4_poster,
    movie_4_trailer)

movie_5_poster = "http://orig04.deviantart.net/7518/f/2016/207/c/2/justice_league_movie____2017__poster_by_mrdeks-dabh40c.jpg"
movie_5_trailer = "https://www.youtube.com/watch?v=3cxixDgHUYw"
justice_league = media.Movie(
    "Justice League",
    "No idea but the trailer was cool",
    movie_5_poster,
    movie_5_trailer)

movie_6_poster = "https://s-media-cache-ak0.pinimg.com/originals/a8/e9/0a/a8e90a844bed9e6951de16f5f6cde1e0.jpg"
movie_6_trailer = "https://www.youtube.com/watch?v=gCcx85zbxz4"
blade_runner = media.Movie(
    "Blade runner",
    "A remake of blade runner",
    movie_6_poster,
    movie_6_trailer)

# Put the movies in an array and generate the website with fresh_tomatoes
movies = [toy_story, dunkirk, jobs, spiderman, justice_league, blade_runner]
fresh_tomatoes.open_movies_page(movies)
