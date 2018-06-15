#  Shows the path to the python interpreter
#!/usr/bin/python

'''
Libraries are collections of prewritten code that in this case is used for:
Pigpio: Allowing the pi's GPIO pins to be used in python
Curses: A library for controling and using the terminal screen (aka console, cmd, shell, etc.)
Time: A library for controlling time and for controlling when code can execute
'''
import pigpio, curses, time

'''
curses.initscr() gets the current window and initializes the curses library. scr is set to a 
reference of the current screen
'''
scr = curses.initscr()

#Allows for the constant stream of keyboard/mouse inputs with no delay between different input.
scr.nodelay(1)

'''
pigpio.pi() returns a reference to the hardware on the pi. Used for the GPIO pins and serial communication.
This code is using pigpio for only the GPIO functionality.
'''
pi = pigpio.pi()

#The various GPIO pins that the hardware is connected to. Check the pinout to see what they are.
ai1 = 17
ai2 = 27
bi1 = 10
bi2 = 9

#Setting GPIO pin 5 to high. Meaning that that pin has power into it.

'''
All the goDIRECTION() methods call the setPins method with the pin's state as either 0 (low) or 1 (high).
The key corresponding with the direction is then printed to the screen.
'''
def goForward():
	setPins(1, 0, 1, 0)
	print('w')
	
def goBackwards():
	setPins(0, 0, 0, 0)
	print('s')

def goLeft():
	setPins(1, 0, 0, 1)
	print('a')
	
def goRight():
	setPins(0, 1, 1, 0)
	print('d')
  
'''
Sets the pwm dutycycles of the pins to an off state, so that both servo pins are not sending any pulses.
It then prints out 'stop' to the screen.
'''
def stopMoving():
	pi.set_PWM_dutycycle(5,32)
	pi.set_PWM_dutycycle(6,32)
	print('stop')

'''
Sets the pwm dutycycle (how long the pin is active) to the longest amount of time that it can be active, which is 255.
The pins are then set to their correct high (1) or low (0) state, depending on the method that called setPins().
'''
def setPins(ai1State, ai2State, bi1State, bi2State):
	pi.set_PWM_dutycycle(5,128)
	pi.set_PWM_dutycycle(6,96)
	pi.write(ai1, ai1State)
	pi.write(ai2, ai2State)
	pi.write(bi1, bi1State)
	pi.write(bi2, bi2State)

'''
The main loop for this whole program. The while loop runs until the user presses the 'q' key. If any of the 
'w', 'a', 's', or 'd' keys are pressed then the corresponsing goDIRECTION() method will be called. If no key is
pressed then the stopMoving() method will be called. Regardless of what key is pressed, or if a key is not pressed,
curses.flushinp() is called, which clears any unused keyboard input from curses, then the code is stopped for 
0.04 seconds.
'''
while True:
	keyPressed = scr.getch()
	if (keyPressed == ord('j')):
		goForward()
	elif (keyPressed == ord('s')):	
		goBackwards()
	elif (keyPressed == ord('a')):
		goLeft()
	elif (keyPressed == ord('d')):
		goRight()
	elif (keyPressed == ord('q')):
		break
	else:
		stopMoving()
		
	curses.flushinp()
	time.sleep(.04)

#Restores the terminal to its previous state before this program was launched.
curses.endwin()
