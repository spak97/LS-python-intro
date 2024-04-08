# because you're not incrementing counter and counter is forever 0
age = int(input('How old are you? '))

age_range = [10, 20, 30, 40]
for i in age_range:
    print(f"In {i} years, you will be {age + i} years old")
