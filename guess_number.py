number = 7
guess = []
for guess_count in range(1,4):
    guess = int(input("Enter a guess: "))
    if guess != number:
        print("Wrong guess!!!")
        guess_count += 1
        if guess_count == 4:
            print("You have failed")
    elif guess == number:
        print("Well guessed!!!")
        break
        
