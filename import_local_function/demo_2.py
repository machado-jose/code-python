from useful_functions import mean_list, add_five

scores = [88, 92, 79, 93, 85]

mean = mean_list(scores)
curved = add_five(scores)

mean_c = mean_list(curved)

print("Scores: ", scores)
print("Original Mean: ", mean, " New Mean: ", mean_c)