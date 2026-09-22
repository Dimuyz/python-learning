#opt gen

import time
import random

while True:
    print("========== OTP GENERATOR ==========\n")
    print("do you want to generate an otp?")
    print("yes/no")
    answer = input("answer: ").lower()
    if answer == "yes":
        print("ok, its processing")
        time.sleep(3)
        kkb = random.randint(1000000, 9999999)
        print(f"hello, your otp today is: {kkb}")
        print("do you want to continue making otp? (yes/no)")
        answer = input("answer: ").lower()
        if answer == "yes":
            print("ok lets go to the main menu")
            continue
        elif answer == "no":
            print("ok thanks for using my program")
            break
        else:
            print("sorry command is not valid")
            break
    elif answer == "no":
        print("are you sure about ur opinion? (yes/no)")
        answer = input("answer: ")
        if answer == "yes":
            print("ok thanks for using my program-!")
            break
        elif answer == "no":
            print("ok lets head back to main menu")
            continue
        else:
            print("sorry command is not valid")
            break
    else:
        print("sorry the command isn`t valid")
        break

