# Reverse an Array

# def reverse_array(arr):
#     return arr[::-1]
# print(reverse_array(arr=[1,2,3,4])) # using slicing

# two  pointers technique
# def rev_array(arr):
    # left, right = 0,len(arr)-1
    #
    #
    # while left < right:
    #         arr[left],arr[right] = arr[right] ,arr[left]
    #
    #     left += 1
    #     right -= 1
    # return arr
#     return list(reversed(arr))
# print(rev_array(arr=[1,2,3,4]))

# def reverse_in_grps(arr,k):
#     n = len(arr)
#     for i in range(0,n,k):
#         left = i
#         right = min(i+k-1,n-1)
#         while left < right:
#             arr[left],arr[right] = arr[right],arr[left]
#
#             left += 1
#             right -= 1
#
#     return arr
# print(reverse_in_grps(arr=[1,2,3,4,5,6,7,8],k=3))




# Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up to target.

# Approach 1: Brute Force (Nested Loops) – O(n²)
# def two_sum(arr,target):
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             if arr[i] + arr[j] == target:
#                 return [i,j]

# print(two_sum(arr=[2,7,11,15],target=9))

# Approach 2: Hash Map (Optimal) – O(n)
# def two_sum(arr,target):
#     seen = {}
#
#     for i,num in enumerate(arr):
#         diff = target - num
#
#         if diff in seen:
#             return [seen[diff],i]
#         seen[num] = i
#
# print(two_sum(arr=[3,2,4],target=6))

def two_sum(arr,target):
    seen = {}
    for i ,num in enumerate(arr)
        diff = target - num
        if diff in seen:
            return [seen[diff],i]
        seen[num] = i

# Given an array nums, move all 0s to the end of it
# while maintaining the relative order of the non-zero elements.
# Do it in-place with minimum operations.

# def move_zeros_end(arr):
#     non_zero_pos = 0
#     for right in range(len(arr)):
#         if arr[right] != 0:
#             arr[non_zero_pos] = arr[right]
#             non_zero_pos += 1
#     for i in range(non_zero_pos,len(arr)):
#         arr[i] = 0
#
#     return arr
# print(move_zeros_end(arr=[1,2,0,2,0,1,2,0,1,1,1]))

def move_zeroes_end(arr):
    non_zero_pos = 0
    for right in range(len(arr)):
        if arr[right] != 0:
            arr[non_zero_pos] =arr[right]
            non_zero_pos += 1
    for i in range(non_zero_pos,len(arr)):
        arr[i] = 0
    return  arr
#Given two strings s and t, return True if t is an anagram of s, and False otherwise.
#An anagram is formed by rearranging the letters of a word to produce a new word, using all original letters exactly once.

# def anagram(a,b):
#     return sorted(a) == sorted(b)
#
# print(anagram(a="anagram",b="nagaram"))

# from collections import Counter
# def is_anagram(a,b):
#     return Counter(a) == Counter(b)
# print(is_anagram(a="silent",b="listen"))

#Given a string, find the length of the longest substring without repeating characters.

# def length_of_longest_substring(s):
#     seen = {}
#     max_length = 0
#     start = 0
#     for end in range(len(s)):
#         ch = s[end]
#
#         if ch in seen and seen[ch] >=start:
#             start = seen[ch]+1
#         seen[ch] = end
#         max_length = max(max_length,end-start+1)
#
#     return max_length
# print(length_of_longest_substring(s="sriiiiini"))
def long_sub_string(s):
    seen = {}
    max_len = 0
    start = 0
    for end in range(len(arr)):
        ch = s[end]

        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = end
        max_len = max(max_len,end-start+1)

def long_sub(s):
    seen = {}
    max_length = 0
    start = 0
    for end in range(len(arr)):
        char = arr[end]

        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = end
        max_length = max(max_length,end-start+1)
    return max_length

# def longest_sub_string(s):
#     seen = {}
#     max_len = 0
#     start = 0
#     for end in range(len(s)):
#         ch = s[end]
#         if ch in seen and seen[ch] >= start:
#             start = seen[ch]+1
#         seen[ch] = end
#         max_len = max(max_len,end-start+1)
#
#     return max_len
# print(longest_sub_string(s="srinivi")

# def sliding_window(arr,k):
#     window_size = sum(arr[:k])
#     max_window = window_size
#
#     for i in range(k,len(arr)):
#         window_size += arr[i] - arr[i-k]
#         max_window = max(window_size,max_window)
#     return max_window
# print(sliding_window(arr=[1,2,3,4,5],k=2))
# Maximum sum brute force method
# def max_sum_brute(arr,k):
#     max_sum = float('-inf')
#     for i in range(len(arr)-k+1):
#         current_sum = sum(arr[i:i+k])
#
#         max_sum = max(current_sum,max_sum)
#     return max_sum
# print(max_sum_brute(arr=[1,2,3,4,5],k=2))
# def sliding_window(target,nums):
#     left = 0
#     total = 0
#     min_len = float('inf')
#     for right in range(len(nums)):
#         total += nums[right]
#         while total >= target:
#             min_len = min(min_len,right-left+1)
#             total -= nums[left]
#             left += 1
#
#     return min_len if min_len != float('inf') else 0
# print(sliding_window(target=7 ,nums= [2,3,1,2,4,3]))

