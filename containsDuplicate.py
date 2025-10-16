def duplicate(nums):
    numsSet = set()
    for num in nums:
        if num in numsSet:
            return True
        numsSet.add(num)
    return False    
if __name__ == "__main__":
    print(duplicate([1,2,3,1]))  # Output: True
    print(duplicate([1,2,3,4]))  # Output: False
    print(duplicate([1,1,1,3,3,4,3,2,4,2]))  # Output: True