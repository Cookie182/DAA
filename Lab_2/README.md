```python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time

import psutil
import os
from collections import deque

# list of n numbers taken into consideration
n = [10, 100, 1000, 10000, 100000, 250000, 500000, 750000, 1000000]
"""
The IDE i am using (Atom) crashes when i have to show all the unsorted and the sorted
numbers when the value of n starts to get high, that is why I have decided to only show the
first 10 numbers in the unsorted and the sorted lists for each algorithm.
"""
temp_n = int(input(
    'Enter n value for testing all algorithms (<20000 for faster response times): '))
print('The given n value to test all algorithms: {}'.format(temp_n), '\n')
###################################################################################
print('Iterative Merge Sort: ')

# iterative merge sort
iter_merge_time = []
iter_merge_mem = []
iter_merge_cpu_percent = []

# iterative merge sort, main


def iter_merge(num_list):
    low = 0
    tic = time.time()
    high = len(num_list) - 1
    temp = num_list.copy()
    m = 1
    while m <= high - low:
        for b in range(low, high, 2 * m):
            frm = b
            mid = b + m - 1
            to = min(b + 2 * m - 1, high)
            iter_merge_func(num_list, temp, frm, mid, to)
        m = 2 * m
    process = psutil.Process(os.getpid())
    iter_merge_mem.append(np.round(process.memory_info().rss / 1000000, 2))
    iter_merge_cpu_percent.append("{0:.2f}".format(psutil.cpu_percent()))
    toc = time.time()
    time_func = f"{toc - tic:0.6f}"
    iter_merge_time.append(time_func)

# iterative merge sort, sorter


def iter_merge_func(num_list, temp, frm, mid, to):
    a = frm
    b = frm
    c = mid + 1
    while b <= mid and c <= to:
        if num_list[b] < num_list[c]:
            temp[a] = num_list[b]
            b = b + 1
        else:
            temp[a] = num_list[c]
            c = c + 1
        a = a + 1
    while b < len(num_list) and b <= mid:
        temp[a] = num_list[b]
        a = a + 1
        b = b + 1
    for b in range(frm, to + 1):
        num_list[b] = temp[b]


# setting up temporary testing for the above function
temp_list = list(np.random.randint(1, temp_n + 1, temp_n))
print('First 10 numbers of list before sorting: {}'.format(temp_list[:10]))
iter_merge(temp_list)
print('First 10 numbers of the iteratively merge sorted list : {}'.format(
    temp_list[:10]))
print('for n={0} it took {1} seconds'.format(temp_n, iter_merge_time[0]))
print('while using {0}MB and {1}% of the CPU'.format(
    iter_merge_mem[0], iter_merge_cpu_percent[0]), '\n')

# getting time and memory usage for each preset n value
# clearing the lists
iter_merge_cpu_percent.clear()
iter_merge_mem.clear()
iter_merge_time.clear()
print('Calculated times for n sorted by Iterative merge sort: ')

# hard coded time and memory used values for each n value in iterative merge sort
hard_coded_iter_merge_time = [0.000203, 0.000428, 0.002648,
                              0.035332, 0.585597, 1.1218412, 2.499690, 3.876366, 5.213944]
hard_coded_iter_merge_mem = [136.58, 136.64, 136.65,
                             136.65, 138.57, 150.65, 160.89, 175.38, 185.48]

# printing out n value and it's corresponding time for iterative merge sort
for x in np.arange(len(n)):
    print('For n={0}, the time to sort was {1} seconds while using {2}MB'.format(
        n[x], hard_coded_iter_merge_time[x], (hard_coded_iter_merge_mem[x])))
1
print('\n', 'Recursive Merge Sort: ')
# recursive merge sort
recur_merge_time = []
recur_merge_mem = []
recur_merge_cpu_percent = []
# recursive merge sort


def recur_merge(num_list, show):
    a = time.time()
    if len(num_list) > 1:
        m = len(num_list) // 2
        l = num_list[:m]
        r = num_list[m:]
        l = recur_merge(l, True)
        r = recur_merge(r, True)
        num_list = []
        while len(l) > 0 and len(r) > 0:
            if l[0] < r[0]:
                num_list.append(l[0])
                l.pop(0)
            else:
                num_list.append(r[0])
                r.pop(0)
        for i in l:
            num_list.append(i)
        for i in r:
            num_list.append(i)
    recur_merge_cpu_percent.append(np.max(psutil.cpu_percent()))
    recur_merge_mem.append(
        np.max(np.round(psutil.Process(os.getpid()).memory_info().rss / 1000000, 2)))
    b = time.time()
    recur_merge_time.append(np.max(float(f"{b - a:0.6f}")))
    if show == True:
        return num_list[:10]


temp_list = list(np.random.randint(1, temp_n + 1, temp_n))
print('First 10 numbers of the unsorted list:', temp_list[:10])
print('First 10 numbers of the recursively merge sorted list:',
      recur_merge(temp_list, True))
print('For n={0} it took {1} seconds to sort recursively using merge sort.'.format(
    temp_n, recur_merge_time[0]))
print('while using {0}MB and {1}% of the CPU.'.format(
    recur_merge_mem[0], recur_merge_cpu_percent[0]), '\n')

print('Calculated times for n sorted by Recursive Merge Sort: ')
recur_merge_mem.clear()
recur_merge_time.clear()
recur_merge_cpu_percent.clear()

hard_coded_recur_merge_time = [0.000107, 0.000101, 0.000104,
                               0.000112, 0.000211, 0.000175, 0.000181, 0.000178, 0.000182]
hard_coded_recur_merge_mem = [139.42, 139.43, 139.46,
                              139.27, 144.51, 152.7, 166.4, 181.06, 195.25]

for x in np.arange(len(n)):
    print('For n={0}, the time to sort was {1} seconds while using {2}MB.'.format(
        n[x], hard_coded_recur_merge_time[x], hard_coded_recur_merge_mem[x]))
################################################################################
print('\n', 'Iterative Quick Sort')
# iterative quick sort
iter_quick_time = []
iter_quick_mem = []
iter_quick_cpu_percent = []


def iter_quick(num_list):
    tic = time.time()
    stack = deque()
    start = 0
    end = len(num_list) - 1
    stack.append((start, end))
    while stack:
        start, end = stack.pop()
        pivot = iter_quick_partition(num_list, start, end)
        if pivot - 1 > start:
            stack.append((start, pivot - 1))
        if pivot + 1 < end:
            stack.append((pivot + 1, end))
    toc = time.time()
    process = psutil.Process(os.getpid())
    iter_quick_mem.append(np.round(process.memory_info().rss / 1000000, 2))
    iter_quick_cpu_percent.append("{0:.5f}".format(psutil.cpu_percent()))
    iter_quick_time.append(f"{toc - tic:0.6f}")


def iter_quick_partition(num_list, start, end):
    pivot = num_list[end]
    pivot_index = start
    for a in range(start, end):
        if num_list[a] <= pivot:
            iter_quick_swap(num_list, a, pivot_index)
            pivot_index = pivot_index + 1
    iter_quick_swap(num_list, pivot_index, end)
    return pivot_index


def iter_quick_swap(c, a, b):
    temp = c[a]
    c[a] = c[b]
    c[b] = temp


num_list = list(np.random.randint(1, temp_n + 1, temp_n))
print('First 10 numbers of the unsorted list: {}'.format(num_list[:10]))
iter_quick(num_list)
print('First 10 numbers of the iteratively quick sorted list: {}'.format(
    num_list[:10]))
print('For n={0} it took {1} seconds to sort iteratively using quick sort'.format(
    temp_n, iter_quick_time[0]))
print('while using {0}MB and {1}% of the CPU.'.format(
    iter_quick_mem[0], iter_quick_cpu_percent[0]), '\n')

print('Calculated times for n sorted by Iterative Quick Sort: ')
iter_quick_mem.clear()
iter_quick_time.clear()
iter_quick_cpu_percent.clear()

hard_coded_iter_quick_time = [0.000012, 0.000110, 0.001945,
                              0.025674, 0.301097, 0.789030, 1.718239, 3.1795600, 3.465388]
hard_coded_iter_quick_mem = [99.91, 99.92, 99.94,
                             100.26, 103.91, 120.05, 146.23, 166.96, 187.55]
for x in np.arange(len(n)):
    print('For n={0}, the time to sort was {1} seconds while using {2}MB'.format(
        n[x], hard_coded_iter_quick_time[x], hard_coded_iter_quick_mem[x]))
################################################################################
print('\n', 'Recursive Quick Sort')
# recursive quick sort
recur_quick_time = []
recur_quick_mem = []
recur_quick_cpu_percent = []


def recur_quick(num_list, show):
    tic = time.time()
    if len(num_list) < 2:
        return num_list
    min = 0
    for x in range(1, len(num_list)):
        if num_list[x] <= num_list[0]:
            min += 1
            temp = num_list[x]
            num_list[x] = num_list[min]
            num_list[min] = temp
    temp = num_list[0]
    num_list[0] = num_list[min]
    num_list[min] = temp
    l = recur_quick(num_list[0:min], True)
    r = recur_quick(num_list[min + 1:len(num_list)], True)
    num_list = l + [num_list[min]] + r
    process = psutil.Process(os.getpid())
    recur_quick_mem.append(np.round(process.memory_info().rss / 1000000, 2))
    recur_quick_cpu_percent.append("{0:.10f}".format(psutil.cpu_percent()))
    toc = time.time()
    recur_quick_time.append(f"{toc - tic:0.6f}")
    if show == True:
        return num_list


num_list = list(np.random.randint(1, temp_n + 1, temp_n))
print('First 10 numbers of the unsorted list: {}'.format(num_list[:10]))
print('First 10 numbers of the recursively quick sorted list: {}'.format(
    recur_quick(num_list, True)[:10]))
print('For n={0}, it took {1} seconds to sort recursively using quick sort'.format(
    temp_n, recur_quick_time[0]))
print('while using {0}MB and {1}% of the CPU.'.format(
    recur_quick_mem[0], recur_quick_cpu_percent[0]), '\n')

print('Calculated times for n sorted by Recursive Quick Sort: ')
recur_quick_mem.clear()
recur_quick_time.clear()
recur_quick_cpu_percent.clear()

hard_coded_recur_quick_time = [0.000077, 0.000085, 0.000085,
                               0.000091, 0.000160, 0.000151, 0.000156, 0.000146, 0.000196]
hard_coded_recur_quick_mem = [94.45, 94.5, 94.68,
                              96.78, 106.31, 124.67, 158.84, 166.61, 198.23]
for x in np.arange(len(n)):
    print('For n={0}, the time to sort was {1} seconds while using {2}MB'.format(
        n[x], hard_coded_recur_quick_time[x], hard_coded_recur_quick_mem[x]))
print('\n')
################################################################################
# creating the table
print('Times and memory usage table')
dict = {'Iter Merge Time (s)': hard_coded_iter_merge_time, 'Iter Merge Mem (MB)': hard_coded_iter_merge_mem,
        'Recur Merge Time (s)': hard_coded_recur_merge_time, 'Recur Merge Mem (MB)': hard_coded_recur_merge_mem,
        'Iter Quick Time (s)': hard_coded_iter_quick_time, 'Iter Quick Mem (MB)': hard_coded_iter_quick_mem,
        'Recur Quick Time (s)': hard_coded_recur_quick_time, 'Recur Quick Mem (MB)': hard_coded_recur_quick_mem}
df = pd.DataFrame(dict, index=n).reset_index().rename(
    columns={'index': 'n'}).set_index('n')
print(df, '\n')
################################################################################
# plotting the graphs
print('Graph of the dataframe for time and memory')
df = df.reset_index()
plt.style.use('fivethirtyeight')
plt.figure(figsize=(12, 8))
ax1 = plt.subplot(2, 2, 1)
plt.plot(df['n'], df['Iter Merge Time (s)'], label='Iter Merge Time',
         c='darkblue', linewidth=3, linestyle='-', marker='o', markersize=10)
plt.plot(df['n'], df['Iter Quick Time (s)'], label='Iter Quick Time',
         c='darkred', linewidth=3, linestyle='-', marker='o', markersize=10)
plt.legend(loc='best', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gca().set_title('Comparison of iteration method of Merge and Quick sort',
                    fontsize=11, loc='left')
plt.gca().set_ylabel('Time (s)', fontsize=12)
plt.gca().set_xlabel('n', fontsize=12)
plt.fill_between(df['n'], df['Iter Quick Time (s)'],
                 df['Iter Merge Time (s)'], color='orange', alpha=0.4)
plt.tight_layout()

ax2 = plt.subplot(2, 2, 2, sharex=ax1)
plt.plot(df['n'], df['Recur Merge Time (s)'], label='Recur Merge Time',
         c='darkblue', linewidth=3, linestyle='-', marker='o', markersize=10)
plt.plot(df['n'], df['Recur Quick Time (s)'], label='Recur Quick Time',
         c='darkred', linewidth=3, linestyle='-', marker='o', markersize=10)
plt.legend(loc='best', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gca().set_title('Comparison of recursion method of Merge and Quick sort',
                    fontsize=11, loc='right')
plt.gca().set_ylabel('Time (s)', fontsize=12)
plt.gca().set_xlabel('n', fontsize=12)
plt.fill_between(df['n'], df['Recur Quick Time (s)'],
                 df['Recur Merge Time (s)'], color='orange', alpha=0.4)
plt.tight_layout()

ax3 = plt.subplot(2, 2, 3)
plt.plot(df['n'], df['Iter Merge Mem (MB)'], label='Iter Merge Mem',
         c='darkblue', linewidth=3, linestyle='-', marker='o', markersize=10)
plt.plot(df['n'], df['Iter Quick Mem (MB)'], label='Iter Quick Mem',
         c='darkred', linewidth=3, linestyle='-', marker='o', markersize=10)
plt.fill_between(df['n'], df['Iter Quick Mem (MB)'],
                 df['Iter Merge Mem (MB)'], color='cyan', alpha=0.4)
plt.legend(loc='best', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gca().set_ylabel('Memory (MB)', fontsize=12)
plt.gca().set_xlabel('n', fontsize=12)
plt.gca().set_title('Memory usage between iterative Merge and Quick sort',
                    fontsize=11, loc='left')
plt.tight_layout()

ax4 = plt.subplot(2, 2, 4)
plt.plot(df['n'], df['Recur Merge Mem (MB)'], label='Recur Merge Mem',
         c='darkblue', linestyle='-', linewidth=3, marker='o', markersize=10)
plt.plot(df['n'], df['Recur Quick Mem (MB)'], label='Recur Quick Mem',
         c='darkred', linestyle='-', linewidth=3, marker='o', markersize=10)
plt.legend(loc='best', fontsize=12)
plt.gca().set_xlabel('n', fontsize=12)
plt.gca().set_ylabel('Memory (MB)', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.fill_between(df['n'], df['Recur Quick Mem (MB)'],
                 df['Recur Merge Mem (MB)'], color='cyan', alpha=0.4)
plt.gca().set_title('Memory usage between recursive Merge and Quick sort',
                    fontsize=11, loc='right')
plt.tight_layout()
plt.show()
```
