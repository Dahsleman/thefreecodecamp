import random
import copy


class Hat:

    def __init__(self,**kwargs) -> list:
        self.kwargs = kwargs
        self.contents = list()
        for key, value in kwargs.items():
            self.contents.extend([key]*value)


    def draw(self, number:int) -> list:
        numbers = range(number)
        draw_list = list()
        for num in numbers:
            if self.contents != []:
                random_item_from_list = random.choice(self.contents)
                draw_list.append(random_item_from_list)
                self.contents.remove(random_item_from_list)
            else:
                self.contents.extend(draw_list)
                random_item_from_list = random.choice(self.contents)
                draw_list.append(random_item_from_list)
                self.contents.remove(random_item_from_list)
        return draw_list
    
def is_subseq(sublist, list) -> bool:
    list = sorted(list)
    sublist = sorted(sublist)
    """Check whether v2 is a subsequence of v1."""
    it = iter(list)
    return all(c in it for c in sublist)

def experiment(**kwargs) -> float:
    kwargs_list = list()
    for key, value in kwargs.items():
        kwargs_list.append(value)

    hat = kwargs_list[0]
    expected_balls = kwargs_list[1]
    num_balls_drawn = kwargs_list[2]
    num_experiments = kwargs_list[3]
    #making a list of expected_balls
    expected_balls_list = list()
    for key, value in expected_balls.items():
        expected_balls_list.extend([key]*value)
    
    num_experiments_range = range(num_experiments)
    contador = 0
    for num in num_experiments_range:
        hat_list = hat.draw(num_balls_drawn)
       
        if is_subseq(expected_balls_list,hat_list) == True:
            contador += 1
            hat.contents.extend(hat_list)
            hat_list.clear()
        else:
            hat.contents.extend(hat_list)
            hat_list.clear()

    return contador/num_experiments

hat = Hat(blue=3, red=2, green=6)

probability = experiment(hat=hat, 
                  expected_balls={"blue":2,"green":1},
                  num_balls_drawn=4,
                  num_experiments=1000)
print(probability)

lista = ['blue','red','yellow']
sublista = ['red','blue','blue']

print(is_subseq(sublista,lista))













