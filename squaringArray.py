class Solution:
  def makeSquares(self, arr):
    n = len(arr)
    squares = [(arr[x] ** 2) for x in range(n)]
    
    return squares
  
if __name__ == "__main__":
  arr = [-2, -1, 0, 2, 3]
  print(Solution().makeSquares(arr))  # Output: [4, 1, 0, 4, 9]

  arr = [-3, -1, 0, 1, 2]
  print(Solution().makeSquares(arr))  # Output: [9, 1, 0, 1, 4]