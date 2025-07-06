# Print all elements in reverse.
# By using Slicing method
def reverse(arr):
    return arr[::-1]
print(reverse(arr=[1,2,3,4,5]))

#By using two-pointer approach, which is efficient (O(n/2) = O(n)).
def reverse_arr(arr):
   l ,r = 0 , len(arr)-1
   while l < r:
       if arr[l] < arr[r]:
           arr[l],arr[r] = arr[r] ,arr[l]
       l += 1
       r -= 1
   return arr
print(reverse_arr(arr=[1,2,3]))


#find maximum element in the array
def max_element(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
print(max_element(arr=[1,2,3,4,5,6]))

#Find the sum of all elements in the array (without using sum()).
def sum_of_all(arr):
    if not arr:
        return None

    total = 0
    lenght = len(arr)
    for num in arr:
        total += num
    return total, total/lenght

total,avg = sum_of_all(arr=[1,2,3,4,5])
print("total" ,total)
print("avg" , avg)


# Write a function that takes an array and a target value, and
# returns the index of the target if it exists. If the target is not found, return -1.
def linear_search(arr,target):

    for num in range(len(arr)):
        if arr[num] == target:
            return num

    return -1
arr = [1,2,3,4,5,6]
target = 3
print(linear_search(arr,target))

# counting the no,of occurence of the element in the array
def linear_search(arr,target):
    count = 0
    for i,num in enumerate(arr):
        if num == target:
            count += 1

    return count
print(linear_search(arr=[1,2,3,4,5,1,1],target=1))

def delete_at_index(arr, index):
    if index < 0 or index >= len(arr):
        return "Index out of range"
    del arr[index]
    return arr

print(delete_at_index(arr=[1, 2, 3, 4, 5], index=2))

#Write a function that inserts a given value at a specific index in the array.
def insert_at_position(arr, index, value): #function signature
    arr.insert(index,value)
    return arr

# print(insert_at_position(arr=[1, 2, 4, 5],index=2 ,value=3))
# Write a function that deletes the element at a given index from the array.

def delete_at_index(arr, target):
    return [num for num in arr if num != target]   #using list compreshisions

print(delete_at_index(arr=[1,2,3,3,3,3,4],target=3))

def second_largest(arr):
   first = second = float('-inf')

   for num in arr:
       if num > first:
           second = first
           first = num
       elif first > num > second:
           second  = num
   return second if num != float('-inf') else None

print(second_largest(arr=[1,2,3,4,5,1]))

# Binary Search
# Repeatedly divide the search space in half.
#
# works only sorted arrays
# time complexity O(log n)

def binary_search(arr,target):
    low , high = 0,len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid-1
    return -1
result = binary_search(arr=[1,2,3,4,5,6,],target=9)
print(result)

# What is Sliding Window?
# The Sliding Window technique is a smart way to avoid repeating work when you're processing subarrays (or substrings) in a row.
#
# Instead of checking every possible subarray (which is slow), you "slide" a fixed-size window over the array and update the result in-place — saving time.
#  Sliding Window Idea (Efficient)
# Compute sum of first k elements — that’s your first window.
#
# Then slide the window 1 step at a time:
#
# Add the new element at the end
#
# Remove the element at the start
#
# Keep track of the max sum
#
#  Time: O(n)
def sliding_window(arr,k):
    if len(arr)< k :
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k,len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum,window_sum)

    return max_sum
print(sliding_window([1, 2, 3, 4, 5], 3))  # Output: 12



def brute_force(arr,k):
    if len(arr) <k :
        return None

    max_sum = float('-inf')
    for i in range(len(arr)-k+1):
        current_sum = 0
        for j in range(i,i+k):
            current_sum += arr[j]

        max_sum = max(max_sum,current_sum)
    return max_sum
print(brute_force(arr=[1, 2, 3, 4, 5],k=3))


