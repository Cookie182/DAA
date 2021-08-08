import timeit
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# I apologize for the messy layout i was constantly testing it every bit using hydrogen
# if any of the values for the time is np.nan it is because they were taking too long to be sorted
# selection sort
print('Selection Sort: ')
setup_code = """
import random

n = int(input("Enter n: "))
num = []
for x in range(n):
    num.append(random.randint(0,10))
print(num) """

main_code = """
def selection(arr):
    for x in range(len(arr)-1):
        min = x
        for y in range(x+1, len(arr)-1):
            if arr[y] < arr[min]:
                min = y
        arr[x], arr[min] = arr[min], arr[x]
selection(num)
print(num) """
execution_time = timeit.timeit(stmt=main_code, setup=setup_code, number=1)
print(f'{execution_time:.20f}')
################################################################################
# times for all the n values were already noted down by me was already taken manually
selection_n_list = [10, 100, 1000, 10000, 1000000]
selection_wc_time_list = [0.00011739999999971218, 0.00037770000000003634,
                          0.02363630000000060960, 2.15139960000000129980, np.nan]
selection_time_list = [0.00000109999999997612, 0.00000109999999997612,
                       0.00000149999999998762, 0.00000160000000004601, 0.00000249999999990536]
selection_df = pd.Series(selection_time_list, index=selection_n_list,
                         name='Selection').rename_axis('n').reset_index()
selection_wc_df = pd.Series(selection_wc_time_list, index=selection_n_list,
                            name='Selection WC').rename_axis('n').reset_index()
final_selection_df = pd.merge(
    selection_df, selection_wc_df, how='left', left_on='n', right_on='n')
print('\n', final_selection_df.set_index(
    'n').sort_values(['Selection', 'Selection WC']), '\n')

# plotting the line graph for selection sort
plt.figure()
plt.plot(selection_df['Selection'], selection_df['n'], '-o',
         color='black', linewidth=1.5, label='My selection sort line')
plt.gca().set_ylabel('n', rotation=0)
plt.gca().set_xlabel('Time (s)')
plt.gca().set_title('Quite close to $n^2$')
plt.gca().margins(x=0.00005, y=0)
plt.legend(loc=(0, 0.65), frameon=False, fontsize=9)
plt.tight_layout()
plt.gca().set_ylim(0, 1000000)
plt.gca().set_xlim(min(selection_time_list), max(selection_time_list))

plt.figure(figsize=(6, 4))
plt.plot(selection_wc_time_list, selection_df['n'], '-o', color='red',
         linewidth=1.5, label='My selection sort line (worst case)')
plt.gca().set_ylabel('n', rotation=0)
plt.gca().set_xlabel('Time (s)')
plt.gca().set_title('Worst Case (Selection sort)')
plt.gca().margins(x=0.00005, y=0)
plt.legend(loc=(0, 0.65), frameon=False, fontsize=9)
plt.tight_layout()
plt.gca().set_ylim(0, 10000)
plt.gca().set_xlim(min(selection_wc_time_list), selection_wc_time_list[-2])
plt.show()
""" The line that i got matches the time complexity line for selection sort """
################################################################################
print('Insertion Sort: ')
setup_code = """
import random

n = int(input("Enter n: "))
num = []
for x in range(n):
    num.append(random.randint(0,10))
print(num) """

main_code = """
def insertion(arr):
    for x in range(1, len(arr)):
        min = x
        y = x - 1
        while y >=0 and min < arr[y]:
            arr[y + 1] = arr[y]
            y -= 1
        arr[y+1]=min
insertion(num)
print(num) """
execution_time = timeit.timeit(stmt=main_code, setup=setup_code, number=1)
print(f'{execution_time:.20f}')
################################################################################
# insertion sort
insertion_n_list = [10, 100, 1000, 10000, 1000000]
insertion_wc_time_list = [0.00010250000000056048, 0.00018419999999963466,
                          0.00083749999999938041, 0.00989549999999894681, 1.92855120000000024305]
insertion_time_list = [0.00011150000000004212, 0.00016139999999964516,
                       0.00111729999999976570, 0.01110819999999979046, 1.78377230000000075449]
insertion_df = pd.Series(insertion_time_list, index=insertion_n_list,
                         name='Insertion').rename_axis('n').reset_index()
insertion_wc_df = pd.Series(insertion_wc_time_list, index=insertion_n_list,
                            name='Insertion WC').rename_axis('n').reset_index()
final_insertion_df = pd.merge(
    insertion_df, insertion_wc_df, how='left', left_on='n', right_on='n')
print('\n', final_insertion_df.set_index(
    'n').sort_values(['Insertion', 'Insertion WC']), '\n')
