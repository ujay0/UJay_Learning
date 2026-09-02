# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def zero_sum_permutations(nums):
  nums = sorted(nums)
  results = []
  path = []
  used = [False] * len(nums)
  
  def backtrack(remaining_sum):
    if path and remaining_sum == 0:
        results.append(tuple(path))
	  
    for i, value in enumerate(nums):
        if used[i]:
            continue
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue
        if remaining_sum >= 0 and value > remaining_sum:
            break
        used[i] = True
        path.append(value)
	  
        backtrack(remaining_sum - value)
	  
        path.pop()
        used[i] = False
  backtrack(0)
  return results

	
nums = [-2, -1, 0,1]
print(zero_sum_permutations(nums))