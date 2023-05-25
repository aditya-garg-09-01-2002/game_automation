import pyautogui,time
from control_ops import find_image,find_shop
from box_ops import empty_box_ops,sold_box_ops,full_box_ops

def open_shop():
    pyautogui.moveTo(find_shop(),duration=2)
    pyautogui.click(pyautogui.position())

def check_empty_box():
    return find_image("empty_box.png")

def check_full_box():
    return find_image("full_box.png")

def check_sold_box():
    return find_image("sold_box.png")

def check_box():
    return (check_empty_box(),check_sold_box())    

def end_of_slot():
    check=None
    check=find_image("end_of_shop.png")
    if check is None:
        return False
    else:
        return True

def next_slot():
    if end_of_slot()==False:
        pyautogui.moveTo(1484, 461)
        pyautogui.dragTo(896, 469,duration=2)

def close_shop():
    pyautogui.moveTo(((1695, 114)),duration=1)
    pyautogui.click(pyautogui.position())

def put_ad():
        open_shop()
        full_box=None
        full_box=check_full_box()
        if full_box is not None:
            pyautogui.moveTo(full_box,duration=1)
            full_box_ops()
        close_shop()

def sell(wheat_count):
    
    h=empty_box=sold_box=None
    open_shop()
    check=True
    h=wheat_count
    while check==True:
        (empty_box,sold_box)=check_box()
        check=False
        if empty_box is not None:
            check=True
            pyautogui.moveTo(empty_box,duration=1)
            h-=empty_box_ops(h)
        if sold_box is not None:
            check=True
            pyautogui.moveTo(sold_box,duration=1)
            h-=sold_box_ops(h)
        empty_box=sold_box=None
        if check == False :
            if end_of_slot():
                close_shop()
            else:
                next_slot()
                check=True
    return wheat_count-h


# time.sleep(25)
# sell(400)