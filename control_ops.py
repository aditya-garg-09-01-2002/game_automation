import pyautogui,cv2,numpy as np,time,tkinter
from tkinter import simpledialog
def ask_for_field_status():
    return "sow"
    root=tkinter.Tk()
    root.withdraw()
    return simpledialog.askstring("Input","If fields are already sown enter: sow\nelse enter: harvest")

def check_ad(last_time):
    if last_time==0:
        return time.time(),1
    else:
        if time.time()-last_time>=300:
            return time.time(),1
        else:
            return 0,0

def ask_for_wheat_count():
    return 500
    root=tkinter.Tk()
    root.withdraw()
    
    top_level = tkinter.Toplevel(root)
    top_level.title("Input")
    # top_level.attributes("-topmost", True) 
    top_level.grab_set()
    top_level.focus_force()

    return simpledialog.askinteger("Input","How much wheat you have")
    
def find_image(image_path):
    template = cv2.imread(image_path)
    # template = cv2.cvtColor(template, cv2.COLOR_RGB2BGR)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    screenshot = pyautogui.screenshot()
    # screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if(max_val<0.7):
        return None
    else:
        top_left = max_loc
        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
        center_x = (top_left[0] + bottom_right[0]) // 2
        center_y = (top_left[1] + bottom_right[1]) // 2

        return (center_x,center_y)

def find_image_lp(image_path):
    template = cv2.imread(image_path)

    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
    center_x = (top_left[0] + bottom_right[0]) // 2
    center_y = (top_left[1] + bottom_right[1]) // 2
    return (center_x,center_y)

def find_shop():
    shop=None
    while shop is None:
        shop=find_image_lp("shop_unsold.png")
        if shop is None:
            shop=find_image_lp("shop_sold.png")
    return shop

def calibrate_field(cur_op,start):
    field_location=None
    if cur_op=="sow":
        # print("c")
        field_location=find_image("full_fields.png")
    else:
        field_location=find_image("empty_fields.png")
    # print("d")
    pyautogui.moveTo(field_location,duration=2)
    pyautogui.mouseDown(button='left')
    # time.sleep(0.001)
    pyautogui.moveTo(start,duration=4)
    # time.sleep(0.5)
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(start[0],start[1]+50,duration=1)
    pyautogui.click(pyautogui.position())
    pyautogui.moveTo(start,duration=1)

# from pynput.keyboard import Listener as keyboardlistener,Key
# from pynput.mouse import Listener as mouselistener

# start_implementation=""

# def on_press(key):
#     global start_implementation
#     if key==Key.space:
#         start_implementation=" "
#         keyboardlistener.stop()

# def on_click(x,y,button,pressed):
#     global start
#     if pressed:
#         if start is None:
#             start=(x,y)
#             mouselistener.stop()

# with keyboardlistener(on_press=on_press) as keyboardlistener:
#     keyboardlistener.join()

# if start_implementation==" ":
#     with mouselistener(on_click=on_click) as mouselistener:
#         mouselistener.join()
#     time.sleep(3)
#     calibrate_field("sow")