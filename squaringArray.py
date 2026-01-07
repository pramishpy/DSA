class Solution:
  def makeSquares(self, arr):
    n = len(arr)
    squares = [0] * n
    left, right = 0, n - 1
    
    for i in range(n - 1, -1, -1):
      if abs(arr[left]) > abs(arr[right]):
        squares[i] = arr[left] ** 2
        left += 1
      else:
        squares[i] = arr[right] ** 2
        right -= 1
    return squares
  
if __name__ == "__main__":
  arr = [-2, -1, 0, 2, 3]
  print(Solution().makeSquares(arr))  # Output: [4, 1, 0, 4, 9]

  arr = [-3, -1, 0, 1, 2]
  print(Solution().makeSquares(arr))  # Output: [9, 1, 0, 1, 4]