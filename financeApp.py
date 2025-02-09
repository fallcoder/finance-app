def get_float_input(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if value < 0:
                print("Error: value cannot be negative")
            else:
                return value
        except ValueError:
            print("Error: please enter a valid numeric value")
            
savings = get_float_input("enter your initial saving amount: ")
interest_rate = get_float_input("enter the annual interest rate (in %): ") / 100
years = int(get_float_input("enter the number of year: "))

print("\nyearly growth report")
print(f"{'year':<10}{'balance':<15}")

balance = savings
for year in range(1, years + 1):
    balance *= (1 + interest_rate)
    print(f"{year: <10}{balance: <15.2f}")
    
print(f"\nFinal amount after {years} years: {round(balance, 2)}")