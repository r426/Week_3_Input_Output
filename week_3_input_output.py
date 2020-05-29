numberOfMarks = 3
marks = []
name = input('Enter your name:')

for i in range(numberOfMarks):
    enteredMark = -1
    while enteredMark < 0 or enteredMark > 100:
        userInput = input('Enter a mark:')
        if userInput.isnumeric():
            enteredMark = int(userInput)
            if enteredMark > 100:
                print("Input error.")
        else: print("Input error.")
    marks.append(enteredMark)
print('{}, your marks are {}'.format(name, marks))