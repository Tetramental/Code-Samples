# File Name: menuGUIs.py
# Purpose: A module to serve as the graphical backbone of the main program "main.py"
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: February 8, 2019

# STATIC VARIABLES [BEGIN]
# menu decoration
equal = "="
space = " "
vertical = "|"

# menu options
menuOption1 = "Return"
menuMainOption1 = "Display All Media"
menuMainOption2 = "Display All Movies"
menuMainOption3 = "Display All Songs"
menuMainOption4 = "Display All Pictures"
menuMainOption5 = "Quit Program"
menuMovieOption1 = "Play Movie"
menuSongOption1 = "Play Song"
menuPictureOption1 = "Display Picture"
# STATIC VARIABLES [END]
    
def menuMain():
    'The graphical display for the main menu of the simulation of a media library.'
    print(equal * 30)
    print((equal * 5) + (space * 20) + (equal * 5))
    print((equal * 5) + (space + "YOUR MEDIA LIBRARY" + space) + (equal * 5))
    print((equal * 5) + (space * 20) + (equal * 5))
    print(equal * 30)
    print(vertical + (space * 9) + "MAIN MENU" + (space * 10) + vertical)
    print(equal * 30)
    print(vertical + (space * 10) + "OPTIONS" + (space * 11) + vertical)
    print(equal * 30)
    print(vertical + "1] " + menuMainOption1 + (space * 8) + vertical)
    print(vertical + "2] " + menuMainOption2 + (space * 7) + vertical)
    print(vertical + "3] " + menuMainOption3 + (space * 8) + vertical)
    print(vertical + "4] " + menuMainOption4 + (space * 5) + vertical)
    print(vertical + "5] " + menuMainOption5 + (space * 13) + vertical)
    print(equal * 30)

def menuMovie():
    'The graphical display for the movie menu of the simulation of a media library.'
    print(equal * 30)
    print((equal * 5) + (space * 20) + (equal * 5))
    print((equal * 5) + (space + "YOUR MEDIA LIBRARY" + space) + (equal * 5))
    print((equal * 5) + (space * 20) + (equal * 5))
    print(equal * 30)
    print(vertical + (space * 11) + "MOVIES" + (space * 11) + vertical)
    print(equal * 30)
    print(vertical + (space * 10) + "OPTIONS" + (space * 11) + vertical)
    print(equal * 30)
    print(vertical + "1] " + menuMovieOption1 + (space * 15) + vertical)
    print(vertical + "2] " + menuOption1 + (space * 19) + vertical)
    print(equal * 30)

def menuSong():
    'The graphical display for the song menu of the simulation of a media library.'
    print(equal * 30)
    print((equal * 5) + (space * 20) + (equal * 5))
    print((equal * 5) + (space + "YOUR MEDIA LIBRARY" + space) + (equal * 5))
    print((equal * 5) + (space * 20) + (equal * 5))
    print(equal * 30)
    print(vertical + (space * 11) + "SONGS" + (space * 12) + vertical)
    print(equal * 30)
    print(vertical + (space * 10) + "OPTIONS" + (space * 11) + vertical)
    print(equal * 30)
    print(vertical + "1] " + menuSongOption1 + (space * 16) + vertical)
    print(vertical + "2] " + menuOption1 + (space * 19) + vertical)
    print(equal * 30)

def menuPicture():
    'The graphical display for the picture menu of the simulation of a media library.'
    print(equal * 30)
    print((equal * 5) + (space * 20) + (equal * 5))
    print((equal * 5) + (space + "YOUR MEDIA LIBRARY" + space) + (equal * 5))
    print((equal * 5) + (space * 20) + (equal * 5))
    print(equal * 30)
    print(vertical + (space * 10) + "PICTURES" + (space * 10) + vertical)
    print(equal * 30)
    print(vertical + (space * 10) + "OPTIONS" + (space * 11) + vertical)
    print(equal * 30)
    print(vertical + "1] " + menuPictureOption1 + (space * 10) + vertical)
    print(vertical + "2] " + menuOption1 + (space * 19) + vertical)
    print(equal * 30)

# main program
if __name__ == "__main__":
    menuMain()
    menuMovie()
    menuSong()
    menuPicture()