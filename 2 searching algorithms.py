# linear search (for) (linear) Big Oh notation O(n)
def linear_search(A, target):
  for i in range(len(A)):
    if A[i] == target: # found
      return i
  return "not found" # not found

# 2 linear search (while)
def linear_search(A, target):
  i = 0
  while i < len(A):
    if A[i] == target: # found
      return i
    i += 1
  return "not found" # not found

# recursive binary search (logarithmic) O(lg n)

def binary_search_recursive(arr, target, low, high):
  if low > high:
  return "not found"  # Target not found in the array
  mid = (low + high) // 2  # Calculate the middle index
  if arr[mid] == target:
      return mid  # Target found at the middle index
  if arr[mid] < target:
      return binary_search_recursive(arr, target, mid + 1, high)  # Target is in the right half
  else:
      return binary_search_recursive(arr, target, low, mid - 1)  # Target is in the left half
