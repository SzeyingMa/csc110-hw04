# ------------------------------------------------------
#        Name: Stephanie Ma
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """Ask for a sentence until a required word is found."""
    while True:
        sentence = input("Give me a sentence: ")
        # Check the secret word first.
        if secret_word in sentence:
            print("You used the secret word!")
            break
        
        # Check for dog or Dog.
        elif "dog" in sentence or "Dog" in sentence:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break

        # Ask again if none of the required words are found.
        else:
            print("Try again")
            
# Task 2
def check_greater():
    """Ask for two integers and print which one is greater."""
    while True:
        first = int(input("Give me a first integer: "))
        second = int(input("Give me a second integer: "))
        if first > second:
            print("First is Greater")
            break
        elif second > first:
            print("Second is Greater")
            break
        else:
            print("Try again")




# Task 3
def get_special_numbers():
    """Print odd multiples of 3 from 1 to 40, excluding multiples of 5."""

    for number in range(1, 41):
        # Skip even numbers.
        if number % 2 == 0:
            continue

        # Skip numbers that are not multiples of 3.
        if number % 3 != 0:
            continue

        # Skip multiples of 5.
        if number % 5 == 0:
            continue
        
        # Print numbers that satisfy all three conditions.
        print(number)

# Task 4.a
def my_for_loop():
    """Ask for a short string and classify each character as a vowel or consonant."""
    
     # Get a string from the user.
    text = input("Give me a string: ")

    # Return if the length is outside 2 to 5 or the string contains spaces.
    if len(text) < 2 or len(text) > 5 or " " in text:
        return

    # Examine each character in the string.
    vowels = "aeiouAEIOU"
    for letter in text:
        if letter in vowels:
            print(f"{letter} is a vowel")
        else:
            print(f"{letter} is a consonant")


# Task 4.b
def my_while_loop():
    """Display a menu repeatedly until the user chooses b or c."""
    while True:
        choice = input("Choose one option: a, b, or c: ")

        if choice == "a":
            continue
        elif choice == "b":
            print("Goodbye")
            return
        elif choice == "c":
            sys.exit()
        else:
            print("try again")


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
