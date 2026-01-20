
# def anagram(str1,str2):
#     if str1.length()!=str2.length():
#         return False
#     charCounts=[]
#     for i in range(str1.lenth):
#         charCounts[(str1.charAt(i)='a')]+=1
#         charCounts[(str2.charAt(i)='a')]-=1

#     for i in charCounts:
#         if i!=0:s
#             return False
#     return True

def anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    sortstr1=sorted(str1.lower())
    sortstr2=sorted(str2.lower())
    if sortstr1==sortstr2:
        return True
    return False
print(anagram("cat","Cat"))

# Given an array of words arr[], the task is to groups strings that are anagrams. An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

# Example:

# Input: arr[] = ["act", "god", "cat", "dog", "tac"]
# Output: [["act", "cat", "tac"], ["god", "dog"]]
# Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.

# Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
# Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"],["rat", "tar", "art"]]
# Explanation: 
# Group 1: "abc", "bac" and "cab" are anagrams.
# Group 2: "listen", "silent" and "enlist" are anagrams.
# Group 3: "rat", "tar" and "art" are anagrams.

MAX_CHAR=26
def getHash(s):
    hashlist=[]
    freq=[0]*MAX_CHAR
    for ch in s:
        freq[ord(ch)-ord('a')]+=1
    for i in range(MAX_CHAR):
        hashlist.append(str(freq[i]))
        hashlist.append("$")
    return "".join(hashlist)
def anagrams(array):
    res=[]
    mp={}
    for i in range(len(array)):
        key=getHash(array[i])
        if key not in mp:
            mp[key]=len(res)
            res.append([])
        res[mp[key]].append(array[i])
    return res

if __name__ == "__main__":
    arr = ["act", "god", "cat", "dog", "tac"]
    
    res = anagrams(arr)
    for group in res:
        for word in group:
            print(word, end=" ")
        print()