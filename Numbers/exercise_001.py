# Find PI to the Nth Digit
# https://github.com/karan/Projects#numbers
# 

print('Enter the number of decimal digits to display: ')
decimalLen = int(input())

if(decimalLen < 100):

    pi = float(22/7)
    print(f'PI value: {pi:.{decimalLen}f}')

else:

    print('Decimal Precision too High! Terminating!')