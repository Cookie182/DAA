import os  # to access the memory itself
import random  # to generate a list of random integers
import time  # to measure time

import pandas as pd  # to generate a table to store data in
import psutil  # to measure memory usage and cpu load
from matplotlib import pyplot as plt  # to generate a graph

"""
importing the numbers from the given file
"""

nums = []  # creating list to store values from the .txt file
with open('numbers.txt', 'r') as txt:  # opening the file
    for line in txt:  # iterating through each line in the file
        # stripping each line and converting the element in that line to an int, appending that to nums list
        nums.append(int(line.strip()))
# showing the numbers extracted from the .txt file
print('\nOriginal number list:', *nums)


"""
 creating the algorithm to make a binary search tree, calculating the height, minimum depth, maximum depth and the LCA from the values given by the user
"""


class node:  # creating node class
    def __init__(self, value=None):  # creating constructor (with a value that is set default to None)
        self.value = value  # saving value
        # since each node has 2 children (left and right, left being the smaller one wih the right being the larger)
        # creating 2 points for the children
        # assume None one because we are assuming there are no initial values for left and right child
        self.left_child = None
        self.right_child = None

    def __str__(self):  # makign the representative function for the class
        return str(self.value)  # returning the value when the class is called


class binary_search_tree:  # binary search tree class, it is the wrapper that handles the management of all the node classes
    def __init__(self):  # creating the constructor
        self.root = None  # initial value will be None

    def insert(self, value):  # creating the constructor
        if self.root == None:  # checking to see if we can insert a value at the root
            # reseting the root with the passed value if there is no value in the root
            self.root = node(value)
        else:  # if we can't insert the root
            # calling in a private recursive function (a seperate function)
            self._insert(value, self.root)

    # defining the private function from the above defined function
    def _insert(self, value, cur_node):
        if value < cur_node.value:  # if the value to be inserted is less than the value already in the node
            if cur_node.left_child == None:  # inserting the value in the left node if there is no pre-existing value in it
                cur_node.left_child = node(value)
            else:  # if the node does have a pre-existing value
                # recurse down the left part of the tree until free space is found
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:  # if the value to be inserted is more than the value already in the node
            if cur_node.right_child == None:  # inserting the value in the right node if there is no pre-existing value in it
                cur_node.right_child = node(value)
            else:  # if the node does have a pre-existing value
                # recurse down the right part of the tree until free space is found
                self._insert(value, cur_node.right_child)
        else:  # if the value to be inserted is equal to the pre-existing value in the node
            # luckily this situation isn't occuring for this assignment
            print("Value already in tree!")

    def print_tree(self):  # defining a function to print out the binary search tree
        if self.root != None:  # checking to see if the root is an actual node
            # inserting the root into a another private function (for better readability)
            self._print_tree(self.root)

    def _print_tree(self, cur_node):  # defining the private function to run if the root is not
        if cur_node != None:  # checking if the node has a value
            # creating the in order reversal of the tree
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    # the below height, min_height and max_height were functions done by me when I was messing around with functions I got from the internet
    # for fun, to get the height of the tree
    def height(self):
        if self.root != None:  # taking into consideration if the tree has values to begin with
            # if it has values, using 2 private functions to calculate max and min height
            return self.max_height(self.root, 0), self.min_height(self.root, 0)
        else:  # return an appropriate if the root DOESN'T have any values in it
            return 0

    # defining the private versions of the min and max height function (to calculate height IF there are values in the root)
    # new variable, cur_height, think of it as a counter for the height as we traverse up the nodes
    def max_height(self, cur_node, cur_height):
        if cur_node == None:  # checking to see if the node we are iterating through has a value
            return cur_height

        # calculating the heights from both sub-trees and returning the larger value, incase the tree is not balanced or full
        # getting the height from the left subtree of the current node and incrementing through them
        left_height = self.max_height(cur_node.left_child, cur_height + 1)
        # getting the height from the right subtree of the current node and incrementing through them
        right_height = self.max_height(cur_node.right_child, cur_height + 1)
        # to return the higher value between left_height and right_height
        return max(left_height, right_height)

    # previous height function was for the max height, same function now, except just for the min height
    def min_height(self, cur_node, cur_height):
        if cur_node == None:  # checking to see if the node we are iterating through has a value
            return cur_height

        # calculating the heights from both sub-trees and returning the larger value, incase the tree is not balanced or full
        # getting the height from the left subtree of the current node and incrementing through them
        left_height = self.min_height(cur_node.left_child, cur_height + 1)
        # getting the height from the right subtree of the current node and incrementing through them
        right_height = self.min_height(cur_node.right_child, cur_height + 1)
        # to return the lower value between left_height and right_height
        return min(left_height, right_height)

    # to search for values in the tree

    def search(self, value):
        if self.root != None:  # goes to the private function only if there are values in the root
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:  # returns true if the value is found in the node
            return True
        # goes to the left child if the value of the node is less than the number we want to find and if there is no value in the left child
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        # goes to the right child if the value of the node is more than the number we want to fidn and if there is no value in the right child
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child)
        else:
            return False


