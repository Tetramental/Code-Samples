# File Name: employee.py
# Purpose: To create an employee used for a payroll application
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: March 8, 2019

class Employee:
    '''This class defines an instance of an Employee.
    Has the attributes:
    1) Employee Identification
    2) Hours Worked per Week
    3) Amount of Money Paid Hourly Rate
    4) Calculated Gross Wage per Week'''
    
    # initialization method
    def  __init__ (self, employeeID = "00000", hourlyRate = 0, hoursPerWeek = 0):
        if employeeID == "":
            self.__employeeID = "Unknown"
        else:
            self.__employeeID = employeeID
        self.__hourlyRate = float(hourlyRate)
        self.__hoursPerWeek = float(hoursPerWeek)
        self.__grossWage = self.__hourlyRate * self.__hoursPerWeek
    
    # overloaded string method
    def __str__ (self):
        return "This employee has the ID: " + self.__employeeID + ". They work " + "{0:.0f}".format(self.getHoursPerWeek()) + " hours/week with an hourly rate of $" + "{0:.2f}".format(self.getHourlyRate()) + ". They make a gross wage of $" + "{0:.2f}".format(self.getGrossWage()) + " per week."
    
    # returns the employee's identification
    def getEmployeeID(self):
        return self.__employeeID
    
    # returns the employee's hours per week
    def getHoursPerWeek(self):
        return float(self.__hoursPerWeek)
    
    # returns the employee's hourly rate
    def getHourlyRate(self):
        return float(self.__hourlyRate)
    
    # returns the employee's gross wage
    def getGrossWage(self):
        return float(self.getHoursPerWeek() * self.getHourlyRate())
    
    # sets the employee's hours per week
    def setHoursPerWeek(self, new):
        self.__hoursPerWeek = new
    
    # sets the employee's hourly rate
    def setHourlyRate(self, new):
        self.__hourlyRate = new
    
# main program
if __name__ == "__main__":
    employee1 = Employee("00000001", 35, 25)
    employee2 = Employee("00000002", 40, 30)
    employee3 = Employee("00000003", 55, 30)
    
    print(employee1)
    print(employee2)
    print(employee3)
    
    help(__name__)