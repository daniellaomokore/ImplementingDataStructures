#set()  .add()
def containsDuplicate(self, nums: List[int]) -> bool:
        # nums = [1,2,3,4]

        seen_numbers = set()

        for number in nums:
            if number in seen_numbers:
                return True
            else:
                seen_numbers.add(number)
        return False

#enumerate()
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seenNumbers = {}

    for index, number in enumerate(nums):

        otherNumber = target - number
        if otherNumber in seenNumbers:
            return [seenNumbers[otherNumber], index]
        else:
            seenNumbers[number] = index  # store it in seeNumbers



#dict.get(key,value)
def isAnagram(self, s: str, t: str) -> bool:
        
        sCount={}
        tCount={}

        for letterS in s:
            sCount[letterS]=sCount.get(letterS,0)+1
        for letterT in t:
            tCount[letterT]=tCount.get(letterT,0)+1
        if sCount == tCount:
            return True
        else:
            return False

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

# or 2 pointer method which is a good DSA method + better for space
def isPalindrome(self, s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not (s[left]).isalnum():
            left += 1
        while left < right and not (s[right]).isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True




