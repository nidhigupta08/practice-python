import datetime

# Get current date and time
current_time = datetime.datetime.now()

# Format and display the current time
formatted_time = current_time.strftime("%H:%M:%S")
print("Current time:", formatted_time)
