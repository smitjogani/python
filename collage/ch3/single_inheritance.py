class Bank(object):
    cash = 5000000
    @classmethod
    def avalable_cash(cls):
        print("Cash : ",cls.cash)

class BOB(Bank):
    pass

class SBI(Bank):
    cash = 2000000
    @classmethod
    def avalable_cash(cls):
        print("Cash in SBI : ",cls.cash + Bank.cash)

class ICICI(Bank):
    cash = 3000000
    @classmethod
    def avalable_cash(cls):
        print("Cash in ICICI : ", cls.cash + Bank.cash)

b = BOB
b.avalable_cash()
s = SBI
s.avalable_cash()
i = ICICI
i.avalable_cash()