# def sliding_window(arr,target):
#     left = 0
#     total = 0
#     min_lenght = float('inf')
#     for right in range(len(arr)):
#         total += arr[right]
#         while total >= target:
#             min_lenght = min(min_lenght,right-left+1)
#             total -= nums[left]
#             left +=1
#     return min_lenght if min_lenght != float('inf') else 0


# def window_size(arr,k):
#     window_s = sum(arr[:k])
#     max_sum = window_s
#     for num in range(k,len(arr)):
#         window_s += arr[num] -arr[num-k]
#         max_sum = max(max_sum,window_s)
#     return max_sum/k
# print(window_size(arr=[1,12,-5,-6,50,3],k=4))

# Find the average of all contiguous subarrays of size k in an array.

# 📥 Input: arr = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5
# 📤 Output: [2.2, 2.8, 2.4, 3.6, 4.4]

# def contin_sub_array(arr,k):
#     avg_new = []
#     for i in range(len(arr)-k+1):
#          current_sum = sum(arr[i:i+k])
#          avg = current_sum/k
#          avg_new.append(avg)
#     return avg_new
# print(contin_sub_array(arr=[1,3,2,6,-1,4,1,8,2],k=5))

# def contin_sub_slid(arr,k):
#     window_size = sum(arr[:k])
#     avg = [window_size/k]
#     for i in range(k,len(arr)):
#         window_size += arr[i] - arr[i-k]
#         avg.append(window_size/k)
#     return avg
# print(contin_sub_slid(arr=[1,3,2,6,-1,4,1,8,2],k=5))

# Find the length of the longest subarray with sum ≤ S
# arr = [4, 1, 1, 1, 2, 3, 5]
# S = 5


# def longest_sub_array(arr,s):
#     total = 0
#     start = 0
#     max_len = 0
#     for end in range(len(arr)):
#         total += arr[end]
#
#         while total >= s:
#             total -= arr[start]
#             start += 1
#
#         max_len = max(max_len,end-start+1)
#     return max_len
# print(longest_sub_array(arr=[4,1,1,1,2,3,5],s=5))


# Find the length of the longest contiguous subarray whose sum is ≤ s using sliding window.

# def longest_sub_array(arr,s):
#     start = 0
#     total = 0
#     max_len = 0
#     for end in range(len(arr)):
#         total += arr[end]
#
#         while total > s:
#             total = total - arr[start]
#             start += 1
#         max_len = max(max_len,end-start+1)
#     return max_len
# arr = [4, 1, 1, 1, 2, 3, 5]
# s = 5
# print(longest_sub_array(arr,s))
# def brute_force_max_len(arr,s):
#     max_len = 0
#     for start in range(len(arr)):
#         total = 0
#         for end in range(start,len(arr)):
#             total += arr[end]
#
#             if total <= s:
#                 max_len = max(max_len,end-start+1)
#             else:
#                 break
#         return max_len
# arr = [4, 1, 1, 1, 2, 3, 5]
# s = 5
# print(brute_force_max_len(arr,s))
# Given an array of positive integers and a number S, find the length of the smallest contiguous subarray
# whose sum is greater than or equal to S. Return 0 if no such subarray exists
# def smallest_sub_array(arr,s):
#     start = 0
#     mini_len = float('inf')
#     total = 0
#
#     for end in range(len(arr)):
#         total += arr[end]
#
#         while total >= s:
#             mini_len  = min(mini_len,end-start+1)
#             total -= arr[start]
#             start +=1
#     return mini_len if mini_len != float('inf') else 0
# arr = [2, 1, 5, 2, 3, 2]
# s = 7
# print(smallest_sub_array(arr,s))

# def smallest_sub_array(arr,s):
#     start = 0
#     mini_len = float('inf')
#     total = 0
#     for end in range(len(arr)):
#         total += arr[end]
#
#         while total >= s:
#             mini_len = min(mini_len,end-start+1)
#             total -= arr[start]
#             start += 1
#     return mini_len if mini_len != float('inf') else 0
# print(smallest_sub_array())



def longest_sub_string(s):
    seen = {} # to store last index of charcters
    max_length = 0 # Final result
    start = 0  # start of current window
    for end in range(len(arr)):  # 'end' is the right end of the window
        ch = s[end]
        # If character is repeated AND its index is within current window
        if ch in seen and seen[ch] >= start:
            start = seen[ch] +1 # Move 'start' right after the repeated character
        seen[ch] = end  #Update the last seen index of the character

        max_length = max(max_length,end-start+1)  #Update result if needed

    return max_length

def longest_sub_string(s):
    seen = {}
    max_length = 0
    start = 0
    for end in range(len(arr)):
        ch = s[end]

        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1

        seen[ch] = end
    