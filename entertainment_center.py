import media
import fresh_tomatoes


def create_movies():
    # Creates the list of movies that will be displayed
    toy_story = media.Movie("Toy Story",
                            "A story of a boy and toys that come to life.",
                            "http://upload.wikimedia.org/wikipedia/en"
                            "/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

    avatar = media.Movie("Avatar the last airbender",
                         "An action fantasy adventure film.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/"
                         "8/8e/The_Last_Airbender_Poster.png/"
                         "220px-The_Last_Airbender_Poster.png",
                         "https://www.youtube.com/watch?v=Wo85qZm-Zuk")

    kubo = media.Movie("Kubo and the two strings",
                       "Young Kubo's peaceful existence comes crashing down.",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/"
                       "Kubo_and_the_Two_Strings_poster.png/220px-Kubo_and_the"
                       "_Two_Strings_poster.png",
                       "https://www.youtube.com/watch?v=p4-6qJzeb3A")

    moana = media.Movie("Moana",
                        "An adventurous teenager sails out on a daring mission"
                        " to save her people.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb"
                        "/2/26/Moana_Teaser_Poster.jpg/220px-Moana_Teaser"
                        "_Poster.jpg",
                        "https://www.youtube.com/watch?v=LKFuXETZUsI")

    trolls = media.Movie("Trolls",
                         "Life in a troll village",
                         "https://upload.wikimedia.org/wikipedia/en/a/ad/"
                         "Trolls_%28film%29_logo.png",
                         "https://www.youtube.com/watch?v=xyjm5VQ11TQ")

    frozen = media.Movie("Frozen",
                         "When their kingdom becomes trapped in perpetual "
                         "winter, fearless Anna joins forces with mountaineer"
                         "Kristoff and his reindeer sidekick to find "
                         "Anna's sister",
                         "https://upload.wikimedia.org/wikipedia"
                         "/en/thumb/0/05/"
                         "Frozen_%282013_film%29_poster.jpg/"
                         "220px-Frozen_%282013_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=twhMKM5B9Ws")

    # Arrange list of movie objects
    movies = [toy_story, avatar, kubo, moana, trolls, frozen]
    return movies

# Get the list of movies
movies = create_movies()

# Call to open movies in a browser
fresh_tomatoes.open_movies_page(movies)