# Find the maximum sum of a subarray of size k in an array.
# Core Idea (Why it's fast):
# Instead of recalculating the sum from scratch each time, we:
#
# Subtract the element going out of the window
#
# Add the new element coming into the window
#
# So we update the sum in constant time → O(1)
# This gives us overall O(n) time — much faster!

def sliding_window(arr,k):
    sliding_sum = sum(arr[:k])
    max_sum = sliding_sum

    for i in range(k,len(arr)):
        sliding_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum,sliding_sum)

    return max_sum
result = sliding_window(arr=[1,2,3,4,1,1,2,4],k=2)
print(result)

# "Find the length of the longest subarray with sum ≤ k"
def variable_length(arr,target):
    start = 0
    current_sum = 0
    max_length = 0
    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > target:
            current_sum -= arr[start]
            start += 1

        max_length = max(max_length,end-start+1)
    return max_length

arr = [1, 2, 1, 0, 1, 1, 0]
target = 4
print(variable_length(arr,target))



#repeated swapped the adjacent elements which they are in wrong order
def bubble_sort(arr):

    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr
print(bubble_sort([5, 1, 4, 2]))

# It builds the sorted array one element at a time — by placing each
# element in its correct position among the previous (already sorted) elements.

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr
arr = [5,1,4,2]

print(insertion_sort(arr))

# Classic Example 1: Pair With Target Sum
# Given a sorted array, find if there exists a pair whose sum is equal to a target.

def two_pointers(arr,target):
    left ,right = 0 ,len(arr)-1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return (arr[left],arr[right])
        elif current > target:
            right -= 1
        else:
            left += 1

    return None

arr = [1, 2, 3, 4, 6]
target = 6

print(two_pointers(arr,target))

# Remove duplicates problem

def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return arr[:i + 1]  # Return only the unique portio
arr = [1,2,3,4,2,2]

# checking target element sum is in the array or not
def two_sum(arr,target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)

    return False

# Hashing counting frequency

def count_freq(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq
arr = [1,1,2,2,3,4,4,3,2,5]
print(count_freq(arr))


def first_repeating_element(arr):
    s = set()
    for num in arr:
        if num in s:
            return num
        s.add(num)

    return None
print(first_repeating_element(arr=[1,2,4,4,2,2,2,8]))

def most_freq_element(arr):
    freq = {}
    max_count = 0
    most_frq = None
    for num in arr:
        freq[num] = freq.get(num,0) + 1

        if freq[num] > max_count:
            max_count

def max_count_num(arr):
    freq = {}
    max_count = 0
    most_frequent = None
    for num in arr:
        freq[num] = freq.get(num,0) + 1

        if freq[num] > max_count:
            max_count = freq[num]
            most_frequent = num

    return most_frequent
print(max_count_num(arr=[1,2,2,1,2,3,4,5,6]))

def arr_count(arr):
    dic = {}
    count = 0
    for num in arr:
        dic[num] = dic.get(num,0) +1
        # if num in dic:
        #     dic[num] += 1
        # else:
        #     dic[num] =1

    for num in dic:
        if dic[num] == 1:
            return num
    return None

arr = [2, 3, 2, 5, 3, 2]
print(arr_count(arr))
#
# prefix sum may sound techniqcal ,but it has superpower
# Turn repeated addition into instant answers
def build_prefix_sum(arr):
    prefix = [0] * len(arr)           # Step 1: create an empty list of same size
    prefix[0] = arr[0]                # Step 2: first element is same as arr[0]

    for i in range(1, len(arr)):      # Step 3: build prefix sums
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix

# problem
def build_prefix_sum(arr):
    prefix = [0] *len(arr)
    prefix[0] = arr[0]

    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix
print(build_prefix_sum(arr=[1,2,3,4]))


def sum_range_query(arr,L,R):
    prefix = [0] *len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    if L == 0:
        return prefix[R]
    else:
        return prefix[R] - prefix[L-1]
arr = [3, 5, 2, 8, 6]
L = 1
R = 3
print(sum_range_query(arr, L, R))  # Output: 15



def subarray(arr,target):
    prefix_sum = 0
    seen = set()
    for num in arr:
        prefix_sum += num
        if prefix_sum == target or (prefix_sum- target) in seen:
            return True
        seen.add(prefix_sum)
    return False
#Test case

arr = [3, 4, -2, 7, 1, 5]
target = 8
print(subarray(arr, target))  # Output: True


#counting the subarrays of the given sum

from collections import defaultdict
def count_subarray(arr,target):
    prefix_sum = 0
    count = 0
    freq = defaultdict(int)
    freq[0] = 1
    for num in arr:
        prefix_sum += num
        count += freq[prefix_sum-target]
        freq[prefix_sum] += 1

    return count
arr = [1,2,3,-2,5]
print(count_subarray(arr,target=5))

#----------------------------------Two Pointers -------------->
""" A technque which is involved 2 indices to iterate over the data structure of strings or arrays
from different directions or at different speeds"""

#Reverse a array in place
#Problem: Given arr = [1, 2, 3, 4, 5], reverse the array without using extra space.

def reverse_arr(arr):
    left ,right = 0 , len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right],arr[left]

        left += 1
        right -= 1

    return arr
