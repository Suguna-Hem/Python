class Account:    
    def __init__(self,initialbal):
        self.initialbal=initialbal
            
        if self.initialbal < 0.0:
            print( "Initial Balance was Invalid")
            self.initialbal = 0.0            
        return self.initialbal
            
    def credit(self,amt):
        self.initialbal += amt
        return True

    def debit(self,amt):
        if amt <= self.initialbal:
            self.initialbal -= amt
            return True
        else:
            print("Debit amount exceeded account balance")
            return False

    def getBalance(self):
        return self.initialbal

      
class SavingsAccount(Account):
    interest_rate=2
    def __init__(self,initialbal):
        self.initialbal=super().__init__(initialbal)        
        self.interest=0.0
    def calculateInterest(self):
        self.interest = ( (self.initialbal * SavingsAccount.interest_rate) / 100)
        return self.interest
    def getBalance(self):
        self.interest=self.calculateInterest()
        self.initialbal += self.interest
        print(self.initialbal)

 
class CheckingAccount(Account):
    fee=50
    def __init__(self,initialbal):
        self.initialbal=super().__init__(initialbal)
    def credit(self,amt):
        bol=super().credit(amt)
        if True:
           self.initialbal -= CheckingAccount.fee
           print(self.initialbal)
    def debit(self,amt):
        bol=super().debit(amt)
        if True:
           self.initialbal -= CheckingAccount.fee
           print(self.initialbal)


class CurrentAccount(Account):
    max_overdraft_limit=40000
    def __init__(self,initialbal):
        self.initialbal=super().__init__(initialbal)
    def debit(self,amt):
        if self.initialbal <= 0.0:
            if amt <= self.max_overdraft_limit:
                self.max_overdraft_limit -= amt
                self.initialbal -= amt
                print(self.initialbal)
            else:
                print("amount exceeds draft limit")
        else:
            b=super().debit(amt)


 
s1=SavingsAccount(100.00)
s1.getBalance()

ch1=CheckingAccount(100.00)
print(ch1.initialbal)
ch1.credit(200.00)
ch1.debit(50.00)

cu1=CurrentAccount(0.0)
cu1.debit(40000.00)
cu1.debit(100.00)



        
        
        
    
    
        
        
        
        
            
            
        
