# Encapsulations
class BankAccount:
    def __init__(self, name , account , balance, phone):
        self.name = name # public acccessed specifier
        self._account = account # protected accessed specifier 
        self.__balance = balance # private accessed specifier 
        self.phone = phone #public specifier

    def get_balance(self):
        return self.name , self._account , self.__balance , self.phone 

# এখানে __balance একটি private attribute, যা সরাসরি অ্যাক্সেস করা যায় না। 
# শুধুমাত্র get_balance() মেথড দিয়ে এটি দেখা যায়

accountBalance = BankAccount("Mamun" , "12122454545" , 10000 , +8801953103206)
print(accountBalance.get_balance())

# let check accessed specifier - name is public 
print(accountBalance.name) 

# protector not access from here 
print(accountBalance._account)

