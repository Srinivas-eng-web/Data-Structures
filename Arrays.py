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