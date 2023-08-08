#1. Star Pattern

rows = 5

for i in range(rows, 0, -1):
    print('*' * i + ' ' * (rows - i))

#2. Star Pattern

rows = 5

for i in range(rows,0,-1):
    print(' '*(rows-i)+'*' * i)

#3. Star Pattern

rows = 5

for i in range(rows,0,-1):
    print(' '*(rows-i)+' *' * i)
