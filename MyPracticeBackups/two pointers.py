#reverse a string

# def reverse_str(arr):
#     return arr[::-1]
# print(reverse_str(arr=["h","e","l","l","o"]))

# def reverse_string(arr):
#     left ,right = 0 ,len(arr)-1
#     while left < right:
#         arr[left],arr[right] = arr[right],arr[left]
#
#         left += 1
#         right -= 1
#     return arr
# print(reverse_string(arr=["h","l","l","e","o"]))

#two sum (Sorted array) ->

# def two_sum(arr,target):
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             if arr[i] + arr[j] == target:
#                 return [i,j]
# print(two_sum(arr=[1,2,3,4,5,7],target=9))

# def two_sum(arr,target):
#     left ,right  = 0 ,len(arr)-1
#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == target:
#             return left,right
#         elif current_sum > target:
#             right -= 1
#         else:
#             left += 1
# print(two_sum(arr=[1,2,3,4,5,6,7],target=9))

# def two_sum(arr,target):
#     seen = {}
#     for i,num in enumerate(arr):
#         diff = target -num
#         if diff in seen:
#             return [seen[diff],i]
#         seen[num] = i
# arr = [1,2,3,4,5,6]
# target = 5
# print(two_sum(arr,target))


# Given an array of integers, move all the 0s to the end while maintaining the relative order of the non-zero elements.

# def move_zeros_end(arr):
#
#     non_zero_pos = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[non_zero_pos] = arr[i]
#             non_zero_pos += 1
#     for j in range(non_zero_pos,len(arr)):
#         arr[i] = 0
#
#     return arr
# print(move_zeros_end([0, 1, 0, 3, 12]))

# def move_zeros_end(arr):
#     zeros = []
#     for i in arr:
#         if i != 0:
#             zeros.append(i)
#     Zero_count = len(arr) - len(zeros)
#     zeros += [0] * Zero_count
#
#     return zeros
# print(move_zeros_end(arr=[1,2,0,0,2,34]))



# def move_zeros_end(arr):
#     non_zero_pos = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[non_zero_pos] = arr[i]
#             non_zero_pos += 1
#
#     for i in range(non_zero_pos,len(arr)):
#         arr[i] = 0
#     return arr
# print(move_zeros_end(arr=[1,2,3,0,0,0,1,2,1]))
