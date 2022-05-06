
import random

def intcheck():
    while True:
        try:
            i = int(input())
        except ValueError:
            print("Incorrect format")
        else:
            return i

def r(diff):
    it = 0
    mark = 0
    while it < 5:
        if diff == 1:
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            cha = random.choice(['+', '*', '-'])    
            if cha == '*':
                print(a, '*', b)
                i = intcheck()
                if i == a * b:
                    print("Right")
                    mark += 1
                else:
                    print("Wrong")
            if cha == '+':
                print(a, '+', b)
                i = intcheck()
                if i == a + b:
                    print("Right")
                    mark += 1
                else:
                    print("Wrong")
            if cha == '-':
                print(a, '-', b)
                i = intcheck()
                if i == a - b:
                    print("Right")
                    mark += 1
                else:
                    print("Wrong")        
        else:
            a = random.randint(11, 29)
            print(f"{a}")
            gh = intcheck()
            if a ** 2 == gh:
                print("Right")
                mark += 1
            else:
                print("Wrong")
        it += 1

    print (f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
    a = input().lower()
    if diff == 1:
        desc = "simple operations with numbers 2-9"
    else:
        desc = "square operations with numbers 11-29"
    if a == "yes" or a == "y":
        print('What is your name?')
        name = input()
        f = open("results.txt", 'a', encoding='utf-8')
        f.write(f"{name}: {mark}/5 in level {diff} ({desc})." + "\n")
        f.close()
        print("The results are saved in \"results.txt\".")

if __name__ == "__main__":
    print("Which level do you want? Enter a number:", "1 - simple operations with numbers 2-9", "2 - integral squares of 11-29", sep="\n")
    r(int(input()))
