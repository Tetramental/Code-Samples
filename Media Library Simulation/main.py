import sys
import menuGUIs
from media import Movie, Song, Picture

# File Name: main.py
# Purpose: To simulate a media library
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: February 8, 2019

def validateInteger(userInput):
    '''Attempts to cast a string representation of a number to an integer to validate user choice.
    User must input a number.'''
    validateInputLoop = True
    while validateInputLoop:
        try:
            inputInteger = int(userInput)
            validateInputLoop = False
        except ValueError as v:
            print("Please input a number!")
            userInput = input()
    return inputInteger

def createListOfMedia(*args):
    'Creates and returns a list of media based on an arbitrary number of given objects of classes and subclasses of Media.'
    listMedia = []
    for objectMedia in args:
        listMedia.append(objectMedia)
    return listMedia

def displayMedia(listMedia):
    'Prints out each individual type of media object in the list of media passed.'
    print("=" * 10 + " DISPLAYING ALL MEDIA " + "=" * 10)
    for m in listMedia:
        print(m)

def displayAllMovies(listMedia):
    'Prints out all Movie objects in the list of media passed.'
    print("=" * 10 + " DISPLAYING ALL MOVIES " + "=" * 10)
    for m in listMedia:
        if type(m) is Movie:
            print(m)

def displayAllSongs(listMedia):
    'Prints out all Song objects in the list of media passed.'
    print("=" * 10 + " DISPLAYING ALL SONGS " + "=" * 10)
    for m in listMedia:
        if type(m) is Song:
            print(m)

def displayAllPictures(listMedia):
    'Prints out all Picture objects in the list of media passed.'
    print("=" * 10 + " DISPLAYING ALL PICTURES " + "=" * 10)
    for m in listMedia:
        if type(m) is Picture:
            print(m)

def playMovie(nameMovie, listMedia):
    'Plays a movie if it exists in the media library.'
    i = 0
    for m in listMedia:
        if m.getName().lower() == nameMovie.lower() and type(m) is Movie:
            m.play()
            return True
        i += 1
    if i == len(listMedia):
        print("\nSorry, that movie is not in the media library!")
        return False

def playSong(nameSong, listMedia):
    'Plays a song if it exists in the media library.'
    i = 0
    for m in listMedia:
        if m.getName().lower() == nameSong.lower() and type(m) is Song:
            m.play()
            return True
        i += 1
    if i == len(listMedia):
        print("\nSorry, that song is not in the media library!")
        return False

def displayPicture(namePicture, listMedia):
    'Displays a picture if it exists in the media library.'
    i = 0
    for m in listMedia:
        if m.getName().lower() == namePicture.lower() and type(m) is Picture:
            m.show()
            return True
        i += 1
    if i == len(listMedia):
        print("\nSorry, that picture is not in the media library!")
        return False

def quitProgram():
    '''Asks the user to confirm their quit selection.
    Also listens for valid input'''
    
    print("=" * 30)
    print(("=" * 5) + (" " * 3) + "ARE YOU SURE?" + (" " * 4) + ("=" * 5))
    print(("=" * 5) + (" " * 7) + "Y / N" + (" " * 8) + ("=" * 5))
    print("=" * 30)
    userInput = input()
    
    loopTemp = True
    while loopTemp:
        if userInput.strip().lower() == "y" or userInput.strip().lower() == "n":
            if userInput.strip().lower() == "y":
                sys.exit(0)
            else:
                break
        else:
            userInput = input("Please input a valid answer (Y/N): ")

