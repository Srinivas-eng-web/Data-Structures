
#Valid anagram or not

# def anagram(s1,s2):
#     if len(s1) != len(s2):
#         return False
#     else:
#         return sorted(s1) == sorted(s2)
# # print(anagram(s1="listen",s2="silent"))
#
# from collections import Counter
#
# def is_anagram_counter(s1,s2):
#     if len(s1) != len(s2):
#         return False
#     return Counter(s1) == Counter(s2)
# print(is_anagram_counter("silent","listen"))
#
def areangrams(s1,s2):
    charcount = {}
    for char in s1:
        charcount[char] = charcount.get(char,0)+1
    for char in s2:
        charcount[char] = charcount.get(char,0)-1

    for value in charcount.values():
        if value != 0:
            return False

    return True

#Longest substring  without Repeating charcters
def longest_sub_String(s):
    max_len = 0
    start = 0
    seen = {}
    for end in range(len(s)):
        char = arr[end]
        if char in seen and seen[char] >= start:
            start  = seen[ch]+1
        seen[ch] = end
        max_len = max_len(max_len,end+start+1)
    return max_len

s = "abcabcbb"
