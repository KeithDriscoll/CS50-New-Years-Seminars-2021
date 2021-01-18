def main():

    x = int(input("Enter number "))

    for y in range(x):
        blocklayer(x)

def blocklayer(x):
    for i in range(x):
        print("#", end="")
    print()
    
main()