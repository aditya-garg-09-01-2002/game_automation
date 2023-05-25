import pyautogui

#shop is static i.e. most coordinates dont change by its own , I will take advantage of the fact and 
#fill in coordinates of repeated tasks which can simplify the task and make program faster and efficient
#without need of find_image function many times, i.e. reducing stack space as well


def check_wheat(h):
    if h>=134:
        return True
    else:
        return False
    
def pc():
    pyautogui.click(pyautogui.position())

def pm(l,t):
    pyautogui.moveTo(l,duration=t)

def empty_box_ops(h):
    #instead of finding picture of wheat , we can introduce variable to store and 
    #suitably sell wheat only if it will be at the top icon else wait for the next time
    if check_wheat(h):
        pc()
        pm((564,295),1)
        pc()
        pm((1513,528),1)
        pc()
        pm((1384,991),1)
        pc()
        pm((1167,57),1)
        pc()
        return 10

def sold_box_ops(h):
    if check_wheat(h):
        pc()
        return empty_box_ops(h)

def full_box_ops():
    pc()
    pm((1184,491),1)
    pc()
    pm((977,751),1)
    pc()
    pm((1468,132),1)
    pc()

        
    
