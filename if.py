b = print("happy_message")
a = print("sad_message")
print("not_so_sad_message")
c = print("message_about_equality")
happy_message = int(input("the cat is happy "))
sad_message = int(input("the cat is dead"))
not_so_sad_message = int(input("the cat is sad"))
message_about_equality = int(input("dog can not operate MRI machines, but catscan"))
if a > b :
    print("sad_message")
if b > a and b > c:
    print("happy_message")
else: print("not_so_happy_message")
if a == b:
    print("message_about_equality")