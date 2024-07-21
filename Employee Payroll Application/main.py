import sys
from employee import Employee
from linkedlist import LinkedList

# File Name: main.py
# Purpose: To simulate a payroll application
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: March 8, 2019

def showMenu():
    '''Displays the main menu of the payroll application'''
    print("*** CS 172 Payroll Simulator ***")
    print("a. Add New Employee")
    print("b. Calculate Weekly Wages")
    print("c. Display Payroll")
    print("d. Update Employee Hourly Rate")
    print("e. Remove Employee from Payroll")
    print("f. Exit the Program")

def validateCharacter(userInput):
    '''Attempts to validate user choice to be a character.
    User must input a character (one letter).'''
    validateInputLoop = True
    while validateInputLoop:
        if len(userInput) == 1:
            if "a" <= userInput.lower() <= "z":
                if "a" <= userInput.lower() <= "f":
                    validateInputLoop = False
                else:
                    print("Please input a character between \"A\" and \"F\".")
                    userInput = input("Enter your choice: ")
            else:
                print("Please don't input numbers and special characters.")
                userInput = input("Enter your choice: ")
        else:
            print("Please limit your response to one character.")
            userInput = input("Enter your choice: ")
    return userInput

def addNewEmployee(passedPayroll):
    '''Adds a new employee through their ID number and given hourly rate
    Checks if there is an existing employee ID; if there is, the user returns to the main menu'''
    
    # asking for user to input the ID of the employee
    user_input_id = input("Enter the new employee ID: ")
    employeeTemp = Employee(user_input_id)
    index, checkEmployeeExist = passedPayroll.search(employeeTemp)
    
    # checks to see if user-inputted ID exists in the payroll or not
    if checkEmployeeExist == True:
        print("\nSorry, that employee ID already exists in the payroll.")
        print("Please choose another option.\n")
    
    # checks if user provides an appropriate input or not
    else:
        validAmount = False
        while not validAmount:
            try:
                user_input_hourlyRate = float(input("Enter the hourly rate (No $): "))
                if user_input_hourlyRate < 6.0:
                    print("You cannot set the hourly rate to less than $6.00 per hour.\n")
                    continue
                else:
                    employeeNew = Employee(user_input_id, user_input_hourlyRate)
                    passedPayroll.append(employeeNew)
                    print("\nSuccess: A new employee has been added to the payroll!")
                    input("\nPress [ENTER] to Continue\n")
                    validAmount = True
            except ValueError:
                print("Please input a valid hourly rate.\n")

def calculateWeeklyWages(passedPayroll):
    '''Calculates the weekly wages for each employee
    Checks if there is/are any employee(s) on the payroll; if there is not, the user returns to the main menu'''
    
    # if there are no employees in the payroll
    if passedPayroll.isEmpty():
        print("Sorry, there is no employee to calculate weekly wages for.")
        print("Please choose another option.\n")
        input("Press [ENTER] to Continue\n")
    
    # if there are employees in the payroll
    else:
        for employee in passedPayroll:
            if employee != None:
                
                # checks if user provides an appropriate input or not
                validAmount = False
                while not validAmount:
                    try:
                        user_input_hoursPerWeek = float(input("\nEnter hours worked for employee " + employee.getEmployeeID() + ": "))
                        employee.setHoursPerWeek(user_input_hoursPerWeek)
                        if user_input_hoursPerWeek < 0.0:
                            print("You cannot set Employee " + employee.getEmployeeID() + " to have worked less than 0 hours.")
                            continue
                        else:
                            validAmount = True
                            print("\nSuccess: Employee " + employee.getEmployeeID() + " has worked " + "{:.2f}".format(user_input_hoursPerWeek) + " hours for this week.")
                    except ValueError as v:
                        print("Please input a valid amount of hours worked per week.")
            else:
                input("\nPress [ENTER] to Continue\n")
                return None

def displayPayroll(passedPayroll):
    '''Displays the payroll of all the employees for the week
    If there is/are no employee(s) to display a payroll for, the user returns to the main menu'''
    print("\n******* Payroll *******")
    
    # if there are no employees in the payroll
    if passedPayroll.isEmpty():
        print("There are no employees. Please enter at least one employee to see a payroll.\n")
        input("Press [ENTER] to Continue\n")
    
    # if there are employees in the payroll
    else:
        for employee in passedPayroll:
            if employee != None:
                print("{:<14s}".format("Employee ID:") + "{:>9s}".format(employee.getEmployeeID()))
                print("{:<14s}".format("Hourly Rate:") + "{:>9.2f}".format(employee.getHourlyRate()))
                print("{:<14s}".format("Hours Worked:") + "{:>9.0f}".format(employee.getHoursPerWeek()))
                print("{:<14s}".format("Gross Wages:") + "{:>9.2f}".format(employee.getGrossWage()) + "\n")
            else:
                print("******* Payroll *******\n")
                input("Press [ENTER] to Continue\n")
                return None

