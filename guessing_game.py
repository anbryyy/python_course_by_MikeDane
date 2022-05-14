secret_word = "mama"
guess = ""
attempt_counter = 1
guess_limit = 3
no_more_attempts = False

while guess != secret_word and not(no_more_attempts):
    if attempt_counter <= guess_limit:
        guess = input("Enter the word: ")
        attempt_counter += 1
    else:
        no_more_attempts = True

if no_more_attempts:
    print("You lose!")
else:
    print("YOU WIN!")




