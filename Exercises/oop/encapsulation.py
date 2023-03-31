class BankAccount:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        print(self.__balance)

    def get_account_number(self):
        print(self.__account_number)


Richard = BankAccount(1000, 123456789)
Richard.get_account_number()
Richard.get_balance()

Richard.deposit(500)
Richard.get_balance()

Richard.withdraw(1000)
Richard.get_balance()

Richard.__balance = 500000000
Richard.get_balance()























