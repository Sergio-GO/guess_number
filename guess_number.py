from random import randint as rnd


number = rnd(1,100)
print('Угадай число от 1 до 100')

while True:
    guess = int(input('Введите число: \n'))
    if guess < number:
        print('Ваше число меньше')
    if guess > number:
        print('Ваше число больше')
    if guess == number:
        break
print('Вы угадали!')