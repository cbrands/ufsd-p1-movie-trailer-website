import fresh_tomatoes
import media


# Define the six movies
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")

dunkirk = media.Movie(
    "Dunkirk",
    "A movie about the battle of Dunkirk",
    "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/dunkirk-poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=F-eMt3SrfFU")

jobs = media.Movie(
    "Steve Jobs",
    "A movie about Steve Jobs",
    "https://image.tmdb.org/t/p/original/7j3xCcZZUDTPuOt6KIVDy7xsMyq.jpg",
    "https://www.youtube.com/watch?v=IeOxo7o9T8Q")

spiderman = media.Movie(
    "Spiderman",
    "A movie about spiderman",
    "http://www.superheromovies.net/img/p/6v0OGYaB8510nH0zcKH0ZWP8HWD.jpg",
    "https://www.youtube.com/watch?v=xEvV3OsE2WM")

justice_league = media.Movie(
    "Justice League",
    "No idea but the trailer was cool",
    "http://orig04.deviantart.net/7518/f/2016/207/c/2/justice_league_movie____2017__poster_by_mrdeks-dabh40c.jpg",  # noqa
    "https://www.youtube.com/watch?v=3cxixDgHUYw")

blade_runner = media.Movie(
    "Blade runner",
    "A remake of blade runner",
    "https://s-media-cache-ak0.pinimg.com/originals/a8/e9/0a/a8e90a844bed9e6951de16f5f6cde1e0.jpg",  # noqa
    "https://www.youtube.com/watch?v=gCcx85zbxz4")

# Put the movies in an list and generate the website with fresh_tomatoes
movies = [toy_story, dunkirk, jobs, spiderman, justice_league, blade_runner]
fresh_tomatoes.open_movies_page(movies)
