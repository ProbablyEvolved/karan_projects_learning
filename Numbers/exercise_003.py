# Fibonacci Sequence
# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
# https://github.com/karan/Projects#numbers
# 003

prev = 0
now = 1
next = int()

sequence = list()

sequence.append(prev)
sequence.append(now)

num = int(input('Enter the number of digits of Fibonacci sequence to be printed: '))

for i in range(2, num):

    next = prev + now
    prev = now
    now = next

    sequence.append(next)

for i in range(num):

    print(sequence[i], end=' ')