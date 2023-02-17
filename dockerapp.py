def findDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]
duplicate=findDuplicate([1,3,4,2,2])
print(duplicate)