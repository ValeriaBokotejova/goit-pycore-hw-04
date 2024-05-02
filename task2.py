# У вас є текстовий файл, який містить інформацію про котів. 
# Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. 
# Наприклад:

# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5

# Ваше завдання - розробити функцію get_cats_info(path), 
# яка читає цей файл та повертає список словників з інформацією про кожного кота.

# Вимоги до завдання:
# Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
# Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


def get_cats_info(path):
    catbase = []
    try:
        with open(path, "r", encoding=("utf-8")) as file:
            for line in file:
                cat_data = line.strip().split(",")
                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                catbase.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено")

    return catbase


# Приклад використання функції:
# cats_info = get_cats_info("path/to/cats_file.txt")
# print(cats_info)

