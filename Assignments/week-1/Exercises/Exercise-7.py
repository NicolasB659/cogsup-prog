"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

def input_feedback(prompt):
    """
    Ask the user for feedback on the guess.
    Expected answers:
    - 'h' if the guess is too high,
    - 'l' if the guess is too low,
    - 'c' if the guess is correct.
    Keeps asking until valid input is received.
    """
    while True:
        response = input(prompt).lower()
        if response in ('h', 'l', 'c'):
            return response
        print("Please enter 'h' (too high), 'l' (too low), or 'c' (correct).")

def computer_guesses():
    """
    Computer tries to guess the number you are thinking of by binary search.
    It narrows down the range after each guess based on your feedback.
    """
    low = 1            # Lower bound of search range (initially 1)
    high = 100         # Upper bound of search range (initially 100)
    guesses = 0        # Count of attempts made by the computer

    print("Think of a number between 1 and 100, and I will try to guess it.")

    while low <= high:
        # Computer guesses the midpoint of the current range
        guess = (low + high) // 2
        guesses += 1

        # Ask the user for feedback about the guess
        feedback = input_feedback(f"My guess is {guess}. Is it too high (h), too low (l), or correct (c)? ")

        if feedback == 'c':
            # The guess was correct: end the game
            print(f"I found your number {guess} in {guesses} guesses!")
            return
        elif feedback == 'h':
            # Guess was too high: adjust the upper bound to be just below guess
            high = guess - 1
        else:  # feedback == 'l'
            # Guess was too low: adjust the lower bound to be just above guess
            low = guess + 1

    # If the loop ends, it means the feedback was inconsistent or number is out of range
    print("Hmm, something went wrong. Are you sure you thought of a number between 1 and 100 and gave correct feedback?")

if __name__ == "__main__":
    computer_guesses()