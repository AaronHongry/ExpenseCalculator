class Person:
    def __init__(self, name):
        self.name = name
        self.owe = 0.0
        self.expenses = []
        
    def getName(self):
        return self.name
    
    def getOwe(self):
        return self.owe
    
    def setOwe(self, amount):
        self.owe = amount
    
    def getExpenses(self):
        return self.expenses
    
    def addExpense(self, expense):
        self.owe += round((expense.getCost()) / len(expense.getPeople()), 2)
        self.expenses.append(expense)
        self.expenses = sorted(self.expenses, key=lambda i: i.getName())

    def displayInfo(self):
        return (f"{self.getName():<30} ${self.getOwe():<10.2f} {', '.join(i.getName() for i in self.getExpenses()):<30}")
    
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
        return (f"{self.getName():<30} ${self.getCost():<10.2f} {', '.join(self.getPeople()):<30}")


people = []
expenses = []

print("Calculate your expenses!\n")
tax = (float(input("How much is tax (%): ")) / 100)
tip = (float(input("How much did you tip on the bill (%): ")) / 100)

print('Enter the people involved in the bill:')
userInput = input()
while (userInput != ""):
    people.append(Person(userInput))
    people = sorted(people, key=lambda i: i.getName())
    print(', '.join(i.getName() for i in people))
    userInput = input()


print("\n")
print(f"{'Name':<30} {'Owe':<11} {'Expenses':<30}")
print("-" * 90)
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
        peeps.sort()
        print(', '.join(peeps))
        peopleName = input()
    exp = Expense(itemName, itemCost, peeps)
    for i in people:
        if i.getName() in peeps:
            i.addExpense(exp)
    expenses.append(exp)
    itemName = input("Name of Expense: ")
print("\n\n")    

print(f"{'Expense':<30} {'Cost':<11} {'People':<30}")
print("-" * 90)
for i in expenses:
    print(i.displayInfo())
print("-" * 90)
subtotal = 0.0
for i in expenses:
    subtotal += i.getCost()
print(f"{'Subtotal':<30} ${subtotal:<30.2f}")
taxText = "Tax (" + str(int(tax * 100)) + "%)"
totalBT = subtotal * (1 + tax)
print(f"{taxText:<30} ${(subtotal * tax):<30.2f}")
print("-" * 90)
print(f"{'Total (Before Tip)':<30} ${totalBT:<30.2f}")
tipText = "Tip (" + str(int(tip * 100)) + "%)"
totalAT = totalBT * (1 + tip)
print(f"{tipText:<30} ${(totalBT * tip):<30.2f}")
print("-" * 90)
print(f"{'TOTAL':<30} ${(totalAT):<30.2f}")
print("\n")


print(f"{'Name':<30} {'Owe':<11} {'Expenses':<30}")
print("-" * 90)
for i in people:
    i.setOwe(i.getOwe() * (1 + tax))
    i.setOwe(i.getOwe() * (1 + tip))
for i in people:
    print(i.displayInfo())
print("-" * 90)
oweTotal = 0.0
for i in people:
    oweTotal += i.getOwe()
print(f"{'Total':<30} ${oweTotal:<30.2f}")
print("\n")    


