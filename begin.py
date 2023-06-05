print(4559)
print(1.45)
print(10-9)
print(10*9)
print(10/9)
print(10+9)
print(10+9*10-9)

# --- Savings Calculator ---
newspace = "   "
nlines = "-------------------------------------------------------------------------"
print(newspace)
print(nlines)
print(newspace)
biob = " This is a savings calculator created with already predefined values, I used this script to test "
bioc = "type conversion and it's effectiveness, as the code will not run without errors if the str functions on line 21, 27, 34, is absent"

print(biob)
print(bioc) 
print(newspace)
print(nlines)
print(newspace)

name = "Bob"
hourly_wage = 20
hours_per_week = 40
weeks_per_year = 48

income_per_week = hourly_wage * hours_per_week
income_per_year = weeks_per_year * income_per_week

yearly_income = name + "'s yearly income is: " + str(income_per_year)
print(yearly_income)
print(newspace)

spend_per_week = 400
spend_per_year = spend_per_week * 52

yearly_spend = name + "'s yearly spend is: " + str(spend_per_year)
print(yearly_spend)
print(newspace)
# --- Calulate Yearly Savings ---

savings_per_year = income_per_year - spend_per_year

# --- Never Trust the Stitches that itches the bitches ---

yearly_savings = name + "'s yearly savings is: " + str(savings_per_year)
print(yearly_savings)
print(newspace)




