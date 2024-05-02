# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників 
# у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, 
# які розділені комою без пробілів.

# Наприклад:
# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000

# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл 
# і повертає загальну та середню суму заробітної плати всіх розробників.

# Вимоги до завдання:
# 1. Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# 2. Файл містить дані про заробітні плати розробників, розділені комами. 
#    Кожен рядок вказує на одного розробника.
# 3. Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
# 4. Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат
#    і середньої заробітної плати.

def total_salary(path):
    try:
        with open (path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                name, salary = line.split(',')
                salaries.append(int(salary))
        total_salary = sum(salaries)
        average_salary = total_salary / len(salaries)
        return total_salary, average_salary
    except FileNotFoundError:
        print("Файл відсутній")
        return FileNotFoundError("File not found")
    

# Приклад використання функції:
# total, average = total_salary("path/to/salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
