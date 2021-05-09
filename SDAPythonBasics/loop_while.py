
# Ask the user how many user's weights He wants to have the average.
# Type all of those average
# Print out the average of their weights

# "How many weights you want to type?"
# 3
# Type the weight 1: 77
# Type the weight 2: 34
# Type the weight 3: 56
# average_of_weights = (77 + 34 + 56) / 3

i = 0
sum_weight = 0

amount_of_weights = int(input("How many weights you want to type?"))

while i < amount_of_weights:
    weigth_str = input(f"Type your weight {i+1}: ")
    weight = float(weigth_str)

    sum_weight = sum_weight + weight # the same of sum_weight += weight

    i = i + 1

average_of_weights = sum_weight / amount_of_weights
print(f"The average for those weights is {average_of_weights}")