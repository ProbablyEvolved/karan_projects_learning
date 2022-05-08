# Next Prime Number
# Have the program find prime numbers until the user chooses to stop asking for the next one.
# https://github.com/karan/Projects
# 005

choice = ''
counter = 1

while True:

    i = 1

    while True:

        if counter % i == 0:

            if i != 1 and i != counter:

                counter += 1
                i = 1

            elif i == counter:

                print("Prime Number: ", counter, '\n')
                counter += 1
                break

            else:

                i += 1

        else:

            i += 1

    print("Do you want to continue? (y/n): ", end='')
    choice = input()

    if choice.lower() == 'y' or choice.lower() == 'yes':

        print()

    elif choice.lower() == 'n' or choice.lower() == 'no':

        print('Exiting!')
        break

    else:

        print('Invalid Input!')