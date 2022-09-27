###
### Author: Adam Fehse
### Course: CSc 110
### Description: A stock plotter. Can print vertical or horizontal modes.

# This checks for and repeats until correct input.
mode = ''
while mode != 'horizontal' and mode != 'vertical':
    mode = input('Enter stock plotter mode:\n')

# Checks to ensure string is correct length>.
string = input('Enter stock plot input string:\n')
length = len(string) % 2
while length != 0:
    stock_string = input('Enter stock plot input string:\n')
    length = len(string) % 2

#Sets the starting position.
#On u's/d's prints spaces and location based on string.
#Position 8 is the middle of the chart and the numerals [i + 1] tell how many spaces
#to moves.
if mode == 'vertical':
    print('#' * 19)
    i = 0
    position = 8
    while i < len(string):
        if string[i] == 'u':
            print('#' + ' ' * (position + (int(string[i + 1]))) + '*' + ' ' * (
                    16 - position - (int(string[i + 1]))) + '#')
            position = position + (int(string[i + 1]))
        if string[i] == 'd':
            print('#' + ' ' * (position - (int(string[i + 1]))) + '*' + ' ' * (
                    16 - position + (int(string[i + 1]))) + '#')
            position = position - (int(string[i + 1]))
        i += 1
    if i >= len(string): # if i ever >= than length of the string, print # * 19 and exit.
        print('#' * 19)
        exit()

if mode == 'horizontal':
    length_div_two = len(string) / 2

    print('##' + '#' * int(length_div_two) + '##')
    rows = 16 #count backwards from 16
    while rows >= 0:
        print('#', end=' ')  # Print one '#', stay on the row.
        to_print = ""
        count = 0
        level = 8
        while count < len(string):
            if string[count] == 'u':
                level += int(string[count + 1])
            else:
                level -= int(string[count + 1])
            if rows == level:
                print('*', end='')
            else:
                print(' ', end='')

            count += 2

        to_print += ' ' * (int(length_div_two) - count) + " #"

        print(to_print)
        rows -= 1

    print('##' + '#' * int(length_div_two) + '##')



