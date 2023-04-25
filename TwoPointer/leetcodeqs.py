class Solution:
    def isPalindrome(self, s: str) -> bool:

        leftPointer = 0  # left pointer starts at index 0
        rightPointer = len(s) - 1  # starts at the end index of the list

        while leftPointer < rightPointer:  # while the pointers have index have not overlapped.

            ## PASS OVER NON-APLHANUMERIC VALUES BY INCREASING THE INDEX
            while leftPointer < rightPointer and not s[
                leftPointer].isalnum():  # while we have come across a non alphanumeric value in the left side
                leftPointer += 1  # increase the pointer index so that we skip over it

            while leftPointer < rightPointer and not s[
                rightPointer].isalnum():  # we have come across a non alphanumeric value in the right side

                rightPointer -= 1  # decrease the pointer index so that we skip over it

            if s[leftPointer].lower() != s[rightPointer].lower():  # while they are lowercase and if they aren't equal
                return False

                # PAMOVESS TO NEXT VALUE IN STRING IF THE STRING IS A PALINDOME SO FAR
            leftPointer += 1
            rightPointer -= 1

            # if they are never not equal return true as it's a palindrome

        return True

# Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:  # so they don't overlap

            sum = numbers[left] + numbers[right]

            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left + 1, right + 1]