# the lca function was taken straight from the function I wrote for it's HackerRank question


def lca(root, v1, v2):  # function to calculate the LCA
    if v1 > v2:  # figuring out which of the 2 given inputs is the larger one
        v_big, v_small = v1, v2
    else:
        v_big, v_small = v2, v1

    cur_node = root  # starts with the root of the tree
    while True:
        if cur_node.value > v_big:  # selects the value in the left child if the value is bigger than the bigger given input
            cur_node = cur_node.left_child
        elif cur_node.value < v_small:  # selects the value in the right child if the value is smaller than the smaller given input
            cur_node = cur_node.right_child
        # finds the parent by choosing a value that is bigger than the smaller input and smaller than the bigger input
        elif cur_node.value >= v_small and cur_node.value <= v_big:
            return cur_node  # returns the value when it matche's the final condition
        else:
            return 'Value not in the tree'

# function to fill in the tree with the numbers from the given assignment .txt file


def fill_tree(tree):
    for x in nums:  # iterating through each element in the given list of numbers
        tree.insert(x)  # adding each element from the root to the tree
    return tree


# creating the tree
tree = binary_search_tree()
# inserting the elements from the numbers list in the tree
tree = fill_tree(tree)
# printing out the tree
print('In order walk of the tree: ')
# this function draws out the tree in the correct order after the values have been inserted
tree.print_tree()

# getting the amount of levels in the tree
print('\nTotal height of the tree: {}'.format(max(tree.height())))
# printing out the maximum depth
print('The maximum depth of the tree is: {}'.format(
    tree.height()[0] - 1))  # the max amount of depths
# printing out the minimum depth
print('The minimum depth of the tree is: {}\n'.format(
    tree.height()[1] - 1))  # the min amount of depths


# making a loop to get the appropriate input from the user
while True:  # making an endless loop
    try:
        N1, N2 = map(int, input(
            "Enter 2 values from the tree to compute it's LCA: ").split())  # getting 2 values from the user as input
        # checking if both values are in the tree first
        if tree.search(N1) == True and tree.search(N2) == True:
            # printing out that the values are in the tree
            print('Values {0} and {1} are in the tree!'.format(N1, N2))
            # finding the LCA of both values within the tree
            print('The LCA for the entered numbers is:',
                  lca(tree.root, N1, N2), '\n')
            break  # breaking the endless loop since the condition has been satisfied
        else:
            # telling the user that the entered values are not in the tree
            print(
                'The values you have entered are not in the tree, try again!')
    except:
        continue  # making an except case to go through the loop again until the appropriate input has been entered


