from random import randint

def random_list(a, b, c):
    t = [randint(a, b) for i in range(c)]
    print(t)

a = int(input("Вкажіть початок діапазону:"))
b = int(input("Вкажіть кінець діапазону:"))
c = int(input("кількість елементів:"))

random_list(int(a), int(b), int(c))
