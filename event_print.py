# Using obsidian as checkbox
import sys

input_month = 0
input_end_of_date = 0

# print(type(sys.argv[1])) check 완료

# 무조건 string으로 입력되기 때문에 if문으로 string 체크하는 의미가 없음.
if sys.argv[1] == None or sys.argv[2] == None:
    input_month = 0
    input_end_of_date = 0
else:
    input_month = int(sys.argv[1])
    input_end_of_date = int(sys.argv[2])

def print_to_dates_on_one_month(month, date_of_end):
    date_counter = 1
    while date_counter <= date_of_end:
        print("- [ ] "+str(month)+"월 "+str(date_counter)+"일 : ")
        date_counter = date_counter + 1

# print_to_dates_on_one_month(3,31)
print_to_dates_on_one_month(input_month, input_end_of_date)
print(sys.argv[1])
print(sys.argv[2])