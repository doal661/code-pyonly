import tkinter as tk # 또는 from tkinter import *

window = tk.Tk() # Tk 객체 생성 (메인 윈도우)
window.title("나의 첫 GUI 창") # 창 제목 설정
window.geometry("400x300") # 창 크기 설정 (가로x세로)
window.mainloop() # 이벤트 루프 시작 (창이 닫힐 때까지 유지)
