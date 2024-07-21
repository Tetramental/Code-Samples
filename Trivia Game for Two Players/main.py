import sys
import question

# File Name: main.py
# Purpose: To simulate a simple trivia game for two players who will take turns in answering questions
# Author: Lange Eo
# Date: January 19th, 2019

def createListOfQuestions(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    'Creates and returns a list of questions based on ten (10) given objects of class Question.'
    listQuestions = []
    listQuestions.append(q1)
    listQuestions.append(q2)
    listQuestions.append(q3)
    listQuestions.append(q4)
    listQuestions.append(q5)
    listQuestions.append(q6)
    listQuestions.append(q7)
    listQuestions.append(q8)
    listQuestions.append(q9)
    listQuestions.append(q10)
    return listQuestions

def printPlayerScores(player1, player2):
    'Prints both of the players\' current scores.'
    print("Player 1:", player1)
    print("Player 2:", player2)
    print("\n")

def switchActivePlayer(player1, player2):
    'Switches which player\'s turn it is.'
    if player1 == True:
        player2 = True
        player1 = False
    else:
        player1 = True
        player2 = False
    return player1, player2

def endOfGameScores(score1, score2):
    'Computes the winner of the trivia quiz.'
    if score1 > score2:
        return "Player 1 wins!\n"
    elif score2 > score1:
        return "Player 2 wins!\n"
    else:
        return "It's a tie!\n"

def resetScores(score1, score2):
    'Resets the players\' current scores to zero (0).'
    score1 = 0
    score2 = 0
    return score1, score2

def playAgain():
    '''Presents the option of playing the trivia quiz again to the players.
    If the player says "no", then the script will abruptly end.
    If an invalid input has been given, the question will repeatedly ask the player to type a valid input.'''
    breakOutOfLoop = False
    while not breakOutOfLoop:
        user_input_playAgain = input("Would you like to play again? (Y/N): ")
        user_input_playAgain = user_input_playAgain.strip().lower()
        if user_input_playAgain == "y" or user_input_playAgain == "n":
            if user_input_playAgain == "y":
                print("\n")
                breakOutOfLoop = True
            elif user_input_playAgain == "n":
                sys.exit(0)
        else:
            print("Please type in either \"Y\" or \"N\".\n")
            continue

# main program
if __name__ == "__main__":
    '''Main Program:
    Questions and answers may be changed here.'''
    
    # declaring and assigning variables
    question01 = "Runescape debuted in 2001. However, it started in 1998 as a game called..."
    question02 = "Runescape was created by the Gower brothers. How many Gower brothers are there?"
    question03 = "In the now defunct Tutorial Island, you meet a Survival Tutor. She introduces herself as..."
    question04 = "Which of the following characters is the only goblin given multiple graphical updates in the past few years?"
    question05 = "The infamous \"Falador Massacre\" occurred as a result of a glitch in a player-owned house. Coincidentally, it occurred on what date?"
    question06 = "The \"Black Knights\" are an iconic order found throughout Runescape. What is the name of their order?"
    question07 = "As of February 19, 2016, how many abilities are available?"
    question08 = "Runescape debuted on what date?"
    question09 = "As of February 19, 2016, how many quest points are required in order to begin the Legends' Quest?"
    question10 = "As of February 19, 2016, what is the highest possible total level?"
    
    quiz01 = question.Question(question01, "RuenscapeMUD", "GowerMUD", "DeviousMUD", "GielinorMUD", "c")
    quiz02 = question.Question(question02, "Two", "Three", "Four", "Five", "b")
    quiz03 = question.Question(question03, "Trick question: her name is simply \"Survival Tutor\"", "Lucy", "Vanessa", "Brynna", "d")
    quiz04 = question.Question(question04, "Ur-tag", "Bentnoze", "Zanik", "Wormbrain", "c")
    quiz05 = question.Question(question05, "May 31, 2006", "April 1, 2007", "October 19, 2015", "June 6, 2006", "d")
    quiz06 = question.Question(question06, "The Black Knights", "The Kinshra", "The Dorgeshuun", "The Godless", "b")
    quiz07 = question.Question(question07, "96", "32", "27", "151", "a")
    quiz08 = question.Question(question08, "November 7, 2001", "October 31, 2001", "January 4, 2001", "February 19, 2001", "c")
    quiz09 = question.Question(question09, "155", "108", "378", "33", "b")
    quiz10 = question.Question(question10, "2595", "2496", "2715", "3215", "c")
    listOfQuestions = createListOfQuestions(quiz01, quiz02, quiz03, quiz04, quiz05, quiz06, quiz07, quiz08, quiz09, quiz10)
    
    # players' stats
    player1State = True
    player2State = False
    player1Score = 0
    player2Score = 0
    
    # ability to play game again when end has been reached
    loopGame = True
    while loopGame:
        # reset players' scores to 0
        player1Score, player2Score = resetScores(player1Score, player2Score)
        messageWelcome = "Welcome to the Runescape Trivia Quiz!"
        print(messageWelcome)
        print("-" * len(messageWelcome) + "\n")
        
        # iterate through each trivia question
        for question in listOfQuestions:
            
            # the current player's turn and printing out the question
            if player1State == True:
                print("Player 1, here is your question:")
            else:
                print("Player 2, here is your question:")
            print(question)
            
            # checking for invalid input
            # checking player's answer to see if correct
            # if correct, the player gets one point added to their score
            valid = True
            while valid:
                user_input_answer = input("Enter your answer: ")
                user_input_answer = user_input_answer.strip().lower()
                if user_input_answer == "a" or user_input_answer == "b" or user_input_answer == "c" or user_input_answer == "d":
                    if user_input_answer == question._Question__getAnswerCorrect():
                        print("\nExcellent! You score!")
                        if player1State == True:
                            player1Score += 1
                        else:
                            player2Score += 1
                        printPlayerScores(player1Score, player2Score)
                        valid = False
                    else:
                        print("\nThat is incorrect. Try again on your next question!\n")
                        valid = False
                else:
                    print("Error: your answer has to be a value between \"a\" and \"d\". Try again.")
                    continue
            
            # at end of each question, switch active player
            player1State, player2State = switchActivePlayer(player1State, player2State)
        
        # printing end-of-game scores
        print("And the final scores are:")
        printPlayerScores(player1Score, player2Score)
        winner = endOfGameScores(player1Score, player2Score)
        print(winner.upper())
        
        # ask to play again
        playAgain()