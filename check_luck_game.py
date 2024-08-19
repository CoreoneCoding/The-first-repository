# Это игра, которая проверяет удачу пользователя и называется "Игра удачи"./This is a game, which can check user's luck and it's name is "A luck game".

import random

def game_in_russian_langiage():
    """Игра на русском языке."""
    print("Привет! Я - программа, которая проверит твою удачу. Я выберу рандомно три числа от 0 до 3, и если они совпадут - выйграл и ты удачный человек.")
    random_number1 = random.randint(0, 3)
    random_number2 = random.randint(0, 3)
    random_number3 = random.randint(0, 3)
    if random_number1 == random_number2 and random_number1 == random_number3:
        print(f"Ура, победа! Все три числа равны. Числа: {random_number1}, {random_number2}, {random_number3}.")
    else:
        print(f"Увы, но ты проиграл! (( Все три числа к сожалению не равны.. Числа: {random_number1}, {random_number2}, {random_number3}.")
    print("Программа завершена. Нажми 'Enter', чтобы выйти из неё.")

def game_in_english_language():
    """A game in english language."""
    print("Hi! I'm game, which can check your luck. I will choose randomly a number from 0 to 3 and if all three numbers is simmilar, you'll win.")
    random_number1 = random.randint(0, 3)
    random_number2 = random.randint(0, 3)
    random_number3 = random.randint(0, 3)
    if random_number1 == random_number2 and random_number1 == random_number3:
        print(f"Congratulations! It is win! All three numbers is simmilar. Numbers: {random_number1}, {random_number2}, {random_number3}.")
    else:
        print(f"Oops, sorry, but it is loss.. (( Unfortunately not all numbers is simmilar.. Numbers: {random_number1}, {random_number2}, {random_number3}.")
    print("Program is finished. Press 'Enter' to exit.")

print("Выбери свой язык и введи его цыфру ниже / choose your language and type it's number below (1 - русский, 2 - english).")
user_language_choose = input("Твой выбор / your choice: ")

if user_language_choose == "1":
    game_in_russian_langiage()
if user_language_choose == "2g":
    game_in_english_language()

# Завершение и цикл программы/Stopping program and it's loop.
input()