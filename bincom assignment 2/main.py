import os
import re

# Assignments

# (1) Create a text file that has your full name, and write code to read it
# and extract firstname, surname and lastname
# read the file
with open('names.txt', 'r') as full_name_fetch:
    full_name_render = full_name_fetch.read().strip()
    print(full_name_render)

# extract first name, surname and last name
first_name, surname, last_name = full_name_render.split()
print(f'First Name: {first_name}')
print(f'Surname: {surname}')
print(f'Last Name: {last_name}')

# (2) Using os library, print your local file path on screen
# Output current working directory (cwd)
print(os.getcwd())


# (3) Extract baby names from HTML files using Regex
fetch_baby_names = open('baby_names.html', 'r')
render_baby_names = fetch_baby_names.read()
baby_names = re.findall(r'<li>(\w+)</li>', render_baby_names)
print(baby_names)

# (4) Implement a sorting algorithm without using built-in libraries


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# checking:
# numbers = [64, 34, 25, 12, 22, 11, 90]
index = binary_search(numbers, 25)
print(sorted_numbers)
print(index)
