```python
import sys
import time

import pandas as pd
from matplotlib import pyplot as plt

# increasing recursion limit to avoid any possible errors related to it
sys.setrecursionlimit(10**9)


def valid_int():  # to get valid int input
    while True:
        num = input('Enter an integer for n: ')
        if num.isdigit():  # checks if input is a positive digit (0 or more)
            num = int(num)  # if so, changes input to an int
            break
        else:
            print('Enter a valid integer!\n')
            continue

    return num


def valid_str():  # to get valid string input
    while True:
        str1 = input('Enter the first string: ')
        str2 = input('Enter the second string: ')
        if str1.isalpha() and str2.isalpha():  # checks if both inputs only contains alphabets
            break
        else:
            print('Enter valid strings!\n')
            continue

    return str1, str2  # returns both strings in a set


# %%


""" Question 1.A - Fibonacci - Brute force approach """


print('LAB-5 DAA')
print('Question 1 - Fibonacci series')

bf_count = 0  # to count how many times the brute force function gets called


def fibonacci_bf(num):
    if num <= 1:  # case when we find the fibonacci
        return num
    global bf_count
    bf_count += 1  # counter
    # recursively calling the function
    return fibonacci_bf(num - 2) + fibonacci_bf(num - 1)


# %%
""" Question 1.B - Fibonacci - Dynamic Programming and Memoization approach """


def fibonacci_dp(num, show):  # dynamic programming function
    tic = time.time()
    # outputs the n value's fibonacci number from the dictionary
    n = "{:,}".format(fibonacci_mem(num, dict()))
    if show == True:
        print('Fibonacci {0} = {1}'.format(num, n))
    toc = time.time()
    return f"{toc - tic:0.6f}"


def fibonacci_mem(num, mem_dict):  # memoization function
    if num in mem_dict:
        # returns the fibonacci value of n if already calculated
        return mem_dict[num]

    if num in [0, 1]:
        mem_dict[num] = num  # trivial cases

    else:
        # if the n value and it's fibonacci number hasn't already been calculated, this calculates it and places it in the dictionary
        mem_dict[num] = fibonacci_mem(
            num - 1, mem_dict) + fibonacci_mem(num - 2, mem_dict)
    return mem_dict[num]  # returns the fibnacci value that corresponds to n


# %%
""" Question 1.C - Fibonacci - Bottom Up approach (and space optimized) """


def fibonacci_botup(num, show):
    nums = [0, 1]
    tic = time.time()
    if num in nums:  # trivial cases
        return num

    # this loop gets the next fibonacci number while removing the first value in the list
    for x in range(num - 1):
        nums.append(nums[-1] + nums[-2])  # getting next fibonacci
        nums.pop(0)  # to keep list size constant
    toc = time.time()

    n = "{:,}".format(nums[-1])
    if show == True:
        print('Fibonnaci  {0} = {1}'.format(num, n))
    return f"{toc - tic: 0.6f}"


# %%
num = valid_int()  # getting valid input

# printing out the values from all the approaches when calculating fibonacci
print('\nBrute Force approach - ')
tic = time.time()
print('Fibonacci {0} = {1}'.format(num, "{:,}".format(
    fibonacci_bf(num))))  # Brute force solution
toc = time.time()
bf_time = f"{toc - tic:0.6f}"
print('Time taken to get Fibonacci number: {} s'.format(bf_time))
print('The function was called {} times\n'.format(bf_count))
time.sleep(1)
print('Dynamic programming with memoization approach - ')
print('Time taken to get Fibonacci number:', fibonacci_dp(num, True),
      's\n')  # Dynamic programming and memoization appproach
time.sleep(1)
print('Bottom to up approach - ')
print('Time taken to get Fibonacci number:', fibonacci_botup(
    num, True), 's')  # Bottom to up approach

# iterating a list of n = 0 - 1000 (step = 5) and calculating time to get fibonacci using dp/memoization and bottom to up approaches
n_list = [x for x in range(0, 1001, 5)]

bf_time = []  # storing brute force approach time values
for x in n_list[:7]:  # getting fibonacci values of N = 0 - 30 using brute force because any higher and the function would take too much time
    tic = time.time()
    fibonacci_bf(x)
    toc = time.time()
    bf_time.append(float(f"{toc - tic:0.6f}"))

dp_time = []  # dynamic programming and memoization time values
botup_time = []  # bottom up appraoch (with storage optimization) time values
for n in n_list:
    dp_time.append(float(fibonacci_dp(n, False)))
    botup_time.append(float(fibonacci_botup(n, False)))

_ = input('\nPress anything ot continue to table of DP/Mem and Bot-Up aproaches... ')


# %%
# making the table to store time values for DP/Mem and Bot-Up approaches
zipped = list(zip(n_list, dp_time, botup_time))
df = pd.DataFrame(
    zipped, columns=['N', 'DP/Mem (s)', 'Bot-Up (s)']).set_index('N')
df.name = 'Main dataframe'

# making a preview table to present why brute force times are not included in the coming graph, as the time difference is too high
print('Brute force times will not be included in the coming graph because the time difference between brute force and the other approaches are too high: ')
preview_zipped = list(zip(n_list, dp_time, botup_time, bf_time))
preview_df = pd.DataFrame(preview_zipped, columns=[
                          'N', 'DP/Mem (s)', 'Bot-Up (s)', 'Brute force (s)']).set_index('N')

print(preview_df, '\n')
_ = input('Press anything to continue to graph... \n')


# %%
# making the graph to compare times for dp/memoization and bottom to up approaches
plt.figure()
plt.style.use('fivethirtyeight')
plt.bar(df.index, df['DP/Mem (s)'], color='blue', label='DP and Memoization',
        width=5, alpha=0.5, align='center', edgecolor='black')
plt.bar(df.index, df['Bot-Up (s)'], color='red', label='Bottom to up (with space optimization)',
        width=5, alpha=0.5, align='center', edgecolor='black')
plt.gca().set_title(
    'Time comparison of DP and Memoization/Bottom to Up approaches', fontsize=14)
plt.legend(loc='best', fontsize=8)
plt.xlabel('N', fontsize=8)
plt.xticks(fontsize=10)
plt.ylabel('Time (s)', fontsize=10)
plt.yticks(fontsize=11)
plt.tight_layout()
plt.margins(x=0, y=0, tight=True)
plt.show()

_ = input('Press anything to continue to Question 2... ')


# %%
""" Question 2 - Longest common substring  """
print('\nQuestion 2 - Longest common substring')


def lcs(str1, str2):
    tic = time.time()

    if len(str1) == 0 or len(str2) == 0:  # returning None is any strings are empty
        return None

    if len(str1) < len(str2):  # formatting str1 to be the longer string and str2 to be the substring
        str1, str2 = str2, str1

    # creating 2D array to store resutls
    res = [[0] * (len(str2) + 1) for x in range(len(str1) + 1)]

    for x in range(len(str1) + 1):
        for y in range(len(str2) + 1):
            # base case
            if x == 0 or y == 0:
                res[x][y] = 0
            # checking if last char in both strings are same, storing them in results if they are and adding 1
            elif str1[x - 1] == str2[y - 1]:
                res[x][y] = res[x - 1][y - 1] + 1  # using the previous result
            # if last chars of both strings are not the same, chopping chars off and comparing lcs of str2 with str1 with their last chars removed
            else:
                res[x][y] = max(res[x - 1][y], res[x][y - 1])

    toc = time.time()
    print('\nMain string: {}'.format(str1))
    print('Substring: {}'.format(str2))
    print('Time to solve: {} s'.format(f"{toc - tic:0.6f}"))

    # returning the corner value of the 2D array
    return 'Longest common subsequence: {}\n'.format(res[len(str1)][len(str2)])


strings = valid_str()
print(lcs(strings[0], strings[1]))

print('Ashwin Rajesh Jawalikar, 20190802140')
# %%
```
