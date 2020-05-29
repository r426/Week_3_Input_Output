enteredNumber = -1
digits = []

while enteredNumber < 0 or enteredNumber > 10000:
    userInput = input('Please enter a non-negative integer number <= 10000:')
    if userInput.isnumeric():
        enteredNumber = int(userInput)
        if enteredNumber > 10000:
            print("Input error.")
    else: print("Input error.")

digitsLeft = True
tempNumber = enteredNumber

while digitsLeft:
    digits.append(tempNumber % 10)
    tempNumber //= 10
    digitsLeft = tempNumber

for x in digits[::-1]: print(x)