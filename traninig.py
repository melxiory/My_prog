class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, foodName):
        self.customer.placeOrder(foodName, self.employee)

    def result(self):
        self.customer.printFood()


class Customer:
    def __init__(self):
        self.food = None

    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder((foodName))

    def printFood(self):
        print('Food name - ', self.food.name)


class Employee:
    def takeOrder(self, foodName):
        return Food(foodName)


class Food:
    def __init__(self, name):
        self.name = name

x = Lunch()
x.order('bigmac')
x.result()
x.order('pizza')
x.result()