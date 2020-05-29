# Recursive implementation.

# Participants can solve it differently not by necessarily using recursion

def print_digits(num):
    # Recursively call print_digits until the number is <10 and then execute the pending prints which had to be executed.
    if num < 10:
        print(num)
    else:
        print_digits(num // 10)
        print(num % 10)

n = int(input())

print_digits(n)
