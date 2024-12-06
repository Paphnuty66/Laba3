import re
import requests

def checkpolz(user_string):
    reg = r"\b[0-9]{3}\-[0-9]{3}\-[0-9]{3}\-[0-9]{2}\b"
    result = re.findall(reg, user_string)
    print(result)

def checkfile(user_filepath):
    with open(user_filepath, "r") as f:
        user_string=f.read()
        checkpolz(user_string)

def checkurl(user_url):
    s=requests.get(user_url)
    checkpolz(s.text)

print("Введите вашу строку: ")
print("Что будем проверять? ")
print("1-если свою строку, 2-если файл, 3-если сайт по usl:")
a=int(input())
if a == 1:
    print("Введите вашу строку: ")
    user_string = input()
    checkpolz(user_string)
if a == 2:
    print("Введите ваш путь к файлу: ")
    user_filepath = input()
    checkfile(user_filepath)
if a==3:
    print("Введите ваш url: ")
    user_url = input()
    checkurl(user_url)