#Given an array of numbers sorted in ascending order and a target sum, find a pair in the array whose sum is equal to the given target.
class Solution:
  def search(self, arr, target_sum):
    lpt, rpt = 0, len(arr) - 1
    while lpt < rpt:
      sumi = arr[lpt] + arr[rpt]
      if sumi == target_sum:
        return [lpt, rpt]
      elif sumi > target_sum:
        rpt -= 1
      else:
        lpt += 1 
    return [-1, -1]
  
if __name__ == "__main__":
  arr = [1, 2, 3, 4, 6]
  target_sum = 6
  print(Solution().search(arr, target_sum))  # Output: [1, 3]

  arr = [2, 5, 9, 11]
  target_sum = 11
  print(Solution().search(arr, target_sum))  # Output: [0, 2]