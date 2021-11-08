
secret_word = "giraffe"
guess = ""
i = 0


while guess != secret_word and i < 3:
    guess = input("Enter guess: ")
    i += 1

if i == 3 and guess != secret_word:
    print("Wrong!")
else:
    print("Correct!")