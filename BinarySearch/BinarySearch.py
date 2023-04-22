def search(nums=[1,8,9,7,4], target=9):
    # Note: the Big O of Binary Search is O(log n).

    left = 0  # start of array
    right = len(nums) - 1  # end of array

    while left <= right:  # because imagine if you array was just [1] and target 2, l=1 and r = 0 which is not allowed.

        middle = (left + right) // 2
        # alt to above to prevent overflow -> middle = left + (right - left) // 2

        if nums[middle] > target:
            right = middle - 1  # -1 because we dont want to include the middle index
        elif nums[middle] < target:
            left = middle + 1  # +1 because we dont want to include the middle index
        else:  # when we have found target

            return middle

    # if the target isn't inside the array
    return -1


print(search())