import random

flag = True

def random_num() -> int:
    """Функция генерирует случайную цифру"""

    num: int = random.randint(1, 9)
    return num

def respond(num: any) -> bool:
    """В будущем будет реализована проверка вводимых пользователем данных"""
    pass

print("Добро пожаловать в игру <Угадай число>!!")
print("Давай, загадывай, я уже готов!!")

# цифра, которую "компьютер загадал"
num_comp = random_num()

while flag:
    
    num_user = int(input())

    # if respond(num_user):

    if num_comp == num_user:
        flag = False
        print("Ты угадал!!")


        #это я спиздил :) сук, пиздато, особенно как это написано нравится
        print(
            '\n'.join(' '.join(*zip(*row))
             for row in ([["*" if row==0 and col%3!=0 or row==1 and col%3==0 or row-col==2 or row+col==8
             else " " for col in range(7)] for row in range(6)]))
             )
    else:
        print("Ох, по идее близко")