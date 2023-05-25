Herein, I developed an Online Game Automation Scipt or Bot in python
  I have used some template images which I arranged as screenshots
  I wrote 5 different modules having 27 functions distributed all over,
    hay_day_bot_5 :- program starts here and defines the flow of different functions and event handling to initialise the program
    control_ops   :- some functions which are accessed by multiple modules and are crucial towards working of Bot at its fundamental level
    shop_ops      :- so there is a shop in Hay Day and functions like finding it, opening it , selling on it , closing it , moving it are here
    field_ops     :- a very basic task of the game is to plant and harvest the crop which are described here
    box_ops       :- box lies inside shops and have three attributes, i.e can be either empty, full or have sold status whose operations are here
  
  I used OpenCV for image detection so the bot can dynamically find locations to create mouse output events
  (I want to deploy AI model to improve image detection though)
  
  How this works?
    You need to provide 6 static input positions for mouse and 2 values for initialising of the code in control_ops, but as later on GUI wil be deployed user interface will be simplified and will ask with promopts.
      - where to bring the bottom left field to (start)
      - where to basically start harvest or sow functions (mid)
      - what are boundaries of the field , bottom_left, bottom_right, top_right, top_left corners
      - how much more of the quantity of wheat can be stored
      - current status of the field "sow" or "harvest"
      
    
