import datetime


today = datetime.date.today()

year = today.year
old_enough = year - 18
print(old_enough)
date = 1901
dates_list = [1900, 1901]
for i in range (300):
	if dates_list[-1] < old_enough:
		date += 1
		dates_list.append(date)
print(dates_list)