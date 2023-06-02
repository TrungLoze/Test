import pyautogui as pad
import time
# Tìm tọa độ
#time.sleep(1)
#pos = pad.position()

# Auto click
# pad.click(pos)
# n=pad.confirm('Tiep tục hay dừng lai')
# if n == 'OK':
#     pad.write('Hello Ken Mom')
#     pad.press('enter')

# # Tìm theo đối tượng
hong=''
vang=''
while True:
    n=pad.confirm('Tiep tục hay dừng lai')
    if n == 'OK':
        for i in range(10000000):
            loc_hong=pad.locateOnScreen(hong)
            loc_vang=pad.locateOnScreen(vang)
            if loc_hong > loc_vang:
                pad.press('right')
            elif loc_hong < loc_vang:
                pad.press('left')
    else:
        break






