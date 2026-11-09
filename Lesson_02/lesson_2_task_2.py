def is_year_leap(year):
    [pylance^^10,4,5,6,7,8,9]
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

test_year = 2020
result = is_year_leap(test_year)
print(f"год {test_year}:", result)