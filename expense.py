class Person:
    def __init__(self, name):
        self.name = name
        self.owe = 0.0
        self.expenses = []
        
    def getName(self):
        return self.name
    
    def getOwe(self):
        return self.owe
    
    def getExpenses(self):
        return self.expenses
    
    def addExpense(self, expense):
        self.owe += round((expense.getCost()) / len(expense.getPeople()), 2)
        self.expenses.append(expense)

    def displayInfo(self):
        return (f"{self.getName():<15} {self.getOwe():<10.2f} {', '.join(i.getName() for i in self.getExpenses()):<30}")
    
class Expense:
    def __init__(self, name, cost, people):
        self.name = name
        self.cost = cost
        self.people = people

    def getName(self):
        return self.name
    
    def getCost(self):
        return self.cost
    
    def getPeople(self):
        return self.people
    
    def displayInfo(self):
        return (f"{self.getName():<15} {self.getCost():<10.2f} {', '.join(self.getPeople()):<30}")


people = []
expenses = []

print("Calculate your expenses!")
tax = 1 + (float(input("How much did you tip on the bill (%): ")) / 100)
subtotal = 0.0

print('Enter the people involved in the bill:')
userInput = input()
while (userInput != ""):
    people.append(Person(userInput))
    print(', '.join(i.getName() for i in people))
    userInput = input()
print("\n")
print(f"{'Name':<15} {'Owe':<10} {'Expenses':<30}")
print("-" * 60)
for i in people:
    print(i.displayInfo())
print("\n")    

print('Enter the expenses involved in the bill:')
itemName = input("Name of Expense: ")
while (itemName != ""):
    itemCost = float(input("Cost of Expense: "))
    peeps = []
    print('Enter the people splitting this expense:')
    peopleName = input()
    while (peopleName != ""):
        peeps.append(peopleName)
        print(', '.join(peeps))
        peopleName = input()
    exp = Expense(itemName, itemCost, peeps)
    for i in people:
        if i.getName() in peeps:
            i.addExpense(exp)
    expenses.append(exp)
    itemName = input("Name of Expense: ")
print("\n\n")    

print(f"{'Expense':<15} {'Cost':<10} {'People':<30}")
print("-" * 60)
for i in expenses:
    print(i.displayInfo())
print("\n")

print(f"{'Name':<15} {'Owe':<10} {'Expenses':<30}")
print("-" * 60)
for i in people:
    print(i.displayInfo())
print("\n")    


