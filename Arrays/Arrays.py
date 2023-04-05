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

