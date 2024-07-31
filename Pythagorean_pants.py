# Yurii Zosia
import logging

# Конфігурація логування
#Можливі значення: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(filename='Pythagorean_pants.log', level=logging.DEBUG)
logging.info('Програма запущена!')

# Використання логування
#logging.debug('Це повідомлення для відлагодження')
#logging.info('Інформаційне повідомлення')
#logging.warning('Попередження')
#logging.error('Помилка')
#ogging.critical('Критична помилка')

try:
    print("Вітання Юрій!")
    x = int(input("Введіть число: "))
    print(10 / x)
except Exception as e:
    logging.error(f"Виникла помилка: {str(e)}")
    print("Сталася помилка. Дивіться лог для деталей.")