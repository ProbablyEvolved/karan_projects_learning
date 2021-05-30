# Prime Factorization
# Have the user enter a number and find all Prime Factors (if there are any) and display them.
# https://github.com/karan/Projects
# 004

import math

primes = list()

num = int(input('Enter the number to prime factorize: '))
temp = num

while temp % 2 == 0:
    
    primes.append(int(2))
    temp /= 2

for i in range(3, int(math.sqrt(temp)+1), 2):

    while temp % i == 0:

        primes.append(i)
        temp /= i
    
if temp > 2:

    primes.append(int(temp))

print('The prime factors of ' + str(num) +' is as follows:\n\n')

for i in range(len(primes)):

    print(primes[i], end=' ')