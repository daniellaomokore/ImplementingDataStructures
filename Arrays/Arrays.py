#set()  .add()
def containsDuplicate(nums):
    seenNums = set()  # we use a set instead of an array because searching for an element in a set is O(1) as it's unordered, unlike searching arrays which is O(n) because you have to transverse through entire array by index.

    for integer in nums:
        if integer in seenNums:
            return True
        else:
            seenNums.add(integer)

    return False


#enumerate()
def twoSum(nums,target):
    seenNumbers = {}

    for index, number in enumerate(nums):

        otherNumber = target - number
        if otherNumber in seenNumbers:
            return [seenNumbers[otherNumber], index]
        else:
            seenNumbers[number] = index  # store it in seeNumbers




from collections import defaultdict
#BIG O/Time Complexity: O(n+m)
def isAnagram(self, s: str, t: str) -> bool:

        sCount = defaultdict(int)  # creates a dict which has the values default to 0
        tCount = defaultdict(int)

        for letterS in s:
            sCount[letterS]+=1
        for letterT in t:
            tCount[letterT]+=1
        if sCount == tCount:
            return True
        else:
            return False

#Use -> from collections import defaultdict



from collections import Counter

#BIG O/Time Complexity: O(n+m)
def isAnagram(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)



#[::-1]    - use this to reverse string, list, array, tuple etc
#.isalnum()   - returns True if something is alphanumeric(a letter and/or number only)
def isPalindrome(self, s: str) -> bool:
    fixedString = []
    for element in s:
        if element.isalnum() == True:
            fixedString.append(element.lower())
    if fixedString == fixedString[::-1]:
        return True
    else:
        return False

#or
def isPalindrome(self, s: str) -> bool:
        fixedString = []
        for element in s:
            if element.isalnum() == True:
                fixedString.append(element.lower())
        return fixedString == fixedString[::-1]


# or 2 pointer(left & right pointer) method which is a good DSA method + better for space
class Solution:
    def isPalindrome(self, s: str) -> bool:

        leftPointer = 0  # left pointer starts at index 0
        rightPointer = len(s) - 1  # starts at the end index of the list

        while leftPointer < rightPointer:  # while the pointers have index have not overlapped.

            ## PASS OVER NON-APLHANUMERIC VALUES BY INCREASING THE INDEX
            while leftPointer < rightPointer and not s[leftPointer].isalnum():  # while the pointers have index have not overlapped + we have come across a non alphanumeric value in the left side
                leftPointer += 1  # increase the pointer index so that we skip over it

            while leftPointer < rightPointer and not s[rightPointer].isalnum():  # while the pointers have index have not overlapped + we have come across a non alphanumeric value in the right side

                rightPointer -= 1  # decrease the pointer index so that we skip over it

            if s[leftPointer].lower() != s[rightPointer].lower():  # while they are lowercase and if they aren't equal
                return False

                # PAMOVESS TO NEXT VALUE IN STRING IF THE STRING IS A PALINDOME SO FAR
            leftPointer += 1
            rightPointer -= 1

            # if they are never not equal return true as it's a palindrome

        return True








