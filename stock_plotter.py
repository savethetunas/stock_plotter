###
### Author: Adam Fehse
### Course: CSc 110
### Description: A stock plotter that can print vertical or horizontal charts.

# Ensure input mode is correct input.
mode = ''
while mode != 'horizontal' and mode != 'vertical':
    mode = input('Enter stock plotter mode:\n')

# Ensure string length is multiple of two.
string = input('Enter stock plot input string:\n')
length = len(string) % 2
while length != 0:
    string = input('Enter stock plot input string:\n')
    length = len(string) % 2

if mode == 'vertical':
    print('#' * 19)
    p = 8  # Position begins at 8. Center of chart.
    i = 0
    while i < len(string):  # Loops (length of string) times.
        if string[i] == 'u':
            num = int(string[i + 1])  # Numeral from input string.
            space = p + num  # Space left of '*'.
            behind_space = 16 - p - num  # Space right of '*'.
            p = p + num  # Update position right.
            output = '#' + ' ' * space + '*' + ' ' * behind_space + '#'
            print(output)

        if string[i] == 'd':
            num = int(string[i + 1])
            space = p - num  # Space left of '*'.
            behind_space = 16 - p + num
            p = p - num  # Update position left.
            output = '#' + ' ' * space + '*' + ' ' * behind_space + '#'
            print(output)
        i += 1

    if i >= len(string):  # Print last row, exit.
        print('#' * 19)
        exit()

if mode == 'horizontal':
    length_div_two = len(string) / 2
    top = '##' + '#' * int(length_div_two) + '##'
    print(top)  # Top row.

    rows = 16  # Start with 16 rows.
    while rows >= 0:
        print('#', end=' ')  # Prints left wall, ends on the same line.
        count = 0
        level = 8  # Center of the chart. Move up and down from here.
        while count < len(string):
            if string[count] == 'u':
                level += int(string[count + 1])  # Add numeral to level.
            else:
                level -= int(string[count + 1])  # Minus numeral form level.
            if rows == level:  # Check row and level, if they are equal print star.
                print('*', end='')
            else:
                print(' ', end='')  # Print empty space. Stay on same line.
            count += 2  # Count +2 because +1 iterates to alpha char.
        output = ' ' * (int(length_div_two) - count) + " #"
        print(output)
        rows -= 1  # Subtract 1 from rows and restart loop.

    print(top)
