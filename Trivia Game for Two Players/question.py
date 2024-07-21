import main

# File Name: question.py
# Purpose: To create a class of what a trivia question would contain for attributes and behaviors; cheat sheat is provided
# Author: Lange Eo
# Date: January 19th, 2019

class Question:
    
    # initialization method
    def __init__(self, __prompt, __answerPossible1, __answerPossible2, __answerPossible3, __answerPossible4, __answerCorrect):
        self.__prompt = __prompt
        self.__answerPossible1 = __answerPossible1
        self.__answerPossible2 = __answerPossible2
        self.__answerPossible3 = __answerPossible3
        self.__answerPossible4 = __answerPossible4
        self.__answerCorrect = __answerCorrect
    
    # getter methods
    def __getPrompt(self):
        return self.__prompt
    
    def __getAnswerPossible1(self):
        return self.__answerPossible1
    
    def __getAnswerPossible2(self):
        return self.__answerPossible2
    
    def __getAnswerPossible3(self):
        return self.__answerPossible3
    
    def __getAnswerPossible4(self):
        return self.__answerPossible4
    
    def __getAnswerCorrect(self):
        return self.__answerCorrect
    
    # setter methods
    def __setPrompt(self, promptNew):
        self.__prompt = promptNew
        return self.__prompt
    
    def __setAnswerPossible1(self, answerPossible1New):
        self.__answerPossible1 = answerPossible1New
        return self.__answerPossible1
    
    def __setAnswerPossible2(self, answerPossible2New):
        self.__answerPossible2 = answerPossible2New
        return self.__answerPossible2
    
    def __setAnswerPossible3(self, answerPossible3New):
        self.__answerPossible3 = answerPossible3New
        return self.__answerPossible3
    
    def __setAnswerPossible4(self, answerPossible4New):
        self.__answerPossible4 = answerPossible4New
        return self.__answerPossible4
    
    def __setAnswerCorrect(self, __answerCorrectNew):
        self.__answerCorrect = __answerCorrectNew
        return self.__answerCorrect
    
    # overridden string method
    def __str__(self):
        return self.__prompt + "\na) " + self.__answerPossible1 + "\nb) " + self.__answerPossible2 + "\nc) " + self.__answerPossible3 + "\nd) " + self.__answerPossible4 + "\n"

if __name__ == "__main__":
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
    
    quiz01 = Question(question01, "RuenscapeMUD", "GowerMUD", "DeviousMUD", "GielinorMUD", "c")
    quiz02 = Question(question02, "Two", "Three", "Four", "Five", "b")
    quiz03 = Question(question03, "Trick question: her name is simply \"Survival Tutor\"", "Lucy", "Vanessa", "Brynna", "d")
    quiz04 = Question(question04, "Ur-tag", "Bentnoze", "Zanik", "Wormbrain", "c")
    quiz05 = Question(question05, "May 31, 2006", "April 1, 2007", "October 19, 2015", "June 6, 2006", "d")
    quiz06 = Question(question06, "The Black Knights", "The Kinshra", "The Dorgeshuun", "The Godless", "b")
    quiz07 = Question(question07, "96", "32", "27", "151", "a")
    quiz08 = Question(question08, "November 7, 2001", "October 31, 2001", "January 4, 2001", "February 19, 2001", "c")
    quiz09 = Question(question09, "155", "108", "378", "33", "b")
    quiz10 = Question(question10, "2595", "2496", "2715", "3215", "c")
    listOfQuestions = main.createListOfQuestions(quiz01, quiz02, quiz03, quiz04, quiz05, quiz06, quiz07, quiz08, quiz09, quiz10)
    
    # cheat sheet
    title = "Answers to Runescape Trivia Quiz"
    print(title)
    print("-" * len(title))
    i = 1
    for question in listOfQuestions:
        print("Question {:>2d}:".format(i), question._Question__getAnswerCorrect().upper())
        i += 1