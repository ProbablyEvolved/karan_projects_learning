# Find e to the Nth digit
# Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
# https://github.com/karan/Projects
# 002

import math

print('Enter the number of decimal digits to display: ')
decimalLen = int(input())

if(decimalLen < 100):

    print(f'PI value: {math.e:.{decimalLen}f}')

else:

    print('Decimal Precision too High! Terminating!')