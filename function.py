def good_morning_kittens():
    print("Good morning, kittens!")
def concatenation():
    a = input("enter first defenition")
    b = input("enter second defenition")
    c = input("enter third defenition")
    print(a+b+c)
def if_elif():
    a = int(input("enter number A:"))
    b = int(input("enter number B:"))
    c = int(input("enter number C:"))
    if b < a:
        print("the cat is dead")
    elif a == b:
        print("dog can not operate MRI machines, but catscan")
    elif a < b:
        print("the cat is happy")
    elif b <= c:
        print("the cat is not dead")
def cycle_while():
    a = int(input("enter number A:"))
    b = int(input("enter number B:"))
    c = int(input("enter number C:"))
    d = "dog can not operate MRI machines, but catscan:"
    while b > a:
        print("bad result")
        a += c
        d += ' ' + str(a)
    print("Good job")
    print(d)

