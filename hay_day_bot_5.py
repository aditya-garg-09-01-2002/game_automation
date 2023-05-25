# import field_ops,shop_ops
import time
from pynput.keyboard import Listener as keyboardlistener,Key
from pynput.mouse import Listener as mouselistener
from control_ops import ask_for_wheat_count,ask_for_field_status,check_ad
from field_ops import sow,harvest
from shop_ops import sell,put_ad
start_implementation=""
start=bottom_left=bottom_right=top_left=top_right=mid=cur_op=None
last_time=None
last_time=0
def on_press(key):
    global start_implementation
    if key==Key.space:
        start_implementation=" "
        keyboardlistener.stop()

def on_click(x,y,button,pressed):
    global start,bottom_left,bottom_right,top_left,top_right,mid
    if pressed:
        if start is None:
            start=(x,y)
        elif mid is None:
            mid=(x,y)
        elif bottom_left is None:
            bottom_left=(x,y)
        elif bottom_right is None:
            bottom_right=(x,y)
        elif top_right is None:
            top_right=(x,y)
        else:
            top_left=(x,y)
            mouselistener.stop()

# time.sleep(20) #just gives me time to open the game in the meanwhile

with keyboardlistener(on_press=on_press) as keyboardlistener:
    keyboardlistener.join()

if start_implementation==" ":
    wheat_count=ask_for_wheat_count()
    cur_op=ask_for_field_status() 
    with mouselistener(on_click=on_click) as mouselistener:
        mouselistener.join()

    while True:
        if cur_op=="sow":
            if 900-wheat_count>=240:
                harvest(cur_op,start,bottom_left,bottom_right,top_left,top_right,mid)
                sow(cur_op,start,bottom_left,bottom_right,top_left,top_right,mid)
                wheat_count-=sell(wheat_count)
                sell(wheat_count)
                temp=check_ad(last_time)
                if temp[1]==1:
                    last_time=temp[0]
                    put_ad()
            else:
                wheat_count-=sell(wheat_count)
        # else:
            sow(cur_op,start,bottom_left,bottom_right,top_left,top_right,mid)
            wheat_count-=sell(wheat_count)
            cur_op="sow"

        



