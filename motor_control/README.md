Motor Driver: [L298](https://www.amazon.com/EC-Buying-L298-Controller-Optocoupler/dp/B0C73DC9CZ)  
Motor: [JGY-370](https://www.aliexpress.us/item/2251832653362809.html?gatewayAdapt=glo2usa4itemAdapt)  
**Motor pinout**:  
Red, white: Motor power, 12V.    
Blue: +3.3-5V code power.  
Black: code power, negative.  
Yellow, green: feedback.

**Set-up:**  
Power the board with a 12V supply. Connect the motor to one of the output terminals using the white and red wires. Supply 5V and ground from the Raspberry Pi or Arduino and connect this ground to the power supply ground. Finally, connect inputs 1&2 or 3&4 (depending on which output terminal is being used) to desired GPIO pins (code assumes GPIO 23 and 24).  

**Using the encoder:** 
Supply 3.3V from the Raspberry Pi / Arduino using the blue and black wires. Connect the yellow and green wires to desired GPIO pins (code assumes GPIO 17 and 22). 
