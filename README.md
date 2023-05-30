Herein, I developed an Online Game Automation Scipt or Bot in python
- I wrote 5 different modules having 27 functions distributed all over,
	- **hay_day_bot_5** :- program starts here and initial inputs are requested
	- **control_ops**   :- fundamental functions of the script
	- **shop_ops**      :- functions controlling the shop 
	- **field_ops**     :- functions controlling the fields
	- **box_ops**       :- functions controlling actions on the boxes of shop

- I used **OpenCV for image detection** so the bot can dynamically find locations to create mouse output events
- (I want to deploy AI model to improve image detection though)

- **How this works?**
	- We need to provide 6 static input positions for mouse.
	 - **start** - required for calibrating fields
	 - **mid** - field belonging to roughly center
	 - **corner inputs** - area of working for the code
	 - the flow of the functions can be understood with the vide demonstrations:
	   - game automation in action - https://youtu.be/gQdrBmnemHY
	   - game automation with function flow - https://youtu.be/M3zJnKzrqs0


      
    
