def containsDuplicate(self, nums: List[int]) -> bool:
        # nums = [1,2,3,4]

        seen_numbers = set()

        for number in nums:
            if number in seen_numbers:
                return True
            else:
                seen_numbers.add(number)
        return False


def twoSum(self, nums: List[int], target: int) -> List[int]:
    seenNumbers = {}

    for index, number in enumerate(nums):

        otherNumber = target - number
        if otherNumber in seenNumbers:
            return [seenNumbers[otherNumber], index]
        else:
            seenNumbers[number] = index  # store it in seeNumbers

