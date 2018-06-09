#!/usr/bin/python
import pigpio, curses, time, random

scr=curses.initscr()
scr.nodelay(1)

pi=pigpio.pi()

ai1 = 17
ai2 = 27
bi1 = 10
bi2 = 9

pi.write(5, 1)

def goForward():
	setPins(1, 0, 1, 0)
	print('w')
	
def goBackwards():
	setPins(0, 1, 0, 1)
	print('s')

def goLeft():
	setPins(1, 0, 0, 1)
	print('a')
	
def goRight():
	setPins(0, 1, 1, 0)
	print('d')
	
def stopMoving():
	pi.set_PWM_dutycycle(2,0)
	pi.set_PWM_dutycycle(3,0)
	print('stop')
	
def setPins(ai1State, ai2State, bi1State, bi2State):
	pi.set_PWM_dutycycle(2,255)
	pi.set_PWM_dutycycle(3,255)
	pi.write(ai1, ai1State)
	pi.write(ai2, ai2State)
	pi.write(bi1, bi1State)
	pi.write(bi2, bi2State)
	
def getDriveMode():
	keyPressed = scr.getch()
	
	print('Autonomous(y/n)')
	if(keyPressed == ord('y') or keyPressed == ord('n')):
	      if(keyPressed == ord('y')):
	          return true
	      else:
	          return false
	elif(keyPressed != 0):
	      print('Invalid Input')
	      getDriveMode()
	      
def initDrive():
	autonomous = getDriveMode()
	
	if(autonomous):
		autonomousDrive()
	else:
	      userDrive()
	      
def autonomousDrive(mode):
	if (mode == 'scripted'):
		movements = ['forward', 'backwards', 'left', 'right']

		for x in movements:
			currentMovement = movements[x]

			if (currentMovement == 'forward'):
				goForward()
			elif (currentMovement == 'backward'):
				goBackwards()
			elif (currentMovement == 'left'):
				goLeft()
			elif (currentMovement == 'right'):
				goRight()

			time.sleep(1)
			stopMoving()
	elif (mode == 'dance')
		
def userDrive():
	while True:
		keyPressed = scr.getch()

		if (keyPressed == ord('w')):
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

initDrive()
curses.endwin()