# plotting the line graph for insertion sort
plt.figure(figsize=(6, 4))
plt.plot(insertion_df['Insertion'], insertion_df['n'], '-o',
         color='black', linewidth=1.5, label='My insertion sort line')
plt.gca().set_ylabel('n', rotation=0)
plt.gca().set_xlabel('Time (s)')
plt.gca().set_title('Line matches the time complexity: $n$')
plt.gca().margins(x=0, y=0)
plt.legend(loc=(0, 0.65), frameon=False, fontsize=9)
plt.tight_layout()

plt.figure(figsize=(6, 4))
plt.plot(insertion_wc_time_list, insertion_df['n'], '-o', color='red',
         linewidth=1.5, label='My insertion sort line (worst case)')
plt.gca().set_ylabel('n', rotation=0)
plt.gca().set_xlabel('Time (s)')
plt.gca().set_title('Worst Case(Insertion sort)')
plt.gca().margins(x=0, y=0)
plt.legend(loc=(0, 0.65), frameon=False, fontsize=9)
plt.tight_layout()
plt.show()
################################################################################
print('Merge sort: ')
setup_code = """
import random
n = int(input("Enter n: "))
num = []
for x in range(n):
    num.append(random.randint(0,10))
print(num) """

main_code = """
def merge(arr):
    if len(arr)>1:
        m = len(arr)//2
        l = arr[:m]
        r = arr[m:]
        l = merge(l)
        r = merge(r)
        arr =[]
        while len(l)>0 and len(r)>0:
            if l[0]<r[0]:
                arr.append(l[0])
                l.pop(0)
            else:
                arr.append(r[0])
                r.pop(0)
        for i in l:
            arr.append(i)
        for i in r:
            arr.append(i)
    return arr
num = merge(num)
print(*num) """
execution_time = timeit.timeit(stmt=main_code, setup=setup_code, number=1)
print(f'{execution_time:.20f}')
################################################################################
# merge sort
merge_n_list = [10, 100, 1000, 10000, 1000000]
merge_wc_time_list = [0.00031099999999639749, 0.00036659999999955062,
                      0.00338530000000503151, 0.04283250000000116131, 59.71065310000000181390]
merge_time_list = [0.00013149999999928497, 0.00035209999999974428,
                   0.00316700000000036397, 0.04493850000000065847, 97.58797420000000499840]
merge_df = pd.Series(merge_time_list, index=merge_n_list,
                     name='Merge').rename_axis('n').reset_index()
merge_wc_df = pd.Series(merge_wc_time_list, index=merge_n_list,
                        name='Merge WC').rename_axis('n').reset_index()
final_merge_df = pd.merge(merge_df, merge_wc_df,
                          how='left', left_on='n', right_on='n')
print('\n', final_merge_df.set_index(
    'n').sort_values(['Merge', 'Merge WC']), '\n')
# plotting the line graph for merge sort
plt.figure(figsize=(6, 4))
plt.plot(merge_df['Merge'], merge_df['n'], '-o', color='black',
         linewidth='1.5', label='My merge sort line')
plt.gca().set_xlabel('Time (s)')
plt.gca().set_ylabel('n', rotation=0)
plt.gca().set_title("Line is similar to insertion's line")
plt.gca().margins(x=0, y=0)
plt.legend(loc=(0, 0.65), frameon=False, fontsize=9)
plt.tight_layout()

plt.figure(figsize=(6, 4))
plt.plot(merge_wc_time_list, merge_df['n'], '-o', color='red',
         linewidth='1.5', label='My merge sort line (worst case)')
plt.gca().set_xlabel('Time (s)')
plt.gca().set_ylabel('n', rotation=0)
plt.gca().set_title("Worst Case (Merge sort)")
plt.gca().margins(x=0, y=0)
plt.legend(loc=(0, 0.65), frameon=False, fontsize=9)
plt.tight_layout()
plt.show()
################################################################################
print('Quick sort: ')
setup_code = """
sys.setrecursionlimit(1500)
import random
n = int(input("Enter n: "))
num = []
for x in range(n):
    num.append(np.random.randint(0, 10))
print(num) """

main_code = """
def quick(arr):
    if len(arr) < 2:
        return arr
    min = 0
    for x in range(1,len(arr)):
        if arr[x] <= arr[0]:
            min += 1
            temp = arr[x]
            arr[x] = arr[min]
            arr[min] = temp
    temp = arr[0]
    arr[0] = arr[min]
    arr[min] = temp

    l = quick(arr[0:min])
    r = quick(arr[min+1:len(arr)])

    arr = l + [arr[min]] + r
    return arr

num = quick(num)
print(*num) """
execution_time = timeit.timeit(stmt=main_code, setup=setup_code, number=1)
print(f'{execution_time:.20f}')
################################################################################
# quick sort
quick_n_list = [10, 100, 1000, 10000, 1000000]
quick_wc_time_list = [0.00029689999999504835,
                      0.00381969999999398624, np.nan, np.nan, np.nan]
