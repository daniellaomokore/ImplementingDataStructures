class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums = [1,2,3,4]

        seen_numbers = set()

        for number in nums:
            if number in seen_numbers:
                return True
            else:
                seen_numbers.add(number)
        return False
