def mean_list(num_list):
	return sum(num_list) / len(num_list)

def add_five(num_list):
	return [n + 5 for n in num_list]

if __name__ == '__main__':
	print("Testing mean function")
	n_list = [34, 44, 23, 46, 12, 24]
	correct_mean = 30.5
	assert(mean_list(n_list) == correct_mean)

	print("Testing add_five function")
	correct_list = [39, 49, 28, 51, 17, 29]
	assert(correct_list == add_five(n_list))

	print("All tests passed!")