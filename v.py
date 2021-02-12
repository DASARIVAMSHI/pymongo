import datetime
import json

a_datetime = datetime.datetime.now()


formatted_datetime = a_datetime.isoformat()
json_datetime = json.dumps(formatted_datetime)


print(json_datetime)

from datetime import datetime, timedelta

current_datetime = datetime.now()

# future dates
one_year_future_date = current_datetime + timedelta(days=365)

print('Current Date:', current_datetime)
print('One year from now Date:', one_year_future_date)

# past dates
three_days_before_date = current_datetime - timedelta(days=3)
print('Three days before Date:', three_days_before_date)