import pyautogui as pad
# Tìm tọa độ
pos = pad.position()
print(pos)

# Auto click
pad.click(pos)