class Owner:
    def __init__(self, name, employeeID, employeeList, salary, winPrice):
        self.name = name
        self.employeeID = employeeID
        self.employeeList = employeeList
        self.salary = salary
        self.winPrice = winPrice
    def printInfo(self):
        print("Your name is {}, ID {}, your employees are {}, and your salary is {} ".format(self.name, self.employeeID,self.employeeList, self.salary + self.winPrice * 6/10))
    def BussinessClass(self):
        if self.employeeID < 5:
            print("{}, You have better skills in Network Bussiness".format(self.name))
        else:
            print("{}, You have better skills in Online Selling Bussiness".format(self.name))

class Cleaner(Owner):
    def __init__(self, name, employeeID, employeeList, salary, winPrice):
        super().__init__(name, employeeID, employeeList, salary, winPrice)
    def printInfo(self):
        print("Your name is {}, ID {}, your employees are {}, and your salary is {}".format(self.name, self.employeeID,self.employeeList, self.salary + self.winPrice * 2/10))

class Waitress(Owner):
    def __init__(self, name, employeeID, employeeList, salary):
        super().__init__(name, employeeID, employeeList, salary)
    def printInfo(self):
        print("Your name is {}, ID {}, your employees are {}, and your salary is {}".format(self.name, self.employeeID,self.employeeList, self.salary))

print("Welcome to our Company Game!")
print("Here you can opportunity to be one of the employee of company!")
def playgame():
    chooser = str(input("Choose one: [Owner, Cleaner, Waitress] : "))
    employeeList = ["George", "Angelica", "Nicolas"]
    if chooser == "Owner":
        name = str(input("Enter Your Name Owner! : "))
        employeeID = int(input("Enter Your Employee ID! [1 - 10] : "))
        salary = int(input("Enter your salary, normally it is 5000 : "))
        winPrice = int(input("Enter value of company win in a year, normally it is 20000: "))
        employee = Owner(name, employeeID, employeeList, salary, winPrice)
        employee.printInfo()
        employee.BussinessClass()
    elif chooser == "Cleaner":
        name = str(input("Enter Your Name! : "))
        employeeID = int(input("Enter Your Employee ID! [1 - 10] : "))
        salary = int(input("Enter your salary, normally it is 3000: "))
        winPrice = int(input("Enter value of company win in a year: "))
        employee = Cleaner(name, employeeID, employeeList, salary, winPrice)
        employee.printInfo()
    elif chooser == "Waitress":
        name = str(input("Enter Your Name! : "))
        employeeID = int(input("Enter Your Employee ID! [1 - 10] : "))
        salary = int(input("Enter your salary, normally it is 1000: "))
        winPrice = int(input("Enter value of company win in a year: "))
        employee = Cleaner(name, employeeID, employeeList, salary, winPrice)
        employee.printInfo()
    else:
        print("Type text correct! Something went wrong!")

playgame()