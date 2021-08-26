from __future__ import annotations

class Category:


    def __init__(self,name:str):

        self.name = name
        self.ledger = list()
        self.funds = 0
        self.withdraws = 0

    def __str__(self):
      return self.print_essa_bosta()

    def deposit(self,amount:float,description:str = None) -> None:
        ledger_deposit = dict()
        ledger_deposit['amount'] = amount
        if not description:
            ledger_deposit['description'] = ''
        else:
            ledger_deposit['description'] = description
        self.ledger.append(ledger_deposit)
        self.funds += amount
    
    def get_balance(self):
        return self.funds

    def check_funds(self,amount:float) -> bool:
        if amount > self.get_balance():
            return False
        else:
            return True

    def withdraw(self,amount:float,description:str = None) -> bool:
        ledger_withdraw = dict()
        if self.check_funds(amount) == False:
            return False
        else:
            ledger_withdraw['amount'] = -amount
            if not description:
                ledger_withdraw['description'] = ''
            else:
                ledger_withdraw['description'] = description
            self.ledger.append(ledger_withdraw)
            self.funds += -amount
            self.withdraws += amount
            return True

    def transfer(self,amount:float,budget:Category) -> bool:
        if self.check_funds(amount) == False:
            return False
        else:
            self.withdraw(amount,f'Transfer to {budget.name}')
            budget.deposit(amount,f'Transfer from {self.name}')
            return True

    def list_of_items(self) -> str:
        lista = ''
        items = list()
        for dict in self.ledger:
            for key in dict:
                items.append(dict[key])
                if len(items) == 2:
                    lista += f'{items[1]:23.23}{items[0]:>7.2f}\n'
                    items.clear()
        return lista

    def total(self) -> str:
        return f'Total: {self.get_balance():.2f}'
                
    def print_essa_bosta(self) -> str:
        return f'{self.name:*^30}\n{self.list_of_items()}{self.total()}'

    def total_withdraw(self):
        return self.withdraws


def total_withdraws(categories:list) -> float:
    tw = 0
    for category in categories:
        tw += category.total_withdraw()

    return tw


def vertically_category(categories:Category) -> str:
    # linha dos tracinhos
    letters = f'---'
    n_letters = len(categories)
    letters = n_letters*letters
    letters = f'{letters}\n'

    # Calc the line max
    lines_number = 0

    for category in categories:
        category_list = list(str(category.name))
        new_len = len(category_list)
        if lines_number < new_len:
            lines_number = new_len

    lines = range(lines_number)

    # return de letters
    letters_list = list()

    for line in lines:
        for category in categories:
            category_list = list(str(category.name))
            if len(category_list)-1 < line:
                letters_list.append(' ')
            else:
                letters_list.append(category_list[line])
            category_list.clear()
    
        first = True
        for letter in letters_list:
            if first == True:
                letters += f'{letter:>6}'
            
            if first == False:
                letters += f'{letter:>3}'

            first = False

        letters += f'  \n'
        letters_list.clear()
        first = True

    return letters[:-1]

def percentual(categories:list) -> list:
    percentual_list = list()
    for category in categories:
        div = category.total_withdraw()/total_withdraws(categories)
        div = div*100
        div = int(div/10)
        div = div*10
        percentual_list.append(div)
    return percentual_list

def grafic(num:int,number:int,first:bool) -> str:
    primeira_bolinha = f' o'
    primeiro_vazio = f'  '
    bolinha = f'  o'
    vazio = f'   '
    grafico = f''
    if first == True:
        if num == number:
            grafico += primeira_bolinha
        else:
            grafico += primeiro_vazio

    if first == False:
        if num == number:
            grafico += bolinha
        else:
            grafico += vazio
    
    return grafico

def bolinha(percentual_list:list) -> str:
    first = True
    indice = [100,90,80,70,60,50,40,30,20,10,0]
    new_list = []
    grafico = f'Percentage spent by category\n'
    for num in indice:
        grafico += f'{num:>3}|'
        for number in percentual_list:
            grafico += f'{grafic(num,number,first)}'
            first = False
            if number == num:
                number = number - 10
            
            new_list.append(number) 
        percentual_list.clear()
        percentual_list.extend(new_list)
        new_list.clear()
        grafico += f'  \n'
        first = True
    
    return grafico

def create_spend_chart(categories:list) -> str:

    return f'{bolinha(percentual(categories))}    -{vertically_category(categories)}'

food = Category('Food')
drink = Category('Drink')
roupa = Category('Roupa')
outro = Category('Outro')
outro_1 = Category('Outro1')
outro_2 = Category('Outro2')
outro_3 = Category('Outro3')
outro_4 = Category('Outro4')


food.deposit(1000,'initial deposit')
food.withdraw(10.15,'groceries')
food.withdraw(15.89,'restaurant and more food for dessert')
food.transfer(100.70,drink)
food.total_withdraw()
drink.withdraw(100)
outro_1.deposit(1000,'initial deposit')
outro_1.withdraw(10.15,'groceries')
outro_1.withdraw(55.89,'restaurant and more food for dessert')
outro_3.deposit(1000,'initial deposit')
outro_3.withdraw(10.15,'groceries')
outro_3.withdraw(75.89,'restaurant and more food for dessert')
# total_withdraws([food,drink,roupa,outro,outro_1,outro_2,outro_3,outro_4])
# x = grafic(100,'',100,'','')
# x = percentual([food,drink])
x = bolinha([50,40,40,30,10,20])
x = vertically_category([food,drink,roupa,outro])
x = create_spend_chart([food,drink,roupa,outro,outro_1,outro_2,outro_3,outro_4])
print(x)
