def twoNumberSum(array, targetSum):
    # Write your code here.
	ans = {}
	for num in array:
		check_num = targetSum - num
		if check_num in ans:
			return [check_num, num]
		else:
			ans[num] = True
	return []