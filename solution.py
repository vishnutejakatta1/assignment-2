import datetime
import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

class User:
    def addUser(self, username, name, phoneno, emailaddress):
        cursor.execute("INSERT INTO User VALUES ('{}', '{}', '{}', '{}')".format(username, name, phoneno, emailaddress))
        connection.commit()
    
    def getName(self, username):
        cursor.execute("SELECT name FROM User WHERE username='{}'".format(username))
        return cursor.fetchall()[0][0]

    def getPhoneNumber(self, username):
        cursor.execute("SELECT phoneno FROM User WHERE username='{}'".format(username))
        return cursor.fetchall()[0][0]

    def getEmailAddress(self, username):
        cursor.execute("SELECT emailaddress FROM User WHERE username='{}'".format(username))
        return cursor.fetchall()[0][0]

    def checkUser(self, username):
        cursor.execute("SELECT username FROM User WHERE username='{}'".format(username))
        if len(cursor.fetchall()) == 0:
            return False
        return True

    def payAmount(self, username, name, amount):
        Orders().placeOrder(username, name, amount)

class FoodItem:
    def showMenu(self):
        print("====================================================")
        print("\t\tDOMINO'S PIZZA MENU")
        print("====================================================")
        print("ID\tPRICE($)\t\tPIZZA TYPE")
        print("====================================================")
        cursor.execute("SELECT id, price, name FROM Fooditem")
        for row in cursor.fetchall():
            print("{}\t${}\t\t\t{}".format(row[0], row[1], row[2]))
        print("====================================================")

    def getPrice(self, id):
        cursor.execute("SELECT price FROM Fooditem WHERE id={}".format(id))
        return cursor.fetchall()[0][0]

    def getName(self, id):
        cursor.execute("SELECT name FROM Fooditem WHERE id={}".format(id))
        return cursor.fetchall()[0][0]

    def getDescription(self, id):
        cursor.execute("SELECT description FROM Fooditem WHERE id={}".format(id))
        return cursor.fetchall()[0][0]

    def addToCart(self, id):
        return None


class Account:
    def createAccount(self):
        print("Kindly register by mentioning the below details :)")
        name = input("Enter your name: ")
        phoneno = input("Enter your phone number: ")
        emailaddress = input("Enter your email address: ")
        while True:
            username = input("Choose a username: ")
            if User().checkUser(username):
                print("A user with {} already exists! Please choose a different one.".format(username))
            else:
                User().addUser(username, name, phoneno, emailaddress)
                print("User registered successfully :)")
                break

class Orders:
    def placeOrder(self, username, name, amount):
        cursor.execute("INSERT INTO Orders (username, name, amount) VALUES ('{}', '{}', {})".format(username, name, amount))
        connection.commit()

    def listOfOrders(self, username, name):
        print("====================================================")
        print("\t\t{}'s ORDERS".format(name.upper()))
        print("====================================================")
        print("S.NO\tPRICE($)\t\tPIZZA TYPE")
        print("====================================================")
        cursor.execute("SELECT amount, name FROM Orders WHERE username='{}'".format(username))
        count = 1
        for row in cursor.fetchall():
            print("{}\t${}\t\t\t{}".format(count, row[0], row[1]))
            count += 1

def main():
    existingCustomer = input("Hello! Are you an existing customer (Y/N)? ")
    if existingCustomer == 'Y':
        username = input("Enter your username: ")
        if not User().checkUser(username):
            print("A user with username {} doesn't exists! Please register first :)".format(username))
        else:
            user = User()
            name = user.getName(username)
            print("Welcome, {}\n".format(name.upper()))
            food = FoodItem()
            food.showMenu()
            foodchoice = int(input("Kindly choose a food item you want to order(1-5): "))
            if foodchoice >= 1 and foodchoice <= 5:
                foodname = food.getName(foodchoice)
                foodprice = food.getPrice(foodchoice)
                fooddescription = food.getDescription(foodchoice)
                user.payAmount(username, foodname, foodprice)
                print("\n{}'s description: {}".format(foodname.upper(), fooddescription))
                print("\nAn order of {} is placed Successfully :)\n".format(foodname.upper()))
                Orders().listOfOrders(username, name)
                print("\nThank you! Do visit us again :)\n")

            else:
                print("Invalid Choice :(")

    elif existingCustomer == 'N':
        account = Account()
        account.createAccount()

    else:
        print("Invalid choice :(")


if __name__ == "__main__":
    main()
    