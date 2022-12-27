def divide(dividend, divisor):
    return dividend / divisor


grades = []
print("Welcome to the grading program")
try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}")
except ZeroDivisionError as e:
    print("There are no grades in your list")
