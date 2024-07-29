# Prompt the user for their current age
current_age = int(input("How old are you? "))

# Calculate how old the user will be in the year 2050
current_year = 2023
future_year = 2050
years_to_add = future_year - current_year
age_in_future = current_age + years_to_add

# Print the result
print(f"In {future_year}, you will be {age_in_future} years old.")
