# Using obsidian as checkbox
import sys

input_month = 0
input_end_of_date = 0

if sys.argv[1] == str and sys.argv[2] == str:
    input_month = int(sys.argv[1])
    input_end_of_date = int(sys.argv[2])

def print_to_dates_on_one_month(month, date_of_end):
    date_counter = 1
    while date_counter <= date_of_end:
        print("- [ ] "+str(month)+"월 "+str(date_counter)+"일 : ")
        date_counter = date_counter + 1

# print_to_dates_on_one_month(3,31)
print_to_dates_on_one_month(input_month, input_end_of_date)
# print(sys.argv[1])