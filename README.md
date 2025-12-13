# too much very important notice
python practice folder on linux mint debian version in T480 thinkpad.

In this folder, only using python.

---

만약 event_print에 '요일까지 같이 프린트되게 하라면' 어떻게 설계가 변할까?

- 일단 시작 요일을 학실하게 하고
- 7번 주기로 반복되게 하면서
- 그 요일이 언제 끝날지를 명시해야 하지 않을까?

일단 요일까지 가능은 했는데, 터미널 매개변수 체크에서 뭐 하려고 하면 계속 index 에러가 뜸. \

---

4년간 파이썬 제대로 안하다가 폐쇄망에서 7시간만에 작성함.

폐쇄망 환경은 초안 만들 때 끝냄. (657a589) -> 그리고 성공함.

2025년 12월 10일에 작업한 모든 게 폐쇄망.

그러나 추가 프로그래밍은 상황 따라서 왔다갔다 할 거임.


----

sudo apt install tcl tk

Traceback (most recent call last):
  File "/home/wfewj/code-pyonly/tktest.py", line 1, in <module>
    import tkinter as tk # 또는 from tkinter import *
    ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.14/tkinter/__init__.py", line 38, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
    ^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named '_tkinter'
