import pyautogui as pad
import time
# Tìm tọa độ
time.sleep(1)
pos = pad.position()

# Auto click
for i in range(10):
    pad.click(pos)
    pad.write('Hello Ken Mom')
    pad.press('enter')