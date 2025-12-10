# List of month names
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# Get the number of years from the user
years = int(input("Enter the number of years: "))

# Start variables
total_rainfall = 0
total_months = 0

# Outer loop iterates once for each year
for year in range(1, years + 1):
    print(f"\nYear {year}:")
    
    # Inner loop iterates once for each month
    for month in range(12):
        rainfall = float(input(f"Enter the rainfall for {months[month]}: "))
        #Calculate the total rainfall
        total_rainfall += rainfall
        total_months += 1

# Calculate the average
average_rainfall = total_rainfall / total_months

# Show the results
print("\n")
print(f"Number of months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
