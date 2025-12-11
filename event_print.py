# Using obsidian as checkbox in TERMINAL
import sys

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
        input_month = int(sys.argv[1]) # 대입이 안 이뤄지는데, 아마 스코프가 로컬이라 그런 거 같음.
        input_end_of_date = int(sys.argv[2])
        input_start_of_week = sys.argv[3] # 달력의 영어가 3글자인 걸 이용해서 터미널 입력을 3글자 문자열로만 받음
        return True
    return False



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



if __name__ == "__main__":
    can_run_it = argv_length_check()
    if can_run_it == True:
        print_to_dates_on_one_month(int(sys.argv[1]), int(sys.argv[2])) # 함수에서 대입하지 말고 직접 대입해야 해결되는듯 ㅇㅇ
    else:
        print("매개변수 다 넣으라니까?")
    # print("y") __main__ 확인용