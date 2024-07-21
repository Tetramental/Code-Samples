# File Name: media.py
# Purpose: To implement a class hierarchy
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: February 8, 2019

# Media class
class Media:
    '''Defines the base class for a variety of media including movies, songs, pictures, and other custom types of media.
    Has the ability to:
    1) Clamp rating value between and including 0 and 10
    2) Initilize three attributes of a Media object: the name, the rating, the type of media
    3) Return the media type
    4) Return the name of the media
    5) Return and set the rating of the media
    6) Overload the string method of any Media object'''
    
    # clamping values
    def clampRating(rating):
        if rating < 0:
            rating = 0
        elif rating > 10:
            rating = 10
        else:
            pass
        return rating
    
    # initialization method
    def __init__(self, __name = "", __rating = 0, __typeMedia = ""):
        self.__typeMedia = __typeMedia
        self.__name = __name
        self.__rating = Media.clampRating(__rating)
    
    # getters
    def getMediaType(self):
        return self.__typeMedia
    
    def getName(self):
        return self.__name
    
    def getRating(self):
        return self.__rating
    
    # setters
    def setRating(self, ratingNew):
        self.__rating = Media.clampRating(ratingNew)
        return self.__rating
    
    # overloaded string method
    def __str__(self):
        return "Media Type: " + self.__typeMedia + "\nName: " + self.__name + "\nRating: " + str(self.__rating) + "/10\n"

# Movie subclass
class Movie(Media):
    '''Defines the Movie class, a subclass of the Media class.
    Has the ability to:
    1) Inherit methods from its superclass, "Media"
    2) Play a movie by printing a message
    3) Return the movie director's name
    4) Return the running time of a movie
    5) Override the string method of any Media object'''
    
    # initalization method
    def __init__(self, __name = "", __rating = 0, __director = "", __timeElapsed = 0, __typeMedia = "Movie"):
        super().__init__(__name, __rating, __typeMedia)
        self.__director = __director
        if __timeElapsed < 0:
            self.__timeElapsed = 0
        else:
            self.__timeElapsed = __timeElapsed
    
    # simulate "playing a movie"
    def play(self):
        print("\n\"" + super().getName() + "\", playing now.")
    
    # getters
    def getDirector(self):
        return self.__director
    
    def getTimeElapsed(self):
        return self.__timeElapsed
    
    # overridden string method
    def __str__(self):
        return "Media Type: " + super().getMediaType() + "\nName: " + super().getName() + "\nRating: " + str(super().getRating()) + "/10\nDirector: " + self.__director + "\nRunning Time: " + str(self.__timeElapsed) + " minutes\n"

# Song subclass
class Song(Media):
    '''Defines the Song class, a subclass of the Media class.
    Has the ability to:
    1) Inherit methods from its superclass, "Media"
    2) Play a song with its artist by printing a message
    3) Return the artist's name
    4) Return the album name to which the song belongs on
    5) Override the string method of any Media object'''
    
    # initialization method
    def __init__(self, __name = "", __rating = 0, __artist = "", __album = "Single", __typeMedia = "Song"):
        super().__init__(__name, __rating, __typeMedia)
        self.__artist = __artist
        self.__album = __album
    
    # simulate "playing a song"
    def play(self):
        print("\n\"" + super().getName() + "\" by [" + self.__artist + "], playing now.")
    
    # getters
    def getArtist(self):
        return self.__artist
    
    def getAlbum(self):
        return self.__album
    
    # overridden string method
    def __str__(self):
        return "Media Type: " + super().getMediaType() + "\nName: " + super().getName() + "\nRating: " + str(super().getRating()) + "/10\nArtist: " + self.__artist + "\nAlbum: " + self.__album + "\n"

# Picture subclass
class Picture(Media):
    '''Defines the Picture class, a subclass of the Media class.
    Has the ability to:
    1) Inherit methods from its superclass, "Media"
    2) Show a picture by printing a message
    3) Return and set the resolution (in dots per inch) of the picture; minimum 200
    4) Override the string method of any Media object'''
    
    # initialization method
    def __init__(self, __name = "", __rating = 0, __resolution = 200, __typeMedia = "Picture"):
        if __name[-4:] == ".jpg" or __name[-4:] == ".png" or __name[-4:] == ".gif" or __name[-4:] == ".bmp" or __name[-4:] == ".tif" or __name[-4:] == ".exr":
            pass
        else:
            __name += ".jpg"
        super().__init__(__name, __rating, __typeMedia)
        if __resolution < 200:
            self.__resolution = 200
        else:
            self.__resolution = __resolution
    
    # simulate "showing a picture"
    def show(self):
        print("\nShowing \"" + super().getName() + "\"")
    
    # getters
    def getResolution(self):
        return self.__resolution
    
    # setters
    def setResolution(self, resNew):
        if resNew >= 200:
            self.__resolution = resNew
        else:
            self.__resolution = 200
        return self.__resolution
    
    # overriden string method
    def __str__(self):
        return "Media Type: " + super().getMediaType() + "\nName: " + super().getName() + "\nRating: " + str(super().getRating()) + "/10\nResolution: " + str(self.__resolution) + " DPI\n"
    
# main program
if __name__ == "__main__":
    title = "Media Tests"
    print(title)
    print("-" * len(title) + "\n")
    
    mediaTest = Media("Fortnite", 6, "Game")
    movieTest = Movie("Kill Bill", 8, "Quentin Tarentino", 111)
    songTest = Song("In the End", 10, "Linkin Park", "Hybrid Theory")
    pictureTest = Picture("Birb.png", 1000, 144)
    
    print("=" * 10 + "TESTING MEDIA" + "=" * 10)
    print(mediaTest)
    print("=" * 10 + "TESTING MOVIE" + "=" * 10)
    print(movieTest)
    print("=" * 10 + "TESTING SONG" + "=" * 10)
    print(songTest)
    print("=" * 10 + "TESTING PICTURE" + "=" * 10)
    print(pictureTest)