# asking the user if they want to enter a new number in the original list
print('Do you want to add a value to the list and see all the previous properties of the new list?')
cont = input('[Y for Yes, enter any other character for No]: ').strip()
# if the user answers appropriately with a yes
if cont == 'Y' or cont == 'y':
    while True:  # making an infiinte loop to make sure the user enters appripriate values for each field
        try:
            new_num = int(input(
                'Enter a number to add to the list. (Number must be unique to the list): '))  # asking for new number
            if new_num not in nums:  # checking if the number is not already in the pre-existing list
                # appending it to the original list if the number is unique to the list
                nums.append(new_num)
                print('{} successfully added to the list, new list:'.format(
                    new_num), *nums)  # printing the list after appending the new number to it
                break  # breakin the infinite loop if all the requirements are met
            else:
                # printing an error message if the entered value is not appropraite
                print('The value you have entered is already in the list or is invalid!')
        except:
            continue  # repeating the loop until user inputs appropriate value

    print('The new in order walk of the tree: ')
    tree.insert(new_num)  # inserting the new number into the tree
    # printing the new in order walk of the tree after inserting the new number
    tree.print_tree()
    # printing the new height of the tree
    print('\nNew total height of the tree:', max(tree.height()))
    # printing the new maximum depth
    print('New maximum depth of the tree is {}'.format(tree.height()[0] - 1))
    # printing the new minimum depth
    print('New minimum depth of hte tree is {}\n'.format(tree.height()[1] - 1))
    # repeating the same while loop as before for this part as well
    while True:  # making an endless loop
        try:
            N3, N4 = map(int, input(
                "Enter 2 values from the tree to compute it's LCA: ").split())  # getting 2 values from the user as input
            # checking if both values are in the tree first
            if tree.search(N3) == True and tree.search(N4) == True:
                # printing out that the values are in the tree
                print('Values {0} and {1} are in the tree!'.format(N3, N4))
                # finding the LCA of both values within the tree
                print('The LCA for the entered numbers is:',
                      lca(tree.root, N3, N4), '\n')
                break  # breaking the endless loop since the condition has been satisfied
            else:
                # telling the user that the entered values are not in the tree
                print(
                    'The values you have entered are not in the tree, try again!')
        except:
            continue  # making an except case to go through the loop again until the appropriate input has been entered
else:
    print('')
    pass

_ = input('Press Enter to continue to Heap Sort...')


"""
Heap Sort
"""

# making the main heap sort function


