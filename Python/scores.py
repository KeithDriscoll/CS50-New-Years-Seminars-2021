def main():
    score1 = int(input("Score: "))
    score2 = int(input("Score: "))
    score3 = int(input("Score: "))
    
    print_scores(score1)
    print_scores(score2)
    print_scores(score3)

def print_scores(score):
    for i in range(score):
        print("#", end="")
    print()

main()