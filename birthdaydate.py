from datetime import date

# 1. Функция определения дня недели
def get_day_of_week(day: int, month: int, year: int) -> str:
    days = [
        "Понедельник", "Вторник", "Среда", "Четверг",
        "Пятница", "Суббота", "Воскресенье"
    ]
    birth_date = date(year, month, day)
    return days[birth_date.weekday()]

# 2. Функция проверки года на високосность
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 3. Функция расчёта текущего возраста пользователя
def calculate_age(day: int, month: int, year: int) -> int:
    today = date.today()
    age = today.year - year
    # Если день рождения в этом году ещё не наступил, вычитаем 1 год
    if (today.month, today.day) < (month, day):
        age -= 1
    return age

# 4. Функция вывода даты звёздочками (*) как на электронном табло (дд мм гггг)
def print_digital_date(day: int, month: int, year: int) -> None:
    digits_art = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "    *", " *** ", "*    ", "*****"],
        '3': [" *** ", "    *", " *** ", "    *", " *** "],
        '4': ["*   *", "*   *", "*****", "    *", "    *"],
        '5': ["*****", "*    ", "**** ", "    *", "**** "],
        '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["*****", "    *", "   * ", "  *  ", "  *  "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " ****", "    *", " *** "],
        ' ': ["   ", "   ", "   ", "   ", "   "]
    }
    
    # Форматируем дату в строку вида "дд мм гггг" с ведущими нулями
    formatted_date = f"{day:02d} {month:02d} {year:04d}"
    
    # Построчно собираем и выводим 5 уровней высоты символов
    for row in range(5):
        line = "  ".join(digits_art[char][row] for char in formatted_date)
        print(line)

# Основной блок программы: последовательный запрос данных у пользователя
def main():
    try:
        day = int(input("Введите день рождения (1-31): "))
        month = int(input("Введите месяц рождения (1-12): "))
        year = int(input("Введите год рождения (например, 2000): "))
        
        # Проверка корректности существования даты
        date(year, month, day)
        
        weekday = get_day_of_week(day, month, year)
        leap_status = "Високосный" if is_leap_year(year) else "Не високосный"
        age = calculate_age(day, month, year)
        
        print("\n--- Результаты анализа ---")
        print(f"День недели: {weekday}")
        print(f"Год рождения ({year}): {leap_status}")
        print(f"Ваш текущий возраст: {age} лет/год(а)")
        print("\nДата рождения на электронном табло (дд мм гггг):\n")
        print_digital_date(day, month, year)
        
    except ValueError as e:
        print(f"\nОшибка ввода данных: введена некорректная дата ({e}).")

if __name__ == "__main__":
    main()