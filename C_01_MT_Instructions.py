# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instruction():
    print('''

**** Kori's Math Test Instructions ****

To start, customise the amount of equations that you want or 
go with the default choice of 10 equations

Then choose how many rounds you'd like to play <enter> for 
infinite mode.

Your goal is to correctly answer the Equations without 
running out of attempts.

 Good luck.   

    ''')


# Main routine
print()
print("🔢🔢🔢 Welcome to the Math Test! 📐📐📐")
print()

# loop for testing purposes

want_instructions = yes_no("Would you like to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
