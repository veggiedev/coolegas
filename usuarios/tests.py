# from django.test import TestCase
import datetime
# Create your tests here.


today = datetime.date.today()

year = today.year
old_enough = year - 18
date = 1901
dates_list = [1900, 1901]
for i in range (250):
	if dates_list[-1] < old_enough:
		date += 1
		dates_list.append(date)
print(dates_list)