arr = [1,2,3,4,5]
result = reverse(arr)
print(f"reverse array in a place :{result}")  # output : reverse array in a place :[5, 4, 3, 2, 1]

#Example 2: Check if String is Palindrome

def palin(s):
    left,right = 0,len(s)-1

    while left < right:
        if s[left] != s[right]:

            return False

        left += 1
        right -= 1
    return True

print(f"checking given string is palin or not : {palin(s="Srinivas")}")  #False

print(f"checking given string is palin or not : {palin(s="radar")}") # True

#Problem: Two Sum II – Input Array Is Sorted
# Given a sorted array of integers numbers, find two numbers such that they add up to a specific target.
# Return the indices (1-based) of the two numbers.
def two_sum(arr,target):
    left,right = 0,len(arr)-1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left+1,right+1]
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    #return []

print(f"the value of the sum is target:,{two_sum(arr=[2,7,11,15] ,target=9)}")


#Problem: Check if a string is a palindrome(ignore spaces, punctuation, and case).


def is_palin(s):
    rm =  "".join(r.lower() for r in s if r.isalnum())
    print(rm)

    l, r = 0,len(rm)-1
    while l < r:
        if rm[l] != rm[r]:
            return False
        l += 1
        r -= 1
    return True

print(is_palin(s="Sri niv aS"))

#Problem: In a sorted array, remove duplicates in-place and return the length of unique elements.

#?

def remove_dup(arr):
    if not arr:
        return 0

    slow = 0
    for fast in range(1,len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1

            arr[slow] = arr[fast]
    return slow+1

arr = [1,2,2,2,3,4,99]
k = remove_dup(arr)
print("After removing the duplicates from the arary:", format(arr[:k]))

#Problem: Merge two sorted arrays into a single sorted array.

def merge_sorted(a,b):

    result = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1

        else:
            result.append(b[j])
            j += 1

    #add remaining

    result.extend(a[i:])
    result.extend(b[j:])
    return result
a = [1, 3, 5]
b = [2, 4, 6]
print(merge_sorted(a, b))

#Move Zeros to End
#Move all 0s to the end of the array while keeping the order of other elements.

def move_zero_to_end(arr):
    non_zero_pos = 0

    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[non_zero_pos],arr[fast] = arr[fast],arr[non_zero_pos]
            non_zero_pos += 1

    return arr
print("moved zeros to end: ", move_zero_to_end(arr=[1,0,0,2,3,9,0,10]))


#Goal: Find two heights that form the container holding the most water.

def finding_height(height):
    left = 0
    right = len(height)-1
    max_water = 0

    while left < right:
        width = right - left
        water = width * min(height[left],height[right])
        max_water = max(max_water,water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
height =  [ 1, 8, 6, 2, 5, 4, 8 ]

print("max height of water :",finding_height(height))