def updateHourlyRate(passedPayroll):
    '''Updates the hourly rate of an employee given the prompt for their ID
    If there is/are no employee(s) on the payroll, the user returns to the main menu
    If the user enters an invalid employee ID to update an hourly rate for, the user returns to the main menu
    Also checks to see if the user has inputted any non-integer/non-float types in input'''
    
    # if there are no employees in the payroll
    if passedPayroll.isEmpty():
        print("There are no employees to update hourly rates for.\n")
        input("Press [ENTER] to Continue\n")
    
    # if there are employees in the payroll
    else:
        # display current payroll with employees and their current hourly rates
        print("{:-<13s}".format("") + "-" + "{:->12s}".format(""))
        print("|{:<12s}".format("Employee ID") + "|" + "{:<11s}|".format("Hourly Wage"))
        print("{:-<13s}".format("") + "-" + "{:->12s}".format(""))
        for employee in passedPayroll:
            if employee != None:
                print("|{:<12s}".format(employee.getEmployeeID()) + "|$" + "{:>10.2f}|".format(employee.getHourlyRate()))
            else:
                break
        print("{:-<15s}".format("") + "-" + "{:->10s}".format(""))
        
        # asking for user to input the ID of the employee
        user_input_id = input("\nEnter the ID of the employee to update their hourly rate: ")
        employeeTemp = Employee(user_input_id)
        index, checkEmployeeExist = passedPayroll.search(employeeTemp)
        
        # checks to see if user-inputted ID exists in the payroll or not
        if checkEmployeeExist == False:
            print("Sorry, that employee ID does not exist in the payroll.")
            print("Please choose another option.\n")
            return None
        
        # checks if user provides an appropriate input or not
        else:
            validAmount = False
            while not validAmount:
                try:
                    user_input_hourlyRate = float(input("Enter the new hourly rate for employee " + passedPayroll[index].getEmployeeID() + " (No $): "))
                    if user_input_hourlyRate < 6.0:
                        print("You cannot set the new hourly rate to less than $6.00 per hour.\n")
                        continue
                    else:
                        passedPayroll[index].setHourlyRate(user_input_hourlyRate)
                        validAmount = True
                        print("\nSuccess: Employee " + passedPayroll[index].getEmployeeID() + "'s hourly rate has been changed to $" + "{:.2f}".format(user_input_hourlyRate))
                        input("\nPress [ENTER] to Continue\n")
                except ValueError as v:
                    print("Please input a valid amount of money.\n")

def removeEmployee(passedPayroll):
    '''Removes an employee from the payroll
    If there is/are no employee(s) on the payroll, the user returns to the main menu
    If the user enters an invalid employee ID to remove from the payroll, the user returns to the main menu'''
    # if there are no employees in the payroll
    if passedPayroll.isEmpty():
        print("There are no employees in the payroll to remove.\n")
        input("Press [ENTER] to Continue\n")
    
    # if there are employees in the payroll
    else:
        # display current employees
        print("{:-^13s}".format(""))
        print("|{:^11s}".format("Employee ID") + "|")
        print("{:-<13s}".format(""))
        for employee in passedPayroll:
            if employee != None:
                print("|{:<11s}".format(employee.getEmployeeID()) + "|")
            else:
                break
        print("{:-^13s}".format(""))
        
        # asking for user to input the ID of the employee
        user_input_id = input("\nEnter the ID of the employee to remove from payroll: ")
        employeeTemp = Employee(user_input_id)
        index, checkEmployeeExist = passedPayroll.search(employeeTemp)
        
        # checks to see if user-inputted ID exists in the payroll or not
        if checkEmployeeExist == False:
            print("Sorry, that employee ID does not exist in the payroll.")
            print("Please choose another option.\n")
            return None
        else:
            print("Success: Employee " + passedPayroll[index].getEmployeeID() + " has been removed from the payroll.")
            passedPayroll.remove(passedPayroll[index])
            input("\nPress [ENTER] to Continue\n")

def quitProgram():
    '''Asks the user to confirm their quit selection.
    Also listens for valid input'''
    
    print("{:-^30s}".format(""))
    print("|{:^28s}|".format("ARE YOU SURE?"))
    print("|{:^28s}|".format("Y/N"))
    print("{:-^30s}".format(""))
    userInput = input("| ANSWER: ")
    loopTemp = True
    while loopTemp:
        if userInput.strip().lower() == "y" or userInput.strip().lower() == "n":
            if userInput.strip().lower() == "y":
                sys.exit(0)
            else:
                print()
                break
        else:
            userInput = input("Please input a valid answer (Y/N): ")
    
# main program
if __name__ == "__main__":
    
    # create new payroll
    employeePayroll = LinkedList()
    
    # menu loop
    menuTrue = True
    while menuTrue:
        showMenu()
        user_input = input("\nEnter your choice: ")
        user_input = validateCharacter(user_input)
        
        # adding new employee
        if user_input.lower() == "a":
            addNewEmployee(employeePayroll)
        
        # calculating weekly wages
        elif user_input.lower() == "b":
            calculateWeeklyWages(employeePayroll)
        
        # displaying the payroll
        elif user_input.lower() == "c":
            displayPayroll(employeePayroll)
        
        # updating the employee hourly rate
        elif user_input.lower() == "d":
            updateHourlyRate(employeePayroll)
        
        # removing an employee from the payroll
        elif user_input.lower() == "e":
            removeEmployee(employeePayroll)
        
        # exiting the program
        elif user_input.lower() == "f":
            quitProgram()