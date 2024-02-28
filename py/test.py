# Polymorphis
# class cat:
#     def make_sound(self):
#         return "Meow"
# class dog:
#     def make_sound(self):
#         return "Woke"   
# def animal_sound(animal):
#         return animal.make_sound()
# cat_instance = cat()
# dog_instance = dog()

# print(animal_sound(cat_instance))
# print(dog().make_sound())



# Encapsulation
# class BackAccount:
#     def __init__(self, balance):
#         self._balance = balance
#     def deposit(self, amount):
#         self._balance += amount
#     def _withdraw(self, amount):
#         if amount <= self._balance:
#             self._balance -= amount
#             return amount
#         else:
#             return "Insufficient funds"
# initial_balance = 50000
# account = BackAccount(initial_balance)
# print(f"{account._balance}")
# account.deposit(5000)
# print(f"{account._balance}")
# withdraw_amount = account._withdraw(3000)
# print(f"Withdraw Amount: {withdraw_amount}")
# print(f"Balance After Paid: {account._balance}")



