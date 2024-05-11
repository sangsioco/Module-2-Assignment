# Task 1: Validating Calculation

# Arithmetic expression
result_normal = 3 * 5 + 20
result_with_parentheses = (3 * 5) + 7

# Compare the results
if result_normal == result_with_parentheses:
    print("Results match!")
else:
    print("Results don't match.")

print("Result normally:", result_normal)
print("Result with parentheses:", result_with_parentheses)


#Task 2: Mix and Match

# Expression
outcome_prediction = (27 > 12) or (3 + 2 > 6)
print("Predicted outcome:", outcome_prediction)

# Computing the expression
actual_outcome = (27 > 12) or (3 + 2 > 6)
print("Actual outcome:", actual_outcome)