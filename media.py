class Movie(object):
    """ A movie with the following properties.

        Attributes:
        title: A string representing movie name
        storyline: A string providing a short introduction to movie
        poster_image_url: A string with a link to a official movie poster
        trailer_youtube_url: A string with a link to a official movie trailer
                            on youtube
    """

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        """ Return a movie object whose title is *movie_title* """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
