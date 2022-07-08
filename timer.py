# COUNTDOWN TIMER
# Created by Toyirov!
# 30.06.2022 -- 8:55

import time
import pyautogui

def countdown(t):
	while t:
		mins, secs = divmod(t,60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	print("Vaqt tugadi...")
	pyautogui.alert("Vaqt tugadi...                  \n\n\n")

vaqt = int(input("Raqam kiriting: "))

countdown(int(vaqt))