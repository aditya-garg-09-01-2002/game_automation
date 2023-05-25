import time,pyautogui
from control_ops import calibrate_field,find_image

def harvest(cur_op,start,bottom_left,bottom_right,top_left,top_right,mid):
    time.sleep(1)
    # print("b")
    calibrate_field(cur_op,start)
    # print("a")
    time.sleep(1)
    pyautogui.moveTo(mid[0], mid[1], duration=1)
    pyautogui.click(pyautogui.position())
    sickle = find_image("sickle.png")
    pyautogui.moveTo(sickle[0], sickle[1], duration=1)
    pyautogui.mouseDown(button='left')
    for i in range(0, 15):
        pyautogui.moveTo(bottom_left[0] - i * ((bottom_left[0] - top_left[0]) / 14), bottom_left[1] + i * ((top_left[1] - bottom_left[1]) / 14), duration=1)
        pyautogui.moveTo(bottom_right[0] - i * (bottom_right[0] - top_right[0]) / 14, bottom_right[1] + i * (top_right[1] - bottom_right[1]) / 14, duration=1)
        if i == 14:
            pyautogui.moveTo(bottom_left[0], bottom_left[1], duration=1)
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(start,duration=2)

def sow(cur_op,start,bottom_left,bottom_right,top_left,top_right,mid):
    time.sleep(1)
    calibrate_field(cur_op,start)
    time.sleep(1)
    pyautogui.moveTo(mid[0], mid[1], duration=1)
    pyautogui.click(pyautogui.position())
    wheat = find_image("wheat.png")
    pyautogui.moveTo(wheat[0], wheat[1], duration=1)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(mid[0], mid[1], duration=1)
    for i in range(0, 15):
        pyautogui.moveTo(bottom_left[0] - i * (bottom_left[0] - top_left[0]) / 14, bottom_left[1] + i * (top_left[1] - bottom_left[1]) / 14, duration=1)
        pyautogui.moveTo(bottom_right[0] - i * (bottom_right[0] - top_right[0]) / 14, bottom_right[1] + i * (top_right[1] - bottom_right[1]) / 14, duration=1)
        if i == 14:
            pyautogui.moveTo(bottom_left[0], bottom_left[1], duration=1)
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(start[0], start[1] + 50, duration=1)
    pyautogui.click(pyautogui.position())
    time.sleep(60)

