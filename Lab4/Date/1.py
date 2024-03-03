from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days = 5)
print(current_date.strftime("%Y-%m-%d"))
print(new_date.strftime("%Y-%m-%d"))