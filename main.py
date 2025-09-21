import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An error occurred as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits, k = 3)
        spchr = random.choices("!@#$%^&*", k = 1)
        id = alpha + num + spchr
        random.shuffle(id)
        return "".join(id)

    def createAccount(self):
        info = {
            "name": input("Tell your name: "),
            "age" : int(input("Tell your age: ")),
            "email": input("Tell your email: "),
            "pin" : int(input("Tell your 4 number pin: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }

        if info['age'] < 18 and len(str(info['pin'])) != 4:
            print("Sorry you cannot create your account")
        else:
            print("Account created Successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)
            Bank.__update()

    def depositMoney(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("How much you want to deposit: "))
            if amount > 10000 or amount < 0:
                print("Sorry the amount is too much you can deposit below 10000")
            else:
                userdata[0]['balance'] += amount  
                Bank.__update()
                print("Amount deposited Successfully")

    def withdrawMoney(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("How much you want to withdraw: "))
            if userdata[0]['balance'] < amount:
                print("Sorry you don't have that much money")
            else:
                userdata[0]['balance'] -= amount  
                Bank.__update()
                print("Amount withdrew Successfully")

    def showDetails(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print("Your information are: \n")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updateDetails(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("No such user found")
        else:
            print("You cannot change age, account number and balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name" : input("Please tell new name or press enter to skip: "),
                "email": input("Please tell new email or press enter to skip: "),
                "pin" : input("Please tell new pin or press enter to skip: ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]    

            newdata["age"] = userdata[0]["age"]
            newdata["accountNo."] = userdata[0]["accountNo."]
            newdata["balance"] = userdata[0]["balance"]

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Details updated Successfully")

    def delete(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no such details found")
        else:
            check = input("press y if you actually want to delete the account or press n: ")
            if check == 'n' or check == 'N':
                print("Bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted Successfully")
                Bank.__update()

user = Bank()
print("Press 1 for creating an account")
print("Press 2 for depositing the money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting an account")

check = int(input("Tell your response: "))

if check == 1:
    user.createAccount()

if check == 2:
    user.depositMoney()

if check == 3:
    user.withdrawMoney()

if check == 4:
    user.showDetails()

if check == 5:
    user.updateDetails()

if check == 6:
    user.delete()