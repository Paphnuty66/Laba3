import re
import requests

def checkpolz(user_string):
    reg = r"\b[0-9]{3}\-[0-9]{3}\-[0-9]{3}\ [0-9]{2}\b"
    result = re.findall(reg, user_string)
    if not result:
        return "Коректных снилсов нет"
    else:
        return result

def checkfile(user_filepath):
    try:
        with open(user_filepath, "r") as f:
            user_string = f.read()
            return checkpolz(user_string)
    except Exception as e:
        return "Ошибка при работе с файлом"

def checkurl(user_url):
    try:
        s = requests.get(user_url)
        return checkpolz(s.text)
    except Exception as e:
        return "Ошибка при работе с сайтом"


print("Что будем проверять? ")
print("1-если свою строку, 2-если файл, 3-если сайт по url, 4-Выход")
a = 0
while a != 4:
    a = int(input())
    if a == 1:
        print("Введите вашу строку: ")
        user_string = input()
        otvet = checkpolz(user_string)
        print(otvet)
    if a == 2:
        print("Введите ваш путь к файлу: ")
        user_filepath = input()
        otvet = checkfile(user_filepath)
        print(otvet)
    if a == 3:
        print("Введите ваш url: ")
        user_url = input()
        otvet = checkurl(user_url)
        print(otvet)

