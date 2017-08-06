import webbrowser


class Movie():
    """
    This class stores movie related information and can play the trailer
    in a browser popup
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        Initializes the movie objet wih the following parameters
        movie_title: The title of the movie
        movie_storyline: A short description of what the movie is about
        poster_image: The URL to the movie poster image
        trailer_youtube: The URL to the trailer on youtube
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        This function displays the movie trailer in a browser popup.
        """
        webbrowser.open(self.trailer_youtube_url)
