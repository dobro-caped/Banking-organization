# bank.py

from customer import Customer
from account import SavingsAccount, CurrentAccount

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def display_customers(self):
        for customer in self.customers:
            print(customer)

if __name__ == "__main__":
    my_bank = Bank("MyBank")

    # Creating customers
    customer1 = Customer("John Doe", "123 Main St")
    customer2 = Customer("Jane Doe", "456 Oak St")

    # Adding customers to the bank
    my_bank.add_customer(customer1)
    my_bank.add_customer(customer2)

    # Displaying customers
    my_bank.display_customers()
