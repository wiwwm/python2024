import random

flag = True

main_dict = {
                1: "камень",
                2: "ножницы",
                3: "бумага"
            }

def comp_choice() -> int:
    """случайное число == случайный ключ словаря"""
    num = random.randint(1, 3)
    return num

def fight(comp: int, user: int) -> bool | str:
    temp = {
        'user': user,
        'comp': comp
    }

    #if main_dict[1]

def respond(user: int) -> bool:
    """В будущем будет реализована проверка вводимых пользователем данных"""
    pass

print(
    """1 - камень, 2 - ножницы, 3 - бумага"""
)


while flag:

    user = int(input())
    comp = comp_choice()

    if fight(comp, user):
        pass