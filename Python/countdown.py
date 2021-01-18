import random
import time

def main():
    number = random.randint(5, 15)
    countdown(number)
    print("Happy New Year!")

def countdown(n):
    for i in range(10):
        print(n-i)
        time.sleep(1)
        
main ()
