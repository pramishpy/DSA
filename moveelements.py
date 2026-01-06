"""Given an array of sorted numbers, move all non-duplicate number instances at the beginning of the array in-place.
 The non-duplicate numbers should be sorted and you should not use any extra space so that the solution has constant space complexity i.e., .
Move all the unique number instances at the beginning of the array and after moving return the length of the subarray that has no duplicate in it."""

class Solution:
  def moveElements(self, arr):
    # Edge case: empty array
    if not arr:
      return 0
    # Initialize two pointers
    sptr, fptr = 0, 1
    # Iterate through the array
    while fptr < len(arr):
      # If the elements at the two pointers are different, we found a unique element
      if arr[sptr] != arr[fptr]:
        # Increment the slow pointer and swap the elements
        sptr += 1
        arr[sptr], arr[fptr] = arr[fptr], arr[sptr]
      # Move the fast pointer forward  
      fptr += 1
    # Return the length of the subarray with unique elements  
    return sptr + 1
  
  def moveElements2(self, arr):
    if not arr:
      return 0
    next_non_duplicate = 1
    for i in range(1, len(arr)):
      if arr[next_non_duplicate - 1] != arr[i]:
        arr[next_non_duplicate] = arr[i]
        next_non_duplicate += 1
    return next_non_duplicate
  
if __name__ == "__main__":
  arr = [2, 3, 3, 3, 6, 9, 9]
  print(Solution().moveElements(arr))  # Output: 4
  print(arr[:4])                       # Output: [2, 3, 6, 9]

  arr = [2, 2, 2, 11]
  print(Solution().moveElements(arr))  # Output: 2
  print(arr[:2])                       # Output: [2, 11]

  arr = [2, 3, 3, 3, 6, 9, 9]
  print(Solution().moveElements2(arr))  # Output: 4
  print(arr[:4])