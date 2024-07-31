# Yurii Zosia
# Піфагорів трикутник, a² + b² = c²
from datetime import datetime
import logging

# Конфігурація логування
# Можливі значення: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(filename='Pythagorean_pants.log', level=logging.DEBUG)

# Отримання поточної дати та часу
current_datetime = datetime.now()

# Формування приставки на основі дати та часу
timestamp_prefix = current_datetime.strftime("%Y%m%d_%H%M%S")

logging.info(f'{timestamp_prefix} Програма запущена!')

def check_numbers(input_string):
  """Перевіряє, чи введений рядок містить три невід'ємних числа, розділених комою.
    True, якщо введені дані коректні, інакше False.
  """
  # Видаляємо всі пробіли перед розділенням
  input_string = input_string.strip()
  
  # Розділяємо введений рядок за комами
  numbers_str = input_string.split(',')

  # Перевіряємо, чи отримали три елементи
  if len(numbers_str) != 3:
    return False

  # Перетворюємо кожен елемент на число і перевіряємо, чи він невід'ємний
  try:
    numbers = [float(num) for num in numbers_str]
    return all(num > 0 for num in numbers)
  except Exception as e:
    logging.error(f"{timestamp_prefix} Виникла помилка: {str(e)}")
    return False

def check_Pythagorean_trykutnyk(input_string):
  input_string = input_string.strip()
  numbers_str = input_string.split(',')
  numbers = [float(num) for num in numbers_str]
  numbers.sort(reverse=True)
  c, a, b = numbers # c - гіпотенуза
  return a**2 + b**2 == c**2

print("Порограма, яка приймає масив несортованих чисел і поверне boolean значення залежно від того,чи можна із заданих значень скласти піфагорів трикутник з відповідними довжинами сторін")

# Отримуємо введення від користувача
x = input("Введіть 3 числа через кому: ")

# Викликаємо функцію для перевірки
if check_numbers(x):
  print(check_Pythagorean_trykutnyk(x))
else:
  print("Некоректний ввід. Будь ласка, введіть три невід'ємних числа через кому.")
