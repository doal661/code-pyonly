# Using obsidian as checkbox in TERMINAL
import sys

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

## 터미널로 쓸거면
# if sys.argv[1] == None: # 입력이 진짜로 없으면 인터프리터는 이 부분에서 에러를 냄.

# 전역변수 초기화
input_month = -9
input_end_of_date = -55

def argv_length_check():
    if len(sys.argv) != 4: # 존나 잘먹힌다. 앞으로는 타입체크 이전에 길이체크부터 해야 out of range 오류가 안 날듯.
        input_month = 0
        input_end_of_date = -55
        # print("here!") 이걸 통해서 len() 잘못쓴거 파악함.
        return False
    else: # 이것도 무사히 넘어갔음.
        input_month = int(sys.argv[1])
        input_end_of_date = int(sys.argv[2])
        input_start_of_week = sys.argv[3] # 달력의 영어가 3글자인 걸 이용해서 터미널 입력을 3글자 문자열로만 받음
        return True
    return False


iterate_seven_days = ["sunday", "monday", "tuesday", "wendsday", "thursday", "friday", "saturday"] # 이건 7개라 하드코딩해도 문제없음.

# 카운트를 위해 사용될 숫자와의 매칭을 위하여 2차원 배열을 쓴다면?
iterate_seven_days_list = [
    ["sun", "sunday", 0],
    ["mon", "monday", 1],
    ["tue", "tuesday", 2],
    ["wen", "wendsday", 3],
    ["thu", "thursday", 4],
    ["fri", "friday", 5],
    ["sat", "saturday", 6]
]

# 아니면 2개만 매칭되는걸 이용해서 2차원배열 말고 딕셔너리로 퉁친다면?
# 라고 세번째 매개변수 고려하기 전까진 생각했었다.
dict_of_interate_seven_days = {
    0: "sun",
    1: "mon",
    2: "tue",
    3: "wed",
    4: "thu",
    5: "fri",
    6: "sat",
    # 숫자로 관리하면서 '인쇄될때만' 필요한 문자열을 관리하자는 의도. 얐으나
    # 터미널 입력을 3자리 문자열로 받기로 했으니...
}

def print_to_dates_on_one_month(month, date_of_end):
    date_counter = 1
    if sys.argv[3] == "sun":
        week_counter = 0
    elif sys.argv[3] == "mon":
        week_counter = 1
    elif sys.argv[3] == "tue":
        week_counter = 2
    elif sys.argv[3] == "wen":
        week_counter = 3
    elif sys.argv[3] == "thu":
        week_counter = 4
    elif sys.argv[3] == "fri":
        week_counter = 5
    elif sys.argv[3] == "sat":
        week_counter = 6
    else: # 요일을 받는 매개변수가 지정된 문자가 아닌 경우를 짚어주면서 스무스하게 에러 처리.
        week_counter = 0
        print("그런거 없다 이새기야 제대로 입력해라")
        return
    while date_counter <= date_of_end:
        print("- [ ] "+str(month)+"월 "+str(date_counter)+"일 (" + str(dict_of_interate_seven_days[int(week_counter)%7]) + ") : ")
        print("") # 터미널로 쓸 경우에만 활성화
        # vscodium의 OUTPUT으로 사용할 때에는 하지 않아도 엔터키 반영이 되기 때문
        date_counter = date_counter + 1
        week_counter = week_counter + 1

# print_to_dates_on_one_month(3,31)



# 불필요하니까 일단 주석처리
# print(sys.argv[1])
# print(sys.argv[2])

if __name__ == "__main__":
    can_run_it = argv_length_check()
    if can_run_it == True:
        print_to_dates_on_one_month(input_month, input_end_of_date)
    else:
        print("매개변수 다 넣으라니까?")
    # print("y") __main__ 확인용