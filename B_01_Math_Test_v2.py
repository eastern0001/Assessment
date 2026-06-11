import random


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instruction():
    print('''

**** Instructions ****

To begin, choose the number of questions you want and if you 
would like to customize the difficulty then choose your 
own parameters or else go with the default settings
(The numbers used will be between 1 and 20).

Choose how many questions you'd like to attempt, or press
<enter> for infinite questions mode.

You have ONE attempt per question — think carefully before answering!

Type 'quit' at any time to exit the test.

Good luck!.

    ''')


# checks for an integer with optional upper / lower limits and an optional exit code
def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for continuous mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# generate a random +, -, or x Question
def generate_equation(low, high):
    eq_type = random.randint(1, 3)

    if eq_type == 1:
        # addition:  a + b = ?
        a = random.randint(low, high)
        b = random.randint(low, high)
        answer = a + b
        equation = f"{a} + {b} = ?"

    elif eq_type == 2:
        # subtraction:  a - b = ?
        a = random.randint(low, high)
        b = random.randint(low, a)
        answer = a - b
        equation = f"{a} - {b} = ?"

    else:
        # multiplication:  a x b = ?
        a = random.randint(low, min(high, 12))
        b = random.randint(low, min(high, 12))
        answer = a * b
        equation = f"{a} x {b} = ?"

    return equation, answer


# Initialise math test variables
mode = "regular"
questions_attempted = 0
end_test = "no"
feedback = ""

test_history = []
num_correct = 0

print("📐📐📐 Welcome to the Math Test ✏️✏️✏️")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

# Ask user for number of questions or continuous mode
num_questions = int_check("Number of questions <enter for continuous mode>: ",
                          low=1, exit_code="")

if num_questions == "":
    mode = "continuous"
    num_questions = 5

# ask user if they want to use default difficulty parameters
default_params = yes_no("Do you want to use the default difficulty parameters? ")
if default_params == "yes":
    low_num = 1
    high_num = 20

# allow user to set the number range for the questions
else:
    low_num = int_check("Minimum number to use in questions? ", low=0)
    high_num = int_check("Maximum number to use in questions? ", low=low_num + 1)

# Test loop starts here
while questions_attempted < num_questions:

    # Question heading
    if mode == "continuous":
        question_heading = f"\n♾♾♾ Question {questions_attempted + 1} (Continuous Mode) ♾♾♾"
    else:
        question_heading = f"\n📝📝📝 Question {questions_attempted + 1} of {num_questions} 📝📝📝"

    print(question_heading)

    # Generate equation and it's correct answer
    equation, secret = generate_equation(low_num, high_num)

    print(f"\n  {equation}")
    print("You have 1 attempt — make it count!\n")

    # Asks the user to submit their answer
    answer = int_check("Answer = ", exit_code="quit")

    # check if they want to exit the test
    if answer == "quit":
        end_test = "yes"
        break

    # provide feedback based on the single submission
    if answer == secret:
        feedback = "✅✅ Correct! Well done! ✅✅"
        num_correct += 1
    else:
        feedback = f"❌ Incorrect. The correct answer was {secret}."

    print(feedback)
    print()

    questions_attempted += 1

    history_feedback = f"Q{questions_attempted} [{equation}]:  {feedback}"
    test_history.append(history_feedback)  # record result in test history

    # if in continuous mode, increase the question count
    if mode == "continuous":
        num_questions += 1

# Test loop ends here

if questions_attempted > 0:  # check the user has completed at least one question

    # Output the results
    print("\n📊📊📊 Test Results 📊📊📊")
    print(f"Questions Attempted: {questions_attempted} | "
          f"Correct: {num_correct} | "
          f"Incorrect: {questions_attempted - num_correct} | "
          f"Score: {num_correct / questions_attempted * 100:.1f}%")
    print()

    # Display the test history on request
    see_history = yes_no("Do you want to review your full test history? ")
    if see_history == "yes":
        for item in test_history:
            print(item)

# if the user exited without completing any questions
else:
    print("📋📋📋 No questions were completed. The test was exited before any answers were submitted. 📋📋📋")
