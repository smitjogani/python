# implement single inheritance in two sub classes are derived from a single base class

class Bank(object):
    cash = 5000000

    @classmethod
    def avalable_cash(cls):
        print(cls.cash)

class AndraBank(Bank):
    pass

class StateBank(Bank):
    cash = 2000000

    @classmethod
    def avalable_cash(cls):
        print(cls.cash + Bank.cash)

a = AndraBank()
a.avalable_cash()

s = StateBank()
s.avalable_cash()