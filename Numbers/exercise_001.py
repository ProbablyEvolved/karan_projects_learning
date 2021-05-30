# Find PI to the Nth Digit
# Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
# https://github.com/karan/Projects
# 001

print('Enter the number of decimal digits to display: ')
decimalLen = int(input())

if(decimalLen < 100):

    pi = float(22/7)
    print(f'PI value: {pi:.{decimalLen}f}')

else:

    print('Decimal Precision too High! Terminating!')