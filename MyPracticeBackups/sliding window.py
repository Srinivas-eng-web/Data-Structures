#find the length of the longest substring  that contains most k  distinct characters
#1. brute force
# def longest_k_distinct_brute(s,k):
#     max_len = 0
#     for i in range(len(s)):
#         unique_chars = set()
#         for j in range(i,len(s)):
#             unique_chars.add(s[j])
#
#             if len(unique_chars) <= k:
#                 max_len = max(max_len,j-i+1)
#             else:
#                 break
#     return max_len
# s = "eceba"
# k = 2
# print(longest_k_distinct_brute(s,k))

# Sliding Window + HashMap (Variable Window Size):
# def longest_k_distinct(s,k):
#     start = 0
#     max_len = 0
#     freq = {}
#
#     for end in range(len(s)):
#         right_char = s[end]
#         freq[right_char] = freq.get(right_char,0)+1
#         while len(freq) > k:
#             left_char  = s[start]
#             freq[left_char] -= 1
#             if freq[left_char] == 0:
#                 del freq[left_char]
#             start += 1
#
#         max_len = max(max_len,end-start+1)
#     return max_len
# s = "eceba"
# k = 2
# print(longest_k_distinct(s,k))


# Problem: Longest Substring with All Distinct Characters
#Find the length of the longest substring with no repeating characters.


#brute force method
# def longest_unique_char(s):
#     max_len = 0
#     for i in range(len(s)):
#         seen = set()
#         for j in range(i,len(s)):
#             if s[j] in seen:
#                 break
#             seen.add(s[j])
#             max_len = max(max_len,j-i+1)
#     return max_len
# print(longest_unique_char("abcabcbb"))

#sliding window tech

# def longest_substring_unique(s):
#     start = 0
#     max_len = 0
#     freq = {}
#
#     for i in range(len(s)):
#         char = s[i]
#
#         freq[char] = freq.get(char,0)+1
#         while freq[char] >1:
#             freq[s[start]] -= 1
#             start += 1
#         max_len = max(max_len,i-start+1)
#     return max_len
# print(longest_substring_unique("abcc"))

# Find the length of the longest substring in which we can change at most k characters to make all characters the same.

# def char_replacement(s,k):
#     freq = {}
#     max_freq = 0
#     start = 0
#     max_len = 0
#
#     for end in in range(len(s)):
#         right_char = s[end]
#         freq[right_char] = freq.get(right_char ,0)+1
#         max_freq = max(max_freq,freq[right_char])
#
#         if (end-start+1) - max_freq >k:
#             left_char = s[start]
#             freq[right_char] -= 1
#             start += 1
#
#         max_len = max(max_len,end-start+1)
#     return max_len
# print(char_replacement(s="AABABBA",k=1))