# main program
if __name__ == "__main__":
    '''Main Program:
    Movies, songs, pictures, and custom types of media may be added and changed here.
    Menu Loop is described here.'''
    
    # declaring and assigning variables/objects
    movie1 = Movie("Kill Bill", 8, "Quentin Tarentino", 111)
    movie2 = Movie("The Penguins of Madagascar", 10, "Eric Darnell & Simon J. Smith", 92)
    movie3 = Movie("Spiderman: Homecoming", 8, "Jon Watts", 133)
    movie4 = Movie("Pokemon: The First Movie", 10, "Kunijiko Yuyama", 75)
    movie5 = Movie("Kung Fu Hustle", 10, "Stephen Chow", 98)
    movie6 = Movie("Coco", 8, "Lee Unkrich", 105)
    movie7 = Movie("Happy Feet", 10, "George Miller", 108)
    movie8 = Movie("Battle Royale", 9, "Kinji Fukasaku", 113)
    movie9 = Movie("The Matrix", 7, "The Wachowski Brothers", 136)
    movie10 = Movie("Scott Pilgrim vs. the World", 10, "Edgar Wright", 112)
    song1 = Song("In the End", 10, "Linkin Park", "Hybrid Theory")
    song2 = Song("Chandelier", 9, "Sia", "1000 Forms of Fear")
    song3 = Song("Love Shack", 8, "B-52's", "Cosmic Thing")
    song4 = Song("Never Gonna Give You Up", 10, "Rick Astley", "Whenever You Need Somebody")
    song5 = Song("World is Mine", 10, "Supercell")
    song6 = Song("NO SCARED", 10, "ONE OK ROCK", "Zankyo Reference")
    song7 = Song("Bubblegum Bitch", 8, "Marina and the Diamonds", "Electra Heart")
    song8 = Song("you should see me in a crown", 9,  "Billie Eilish")
    song9 = Song("Radioactive", 10, "Imagine Dragons", "Night Visions")
    song10 = Song("Rush Over Me", 10, "Seven Lions, ILLENIUM, Said the Sky ft. HALIENE")
    picture1 = Picture("birb.png", 1000, 144)
    picture2 = Picture("loaf", 10, 288)
    picture3 = Picture("penggi.gif", 2000, 1080)
    picture4 = Picture("puni.tif", 5500, 2160)
    picture5 = Picture("dimsum.exr", 8, 844)
    picture6 = Picture("simuliu", 40000, 671)
    picture7 = Picture("sanfran.tif", 9, 42)
    picture8 = Picture("laptop.gif", 6, 99)
    picture9 = Picture("Threshold.png", 4, 72)
    picture10 = Picture("freshbowlofrice.exr", 7, 300)
    listOfMedia = createListOfMedia(movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, song1, song2, song3, song4, song5, song6, song7, song8, song9, song10, picture1, picture2, picture3, picture4, picture5, picture6, picture7, picture8, picture9, picture10)
    
    # menu loop
    menuTrue = True
    while menuTrue:
        menuGUIs.menuMain()
        user_input = input()
        user_input = validateInteger(user_input)    # validate user_input as a number
        
        if 1 <= user_input <= 5:
            
            # Display All Media
            if user_input == 1:
                displayMedia(listOfMedia)    # show all media in list
                user_input = input("Press [ENTER] to go back.")
            
            # Display All Movies
            elif user_input == 2:
                displayAllMovies(listOfMedia)    # show all movies in list
                menuGUIs.menuMovie()     # show movies menu
                user_input = input()
                user_input = validateInteger(user_input)    # validate user_input as a number
                
                validateInputLoop1 = True
                while validateInputLoop1:
                    if user_input == 1 or user_input == 2:
                        
                        # Play movie
                        if user_input == 1:
                            nameMovie = input("Please enter the name of the movie: ")
                            movieStateLoop = True
                            while movieStateLoop:
                                movieState = playMovie(nameMovie, listOfMedia)
                                if movieState == True:
                                    user_input = input("Press [ENTER] to go back.")
                                    movieStateLoop = False
                                    validateInputLoop1 = False
                                else:
                                    nameMovie = input("Please choose another movie: ")
                        
                        # Return to main menu
                        else:
                            validateInputLoop1 = False
                    else:
                        print("Please choose one of the options available.")
                        user_input = input()
                        user_input = validateInteger(user_input)    # validate user_input as a number
                        continue
            
            # Display All Songs
            elif user_input == 3:
                displayAllSongs(listOfMedia)
                menuGUIs.menuSong()    # show songs menu
                user_input = input()
                user_input = validateInteger(user_input)    # validate user_input as a number
                
                validateInputLoop2 = True
                while validateInputLoop2:
                    if user_input == 1 or user_input == 2:
                        
                        # Play song
                        if user_input == 1:
                            nameSong = input("Please enter the name of the song: ")
                            songStateLoop = True
                            while songStateLoop:
                                songState = playSong(nameSong, listOfMedia)
                                if songState == True:
                                    user_input = input("Press [ENTER] to go back.")
                                    songStateLoop = False
                                    validateInputLoop2 = False
                                else:
                                    nameSong = input("Please choose another song: ")
                        
                        # Return to main menu
                        else:
                            validateInputLoop2 = False
                    else:
                        print("Please choose one of the options available.")
                        user_input = input()
                        user_input = validateInteger(user_input)    # validate user_input as a number
                        continue
            
            # Display All Pictures
            elif user_input == 4:
                displayAllPictures(listOfMedia)
                menuGUIs.menuPicture()
                user_input = input()
                user_input = validateInteger(user_input)    # validate user_input as a number
                
                validateInputLoop3 = True
                while validateInputLoop3:
                    if user_input == 1 or user_input == 2:
                        
                        # Show picture
                        if user_input == 1:
                            namePicture = input("Please enter the name of the picture: ")
                            pictureStateLoop = True
                            while pictureStateLoop:
                                pictureState = displayPicture(namePicture, listOfMedia)
                                if pictureState == True:
                                    user_input = input("Press [ENTER] to go back.")
                                    pictureStateLoop = False
                                    validateInputLoop3 = False
                                else:
                                    namePicture = input("Please choose another picture: ")
                        
                        # Return to main menu
                        else:
                            validateInputLoop3 = False
                    else:
                        print("Please choose one of the options available.")
                        user_input = input()
                        user_input = validateInteger(user_input)    # validate user_input as a number
                        continue
            
            # Quit Program
            else:
                quitProgram()
        else:
            print("Please choose one of the options available.\n")
            continue