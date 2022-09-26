###
### Author: Adam Fehse
### Course: CSc 110
### Description: A stock plotter.

mode = ''
while mode != 'horizontal' and mode != 'vertical':
    mode = input('Enter stock plotter mode:\n')

string = input('Enter stock plot input string:\n')
length = len(string) % 2
while length != 0:
    stock_string = input('Enter stock plot input string:\n')
    length = len(string) % 2

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
    if i >= len(string):
        print('#' * 19)
        exit()



