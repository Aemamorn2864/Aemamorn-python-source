print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

#input
seconds = int(input("Enter seconde: "))

#process
hours = seconds // 3600
seconds_remain = seconds % 3600

minutes = seconds_remain // 60
second_remain = seconds_remain % 60

#output
print(seconds, "seconds = ", hours, "hour,", minutes , "miunte,", seconds_remain, "second")
print(f"{seconds} seconds = {hours} hour, {minutes} miunte, {seconds_remain} second")