#question
'''
Encapsulation using private variables
'''
#answer/code
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount(1000)
acc.show_balance()