# Using obsidian as checkbox
import sys

input_month = int(sys.argv[1])
input_end_of_date = int(sys.argv[2])


# 매개변수로 돌아가는 프로그램을 매개변수 없이 돌리면 아예 sys.argv[1] 자체를 인식하지 못해서 
# if (sys.argv[1] == None):
#        ~~~~~~~~^^^
#IndexError: list index out of range
# 과 같은 에러가 뜨고 말음.


# print(type(sys.argv[1])) check 완료

# 무조건 string으로 입력되기 때문에 if문으로 string 체크하는 의미가 없음.
#if sys.argv[1] == None or sys.argv[2] == None:
#    input_month = 0
#    input_end_of_date = 0
#else:
#    input_month = int(sys.argv[1])
#    input_end_of_date = int(sys.argv[2])

# -------------------------------

# if (sys.argv[1] == None):
#     sys.argv.append(0)

# try : input_month = int(sys.argv[1]) (IndexError)
# finally: 
    # sys.argv[1] = 0 // list assignment index out of range
#     sys.argv.append(0)
# try : input_end_of_date = int(sys.argv[2]) (IndexError)
# finally:
#     sys.argv[2] = 0

def print_to_dates_on_one_month(month, date_of_end):
    date_counter = 1
    while date_counter <= date_of_end:
        print("- [ ] "+str(month)+"월 "+str(date_counter)+"일 : ")
        date_counter = date_counter + 1

# print_to_dates_on_one_month(3,31)
print_to_dates_on_one_month(input_month, input_end_of_date)


# 불필요하니까 일단 주석처리
# print(sys.argv[1])
# print(sys.argv[2])