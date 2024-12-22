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

    if random_num() == num_user:
        flag = False
        print("Ты угадал!!")
    else:
        print("Ох, по идее близко")