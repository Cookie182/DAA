import sys
import time

import numpy as np

# increasing recursion limit to prevent any potential limits
sys.setrecursionlimit(10**9)

###############################################################################################################################################
""" Question 1 - Number of queens with backtracking """
print('LAB-4 DAA')
print('QUESTION 1\n')


def valid_input():  # getting valid input
    while True:
        try:
            num = int(input('Enter chessboard size: '))
            break
        except:
            print('Enter a valid integer!\n')
            continue
    return num


def can_attack(x, y):  # support function
    # checking if more than 1 queen in row and column
    for k in range(num):
        if chessboard[x][k] == 'Q' or chessboard[k][y] == 'Q':
            return True
    # checking diagonally
    for k in range(num):
        for l in range(num):
            if (k + l == x + y) or (k - l == x - y):
                if chessboard[k][l] == 'Q':
                    return True
    return False


def num_queen(n):  # main fucntion
    # sanity check
    if n == 0:
        return True
    for x in range(num):
        for y in range(num):
            # to check if a queen can be placed without being attacked
            if not can_attack(x, y) and chessboard[x][y] != 'Q':
                chessboard[x][y] = 'Q'
                # to check if a queen can be placed
                if num_queen(n - 1) == True:
                    return True
                chessboard[x][y] = 'X'
    return False


def print_chessboard():  # pretty printing the chess board
    for x in chessboard:
        print(*x)


def count_queens():  # counting the queens that are on the board
    Q_count = 0
    for x in chessboard:
        Q_count += x.count('Q')
    print('{} queens can be placed on the board'.format(Q_count))


for num in range(2, 10):  # loop to print chessboard for N values of 2 - 9
    chessboard = [['X'] * num for _ in range(num)]  # making the chessboard
    tic = time.time()  # calculating time for each N value
    num_queen(num)
    toc = time.time()
    print('For N = {}: '.format(num))
    count_queens()  # counting queens
    print_chessboard()  # to pretty printing chessboard
    print('Time to solve: {}s'.format(f"{toc - tic:0.6f}"))
    if num != 9:  # checkpoint except for last N value
        print('Going to the next N value...\n')
        time.sleep(1)


# to ask user if they want to try problem with custom N value
response = input('\nDo you want to try with a custom N value?[Y]: ')
if response.upper() == 'Y':
    num = valid_input()
    chessboard = [['X'] * num for _ in range(num)]
    tic = time.time()
    num_queen(num)
    toc = time.time()
    print('For N = {}: '.format(num))
    count_queens()
    print_chessboard()
    print('Time to solve: {}s'.format(f"{toc - tic:0.6f}"))
else:
    print('N')

_ = input('Press anything to continue...')
###############################################################################################################################################
""" Question 2 - Sudoku via backtracking """
print('\nQUESTION 2\n')

# question sudoku table (0 denotes empty boxes)
table = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
         [2, 8, 9, 0, 0, 4, 0, 0, 0],
         [3, 4, 6, 2, 0, 5, 0, 9, 0],
         [6, 0, 2, 0, 0, 0, 0, 1, 0],
         [0, 3, 8, 0, 0, 6, 0, 4, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 7, 8],
         [7, 0, 3, 4, 0, 0, 5, 6, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]


backtrack_count = 0


def complete(table):

    global backtrack_count  # global - to access outer scope variable
    backtrack_count += 1
    find = find_empty(table)
    if not find:  # to check if the table is complete (base case)
        return True
    else:
        row, col = find

    for x in range(1, 10):  # adding numbers to the board if they meet the sudoku criteria
        if valid_num(table, x, (row, col)):
            table[row][col] = x

            # recursively solve the table until fully complete with no more empty boxes
            if complete(table):
                return True

            table[row][col] = 0  # backtracks to reset the last changed element

    return False


def valid_num(table, num, pos):  # to check if a number satisfies the normal sudoku rules
    # checking the row
    for x in range(len(table[0])):
        # checking each row and a measure to prevent rechecking of recently entered boxes
        if table[pos[0]][x] == num and pos[1] != x:
            return False

    # checking the column
    for x in range(len(table)):
        # same procedure, but for the column of table
        if table[x][pos[1]] == num and pos[0] != x:
            return False

    # checking within respective box, used integer division to seperate table into mini even boxes
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # to go into respective boxes
    # to check which column (box length) to respond to
    for x in range(box_y * 3, box_y * 3 + 3):
        for y in range(box_x * 3, box_x * 3 + 3):  # same as above but for row
            # to check if element we add meets the sudoku rules
            if table[x][y] == num and (x, y) != pos:
                return False

    return True


def print_table(table):  # pretty printing the table
    for x in range(len(table)):
        if x % 3 == 0 and x != 0:  # row seperator
            print("- - - - - - - - - - -")

        for y in range(len(table[0])):
            if y % 3 == 0 and y != 0:
                print("| ", end="")  # column seperator

            if y == 8:
                print(table[x][y])
            else:
                print(str(table[x][y]) + " ", end="")


def find_empty(table):  # finding empty boxes in table
    for x in range(len(table)):
        for y in range(len(table[0])):
            if table[x][y] == 0:
                return (x, y)  # row, column of empty box

    return None  # when function can't find empty box


# printing results
print('Before: ')
print_table(table)
time.sleep(1)
print("_____________________")
print('After: ')
print_table(table)
print('Number of backtracks = {}\n'.format(backtrack_count))
_ = input('Press anything to continue...')
###############################################################################################################################################
""" Question 3 - Candidates and target """
print('\nQUESTION 3\n')

comb_count = 0


def comb_sum(combinations, target):  # main func
    recursive_sum(combinations, target, 0, [])  # starting entries
    return


def recursive_sum(combinations, target, index, sub_lists):
    if target == 0:  # security check
        print(*sub_lists)
        return

    if target < 0:  # security check
        return

    for x in range(index, len(combinations)):
        # adds all possible combinations to the sub list
        sub_lists.append(combinations[x])
        # recursively calls function with new  for each comb in sub list
        recursive_sum(combinations, target - combinations[x], x, sub_lists)
        global comb_count
        comb_count += 1  # counter for total combinations
        # removes any other combination that has the same target in list
        sub_lists.remove(combinations[x])


while True:
    try:
        # getting valid list of numbers from user, turning into list of unique numbers
        candidates = np.unique([int(x) for x in input(
            'Enter spaced out numbers to compute: ').split()])
        target = int(input('Enter target value: '))  # valid target value
        break
    except:
        print('Enter valid input!\n')
        continue

print('\nCandidates =', *candidates)
print('Target = {}'.format(target))
print('Unique Combinations: ')
comb_sum(candidates, target)
print('Total combinations = {}'.format(comb_count))
###############################################################################################################################################