quick_time_list = [0.00013290000000054647, 0.00032189999999943097,
                   0.00719890000000056318, 0.65811549999999918725, np.nan]
quick_df = pd.Series(quick_time_list, index=quick_n_list,
                     name='Quick').rename_axis('n').reset_index()
quick_wc_df = pd.Series(quick_wc_time_list, index=quick_n_list,
                        name='Quick WC').rename_axis('n').reset_index()
final_quick_df = pd.merge(quick_df, quick_wc_df,
                          how='left', left_on='n', right_on='n')
print('\n', final_quick_df.set_index(
    'n').sort_values(['Quick', 'Quick WC']), '\n')
# plotting the line graph for quick sort
plt.figure(figsize=(6, 4))
plt.plot(quick_df['Quick'], quick_df['n'], '-o',
         color='black', linewidth=1.5, label='My quick sort line')
plt.gca().set_xlabel('Time (s)')
plt.gca().set_ylabel('n', rotation=0)
plt.gca().set_title(' Very steep at the start, but later on evens out ')
plt.gca().margins(x=0, y=0)
plt.legend(loc=(0, 0.65), frameon=False, fontsize=9)
plt.tight_layout()

plt.figure(figsize=(6, 4))
plt.plot(quick_wc_time_list, quick_df['n'], '-o', color='red',
         linewidth=1.5, label='My quick sort line (worst case)')
plt.gca().set_xlabel('Time (s)')
plt.gca().set_ylabel('n', rotation=0)
plt.gca().set_title(' Worst Case (Quick Sort) ')
plt.gca().margins(x=0, y=0)
plt.legend(loc=(0, 0.65), frameon=False, fontsize=9)
plt.tight_layout()
plt.show()
################################################################################
print('Bubble sort: ')
setup_code = """
import random
n = int(input("Enter n: "))
num = []
for x in range(n):
    num.append(random.randint(0,10))
print(num) """

main_code = """
def bubble(arr):
    for x in range(len(arr)):
        swapped = False
        for y in range(0,n-x-1):
            if arr[y] > arr[y+1]:
                arr[y],arr[y+1] = arr[y+1],arr[y]
                swapped=True
        if swapped==False:
            return arr
            break

num = bubble(num)
print(num) """
execution_time = timeit.timeit(stmt=main_code, setup=setup_code, number=1)
print(f'{execution_time:.20f}')
################################################################################
# bubble sort
bubble_n_list = [10, 100, 1000, 10000, 1000000]
bubble_wc_time_list = [0.00038699999999991519, 0.00042089999999461725,
                       0.00092680000000022744, 0.01205999999999995964, 2.03698310000000049058]
bubble_time_list = [0.00034989999999979204, 0.00070260000000033074,
                    0.05500350000000153727, 6.12761979999999795155, np.nan]
bubble_wc_df = pd.Series(bubble_wc_time_list, index=bubble_n_list,
                         name='Bubble WC').rename_axis('n').reset_index()
bubble_df = pd.Series(bubble_time_list, index=bubble_n_list,
                      name='Bubble').rename_axis('n').reset_index()
final_bubble_df = pd.merge(bubble_df, bubble_wc_df,
                           how='left', left_on='n', right_on='n')
print('\n', final_bubble_df.set_index(
    'n').sort_values(['Bubble', 'Bubble WC']), '\n')
# plotting the line graph for bubble sort
plt.figure(figsize=(6, 4))
plt.plot(bubble_df['Bubble'], bubble_df['n'], '-o',
         color='black', linewidth=1.5, label='My bubble sort line')
plt.gca().set_xlabel('Time (s)')
plt.gca().set_ylabel('n', rotation=0)
plt.gca().set_title('My line is very similar to my line on Quick sort')
plt.gca().margins(x=0, y=0)
plt.legend(loc=(0, 0.65), frameon=False, fontsize=9)
plt.tight_layout()

plt.figure(figsize=(6, 4))
plt.plot(bubble_wc_time_list, bubble_df['n'], '-o', color='red',
         linewidth=1.5, label='My bubble sort line (worst case)')
plt.gca().set_xlabel('Time (s)')
plt.gca().set_ylabel('n', rotation=0)
plt.gca().set_title('Worst Case (Bubble Sort)')
plt.gca().margins(x=0, y=0)
plt.legend(loc=(0, 0.65), frameon=False, fontsize=9)
plt.tight_layout()
plt.show()
################################################################################
