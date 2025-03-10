#Завдання_№1

from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Розрахунок кількості днів між заданою датою та поточною.
    """
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        days_diff = (target_date - today).days
        return days_diff
    except ValueError:
        raise ValueError("Невірний формат дати. Використовуйте 'РРРР-ММ-ДД'.")

# Тестування функції
date_input = "2021-10-09"
days_diff = get_days_from_today(date_input)
print(f"Дни между {date_input} и сегодня: {days_diff} дней.")

#Завдання_№2

import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Генерує список унікальних випадкових чисел в заданому діапазоні.
    """
    if not (1 <= min <= max <= 1000 and min <= quantity <= (max - min + 1)):
        return []
    numbers = sorted(random.sample(range(min, max + 1), quantity))
    print(f"Сгенеровані числа: {numbers}")
    return numbers
# Тестування функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

#Завдання_№3

import re

def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує номер телефону, видаляючи зайві символи та додаючи міжнародний код.
    """
    # Видаляємо всі символи, окрім цифр та знака '+'
    digits = re.sub(r'\D', '', phone_number)
    
    # Якщо номер починається з міжнародного коду +380 або 380
    if digits.startswith('380'):
        normalized_phone = f'+{digits}'
    # Якщо номер починається з нуля, додаємо код +38
    elif digits.startswith('0'):
        normalized_phone = f'+38{digits[1:]}'  # Видаляємо нуль на початку
    else:
        # Якщо номер не містить міжнародного коду, додаємо +38
        normalized_phone = f'+38{digits}'
    
    return normalized_phone

# Тестування функції
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#Завдання_№4

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Запитуємо у користувача, чи хоче він ввести свою дату або використовувати поточну
    user_input = input("Введіть дату у форматі РРРР.ММ.ДД або натисніть Enter для поточної дати: ")

    if user_input:
        try:
            today = datetime.strptime(user_input, "%Y.%m.%d").date()  # Перетворюємо введену дату в об'єкт datetime
        except ValueError:
            print("Невірний формат дати. Використовуємо поточну дату.")
            today = datetime.today().date()  # Використовуємо поточну дату, якщо формат неправильний
    else:
        today = datetime.today().date()  # Використовуємо поточну дату, якщо не введено

    print(f"Сьогоднішня дата: {today}")  # Виводимо поточну дату для перевірки
    upcoming_birthdays = []

    # Проходимо по всіх користувачах
    for user in users:
        # Перетворюємо строку з датою народження в об'єкт datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Якщо день народження вже був в цьому році, переносимо його на наступний рік
        if birthday.replace(year=today.year) < today:
            # Якщо день народження вже минув у поточному році, переносимо на наступний
            birthday = birthday.replace(year=today.year + 1)
        else:
            # Якщо день народження ще не був у цьому році, використовуємо поточний рік
            birthday = birthday.replace(year=today.year)
        
        # Перевіряємо, чи потрапляє день народження в наступні 7 днів
        if today <= birthday <= today + timedelta(days=7):
            
            # Якщо день народження припадає на вихідний (субота чи неділя), переносимо його на понеділок
            if birthday.weekday() == 5:  # Якщо субота
                birthday = birthday + timedelta(days=2)  # Переносимо на понеділок
                # Виводимо повідомлення з інформацією про перенесення
                print(f"День народження {user['name']} припадає на суботу ({user['birthday']}), привітання переносимо на понеділок: {birthday.strftime('%Y-%m-%d')}")
            elif birthday.weekday() == 6:  # Якщо неділя
                birthday = birthday + timedelta(days=1)  # Переносимо на понеділок
                # Виводимо повідомлення з інформацією про перенесення
                print(f"День народження {user['name']} припадає на неділю ({user['birthday']}), привітання переносимо на понеділок: {birthday.strftime('%Y-%m-%d')}")

            # Додаємо користувача та дату привітання в список
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%Y.%m.%d")  # Форматуємо дату як рядок
            })

    #print(f"Список привітань: {upcoming_birthdays}")  # Виводимо список привітань перед поверненням
    print("Список привітань на цьому тижні:")
    for item in upcoming_birthdays:
        print(f"Ім'я: {item['name']}, Дата привітання: {item['congratulation_date']}")

    return upcoming_birthdays

# Приклад використання функції
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Mara Bond", "birthday": "1995.03.13"},
    {"name": "Andreas Bosch", "birthday": "1995.03.15"},
    {"name": "Rita Konig", "birthday": "1995.03.18"}

]

# Отримуємо список днів народжень на наступному тижні
upcoming_birthdays = get_upcoming_birthdays(users)

# Виводимо список привітань на цьому тижні
# print("Список привітань на цьому тижні:", upcoming_birthdays)