def heap(num_list):
    tic = time.time()  # starting the timer
    n = len(num_list)  # saving the length of the array

    # building the max heap
    # start at ((n // 2) - 1) location since that is where the last parent of the tree will be
    for x in range(n // 2 - 1, -1, -1):  # going left on the array until we hit the last value
        heapify(num_list, n, x)  # using the helper function

    # extract the elements one by one
    for x in range(n - 1, 0, -1):
        # swapping the elements
        num_list[x], num_list[0] = num_list[0], num_list[x]
        heapify(num_list, x, 0)  # using the helper function
    process = psutil.Process(os.getpid())  # accessing the OS memory info
    # accessing the correct memory and converting it
    mem = process.memory_info().rss / 1000000
    heap_mem.append(mem)  # appending it to memory list
    # printing the amount of memory used
    print('Memory usage: {} MB'.format(mem))
    # accessing the CPU load percentage when the script is running
    cpu = "{:0.2f}".format(psutil.cpu_percent())
    print('CPU load: {}%'.format(cpu))  # printing the CPU load percentage
    heap_cpu.append(cpu)  # appending CPU load percentage to the CPU load list
    toc = time.time()  # stopping the timer
    # basic maths to calculate the run time of the script
    tim = f'{toc - tic:0.6f}'
    # printing the run time for hte script
    print('Time taken to sort: {} s'.format(tim))
    heap_time.append(tim)  # appending the run time to the time list

# function to convert the binary tree into heap data sturcture, heapify


def heapify(num_list, n, x):
    largest = x  # initializing the largest value as root
    left = 2 * x + 1
    right = 2 * x + 2

    # seeing if there is a value in the left child of the root and if it is greater than the root
    if left < n and num_list[x] < num_list[left]:
        largest = left

    # seeing if there is a value in the right child of the root and if it is greater than the root
    if right < n and num_list[largest] < num_list[right]:
        largest = right

    # changing the root if needed
    if largest != x:
        # swapping the values
        num_list[x], num_list[largest] = num_list[largest], num_list[x]

        # applying the heapify process to the root
        heapify(num_list, n, largest)


"""
the technical part of getting the data required from the algorithm depending on the n values
"""

heap_time = []  # time list
heap_mem = []  # memory list
heap_cpu = []  # cpu load percentage list
# list of n values to test the heap sort algorithm with
n = [10, 100, 500, 1000, 2500, 5000, 7500, 10000]
print('N values to be considered:', *n, '\n')
# starting a loop to feed every value of n in the list to the heap sort algorithm and to extract the stats from itf
for num in n:
    # creating a random list of numbers to feed into the algorithm
    # list that starts from 0, maximum value = n with n amount of numbers
    num_list = random.sample(range(0, num + 1), num)
    # printing the n value that the printed info is corresponding to
    print('For a list of {} digits:'.format(num))
    # printing the first 10 digits of the random (un-sorted) integers list before it gets fed to the heap algorithm
    print('First 10 digits before sorting:', *num_list[:10])
    # feeding the list of random, un-sorted, numbers to the heap algorithm
    heap(num_list)
    # printing the list of random, now sorted, list of numbers after it was fed to the heap algorithm
    print('First 10 digits after heap sorting', *num_list[:10], '\n')
    _ = input('Press Enter to continue...')


# creating the table to display the stats corresponding with the n values
# zipping the 3 lists together whose values correspond with each other
zipped_list = list(zip(heap_time, heap_mem, heap_cpu, n))
# creating the data base with the zipped list as the data, n values as the index and also applying column names
df = pd.DataFrame(zipped_list, columns=['Time taken (s)', 'Memory used (MB)',
                                        'CPU load (%)', 'n']).set_index('n')
print('Table for heap sort times, memory usage and cpu load percentages depending on the n value:\n')
print(df, '\n')  # printing the dataframe
_ = input('Press Enter to continue to the graph...')

"""
making the graph with the database
"""

plt.xkcd()  # setting the style for the graphs
# making the figure and setting the figure size
fig = plt.figure(figsize=(20, 8))
# setting the background color of the entire figure
fig.set_facecolor('cyan')
# setting the opacity levels of the graph's background
fig.set_alpha(0.3)
ax1 = plt.subplot(1, 2, 2)  # making the first subplot
plt.gca().set_facecolor('orange')  # setting the background color of the graph
plt.plot(df['Time taken (s)'], df.index, linestyle='-',
         c='black', linewidth=3.5)  # plotting the time against the n, setting the linestyle, width and color
plt.gca().set_xlabel('Time (s)', fontsize=13,
                     loc='right')  # making a label for the x axis
# making a label for the y axis and with no rotation on it
plt.gca().set_ylabel('n', rotation=0, fontsize=13)
plt.gca().set_title('Relationship between time and n for Heap sort',
                    fontsize=16, loc='right')  # setting the title with fontsize
# filling the area under the line on the graph
plt.fill_between(df['Time taken (s)'], 0, n, color='red', alpha=0.5)
plt.gca().margins(x=0, y=0)  # making sure the line fits the corners of the graph
plt.xticks(fontsize=8)  # setting the x axis tick's font size
plt.yticks(fontsize=10)  # setting the y axis tick's font size
plt.tight_layout()  # giving the subplot graph a tight layout

ax2 = plt.subplot(1, 2, 1, sharey=ax1)  # making the second subplot
plt.gca().set_facecolor('orange')  # setting the background color of the graph
# plotting the memory used agaisnt the n, setting the linestyle, width and color
plt.plot(df['Memory used (MB)'], n, linestyle='-', c='black', linewidth=3.5)
plt.fill_between(df['Memory used (MB)'], 0, n, color='red', alpha=0.5)
plt.gca().set_title('Relationship between memory usage and n for Heap sort',
                    fontsize=16, loc='left')  # setting the title with fontsize
# making a label for the x axis
plt.gca().set_xlabel('Memory used (MB)', fontsize=13)
# making a label for the y axis with no rotation on it
plt.gca().set_ylabel('n', rotation=0, fontsize=13)
plt.gca().margins(x=0, y=0)  # making sure the line fits the corners of the graph
plt.xticks(fontsize=8)  # setting the x axis tick's font size
plt.yticks(fontsize=10)  # setting the y axis tick's font size
plt.tight_layout()  # giving the subplot graph a tight layout
plt.show()  # showing the final graph
