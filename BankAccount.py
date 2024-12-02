class Account(object):
    def set(self,value):
        self.balance=value 
    def get(self):
        return self.balance

    def deposit(self,amount):
        'apdates the balance by amount'
        self.balance+=amount
    def withdraw(self,w_amount):
        'withdraw some money from the acccount'
        self.balance-=w_amount
        

class Savings(Account):
    'models a saving account with the sab class of class Acount'
    def __init__(self,amount=0,rate=.043):
        Account.__init__(self)
        self.balance=amount
        self.rate=rate
    def set_rate(self,value):
        'sets the annoual interst rate'
        self.rate=value
        
    def add_interest(self):
        'calculates one month of interest and adds it to the balance'
        self.balance=self.balance*(1+(self.rate/12))
        
    def get(self):
        'returns the vlaue of the balance and the interets rate'
        return f'Balance={self.balance:.2f}\nRate={self.rate}'
    def __repr__(self):
        
        return f'Balance={self.balance:.2f}\nRate={self.rate}'

    def __str__(self):
        return self.get()

class Money_market(Savings):
    'models the account with a minimum balance requrirment'
    def __init__(self,value=1000,rate=.05,m=1000):
        Savings.__init__(self,value,rate)
        self.balance=value
        self.rate=rate
        self.min=m
    def withdraw(self,amount):
        if self.balance-amount>=1000:
            self.balance-=amount
            return True
        else:
            print('trying to withdraw more than money that you have')
            return False
    def __eq__(self,other): 
        'compare two money market accounts'
        return self.balance==other.balance and self.rate==other.rate and self.min==other.min
        
    
    def __repr__(self):
        
        return f'Balance={self.balance:.2f}\nRate={self.rate}\nMinimum balance is {self.min}'

    
    def __str__(self):
        
        return f'Balance={self.balance:.2f}\nRate={self.rate}\nMinimum balance is {self.min}'

    

    
