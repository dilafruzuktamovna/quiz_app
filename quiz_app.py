questions = ("What is the purpose of indentation in Python? ",
             "What is the output of the following code snippet: print(2 + 3 * 4)? ",
             "What is the correct way to declare a variable in Python? ",
             "What is the purpose of the if statement in Python? ",
             "Which of the following is a valid Python comment? ",
             "How do you convert a string to an integer in Python? ",
             "What is the output of the following code snippet: print(list(range(3, 8, 2)))? ",
             "What does the len() function do in Python? ",
             "How do you define a function in Python? ",
             "What is the purpose of the for loop in Python? ")

options = (
           ("A: It helps define the structure and scope of code blocks ",  "B: It is used to improve code readability. ", "C: It is a requirement for Python syntax ",  "D: It has no impact on the execution of the code.  "),
           ("A: 16", "B: 20", "C: 9", "D: 14"),
           ("A: 'variable = value'", "B:'value = variable'", "C: 'variable(value)'", "D: 'value(variable)'"),
           ("A: It is used for loop iterations.", "B: It is used to define functions.", "C: It is used to perform arithmetic operations.", "D: It is used for conditional execution of code."),
           ("A: /* This is a comment */", "B: # This is a comment", "C: // This is a comment", "D: <!-- This is a comment -->"),
           ("A: str_to_int()", "B: to_integer()", "C: int()", "D: string_to_int()"),
           ("A: [3, 5, 7]", "B: [2, 4, 6], ""C: [3, 6, 9]", "D: [2, 5, 8]"),
           ("A: It returns the length of a list.", "B: It returns the length of a string.", "C: It returns the length of a dictionary.", "D: It returns the length of an integer."),
           ("A: def function_name():", "B: function function_name():", "C: define function_name():", "D: function_name():"),
           ("A1: It is used to read user input.", "B: It is used to iterate over a sequence of elements.", "C: It is used to declare variables.", "D: It is used to perform mathematical calculations.")
)

answers = ("B", "D", "A", "D", "C", "C", "A", "B", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    # guess = input()
    # question_num += 1

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f'{answers[question_num]} is the correct answer.')

    question_num += 1

print("----------------------------")
print("           results          ")
print("----------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

score = score / len(questions) * 100
print(f"Your score is: {score}%")



