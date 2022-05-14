secret_word = "lama"
guess = ""
attempt_counter = 1
no_more_attempt = False
guess_limit = ""
level = input("Enter difficulty level 1, 2 or 3: ")

if level == "1":
    guess_limit = 7
elif level == "2":
    guess_limit = 5
elif level == "3":
    guess = 3
elif level != '1' or level != '2' or level != '3':
    print("Invalid value. You must enter only the numbers 1, 2 or 3.")
    guess_limit = int(input("Enter difficulty level 1, 2 or 3: "))

while guess != secret_word and not(no_more_attempt):
    if attempt_counter <= guess_limit:
        guess = input("Enter the word: ")
        attempt_counter += 1
    else:
        no_more_attempt = True

if no_more_attempt:
    print("You lose!")
else:
    print("You win!")

