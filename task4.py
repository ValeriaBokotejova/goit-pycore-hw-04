# Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, 
# та буде відповідати відповідно до введеної команди.

# Будь-який CLI складається з трьох основних елементів:
# 1. Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових 
# слів та модифікаторів команд.
# 2. Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
# 3. Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві 
# відповіді від функції - handler-а.

# На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, 
# змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, 
# скористаємося словником. У словнику будемо зберігати ім'я користувача, як ключ, і номер телефону як значення.

# Вимоги до завдання:

# 1. Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
# 2. Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. 
#    Команди та аргументи мають бути розпізнані незалежно від регістру введення.
# 3. Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. 
#    В разі введення команди "exit" або "close", програма повинна завершувати виконання.
# 4. Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
# 5. Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
# 6. Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.


def parse_input(user_input): # Парсер команд
    parts = user_input.split()
    cmd = parts[0].strip().lower() 
    args = parts[1:] 
    return cmd, args


def add_contact(args, contacts): # Додати контакт
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts): # Змінити контакт
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."

def show_phone(name, contacts): # Показати номер телефону
    if name in contacts:
        return f"The phone number for contact '{name}' is {contacts[name]}."
    else:
        return f"Contact '{name}' not found."

def show_all_contacts(contacts): # Показати всі контакти
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."


def main(): # Функція, яка управляє основним циклом обробки команд
    contacts = {}
    print("Welcome to the assistant bot!")

    while True: 
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            print(add_contact(args, contacts))
        elif command == "change" and len(args) == 2:
            print(change_contact(args, contacts))
        elif command == "phone" and len(args) == 1:
            print(show_phone(args[0], contacts))
        elif command == "all" and len(args) == 0:
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

