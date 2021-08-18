class Category:

    first_time = True

    def __init__(self,name):
        self.name = name
        self.ledger = list()

    def deposit(self,amount,description = None):
        ledger_deposit = dict()
        ledger_deposit['amount'] = amount
        if not description:
            ledger_deposit['description'] = ''
        else:
            ledger_deposit['description'] = description
        self.ledger.append(ledger_deposit)

    def withdraw(self,amount_2,description_2 = None):
        ledger_withdraw = dict()
        funds_list = list()
        if self.first_time == True:
            funds = self.ledger[0]['amount'] - amount_2
            
        if self.first_time == False:
            funds = sum(funds_list) - amount_2
            
        if funds <= 0:
            return False
        else:
            ledger_withdraw['amount'] = -amount_2
            if not description_2:
                ledger_withdraw['description'] = ''
            else:
                ledger_withdraw['description'] = description_2
            self.ledger.append(ledger_withdraw)
            funds_list.append(funds)
            self.first_time = False
            return True
    

thing = Category('food')
thing.deposit(200,'deposit')
thing.withdraw(400)
thing.withdraw(10)

print(thing.ledger)
print()





