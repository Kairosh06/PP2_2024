from datetime import datetime

# Define the two dates
date1 = datetime(2022, 1, 1, 0, 0, 0)  
date2 = datetime(2023, 1, 1, 0, 0, 0)
difference = date2 - date1
difference_in_seconds = difference.total_seconds()
print( difference_in_seconds)