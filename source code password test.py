RUNTIME = True
while RUNTIME:
    from colorama import Fore, Style


    def length(password):
        check = len(password)
        if check >= 8:
            return True
        else:
            return False


    def upper(password):
        flag = True
        Upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in password:
            if i in Upper:
                flag = True
                break
            else:
                flag = False
        return flag


    def lower(password):
        Lower = "abcdefghijklmnopqrstuvwxyz"
        flag = True
        for i in password:
            if i in Lower:
                flag = True
                break
            else:
                flag = False
        return flag


    def character(password):
        Character = '!@#$%^&*()_+=-{}[]|:;"<>,.?//*-~ '
        flag = True
        for i in password:
            if i in Character:
                flag = True
                break
            else:
                flag = False
        return flag


    def number(password):
        Number = '1234567890'
        flag = True
        flag = True
        for i in password:
            if i in Number:
                flag = True
                break
            else:
                flag = False
        return flag


    def result(a, b, c, d, e):
        if a == True:
            print(Fore.GREEN + "Length test True")
        else:
            print(Fore.RED + "Length test False")
        if b == True:
            print(Fore.GREEN + "Upper case True")
        else:
            print(Fore.RED + "Upper case False")
        if c == True:
            print(Fore.GREEN + "Lower case True")
        else:
            print(Fore.RED + "Lower case False")
        if d == True:
            print(Fore.GREEN + "Character test True")
        else:
            print(Fore.RED + "Character test False")
        if e == True:
            print(Fore.GREEN + "Number test True")
        else:
            print(Fore.RED + "Number test False")
        if a == True and b == True and c == True and d == True and e == True:
            print(Fore.GREEN + "Password meets all standards ! ")
        else:
            print(Fore.RED + "Password doesnot meet all standards ! :( ")

        print(Style.RESET_ALL)
        print("Thank You For Using \n"
              "CODED BY ISHMAM")


    password = input("Enter your password: ")
    pass_length = length(password)
    pass_upper = upper(password)
    pass_lower = lower(password)
    pass_character = character(password)
    pass_number = number(password)
    result(pass_length, pass_upper, pass_lower, pass_character, pass_number)
    CHECK = input("WANT TO TEST ANOTHER PASSWORD ?(Y/N):  ")
    if CHECK.upper()[0] == 'Y':
        RUNTIME =True
    else:
        RUNTIME = False
