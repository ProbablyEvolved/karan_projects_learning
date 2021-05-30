import math

print('Enter the number of decimal digits to display: ')
decimalLen = int(input())

if(decimalLen < 100):

    print(f'PI value: {math.e:.{decimalLen}f}')

else:

    print('Decimal Precision too High! Terminating!')