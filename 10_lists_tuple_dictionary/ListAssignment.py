# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [24,24,52]

# Create a tuple, called my_tuple, with a single value in it
my_tuple = (12)

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5}
set2.add(77)
set2.add(9)
set2.add(12)

print(sorted(set1.intersection(set2)))