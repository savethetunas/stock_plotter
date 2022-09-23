###
### Author: Adam Fehse
### Course: CSc 110
### Description: A stock plotter.

mode = '' or ''
while mode != 'horizontal' and mode != 'vertical':
    mode = input('Enter stock plotter mode:\n')

stock_string = input('Enter stock string:\n')
length = len(stock_string) % 2
while length != 0:
    stock_string = input('Enter stock string:\n')
    length = len(stock_string) % 2
print('#' * 19)

count_up = 0
count_down = 0

