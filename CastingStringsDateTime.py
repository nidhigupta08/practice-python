import datetime
# Initial date and time strings
date_string = "2024-05-29"
time_string = "14:35:00"

# Convert string to date object
date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
print(f"The date object is: {date_object}")

# Convert string to time object
time_object = datetime.datetime.strptime(time_string, "%H:%M:%S").time()
print(f"The time object is: {time_object}")

# Combine date and time into a datetime object
datetime_object = datetime.datetime.combine(date_object, time_object)
print(f"The combined datetime object is: {datetime_object}")
