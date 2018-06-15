#!/usr/bin/python
import pigpio, curses, time, random

scr=curses.initscr()
scr.nodelay(1)

pi=pigpio.pi()

ai1 = 17
ai2 = 27
bi1 = 10
bi2 = 9


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
	pi.set_PWM_dutycycle(5,0)
	pi.set_PWM_dutycycle(6,0)
	print('stop')
	
def setPins(ai1State, ai2State, bi1State, bi2State):
	pi.set_PWM_dutycycle(5,255)
	pi.set_PWM_dutycycle(6,255)
	pi.write(ai1, ai1State)
	pi.write(ai2, ai2State)
	pi.write(bi1, bi1State)
	pi.write(bi2, bi2State)
	
def getDriveMode():
	scr.nodelay(0)
	scr.addstr(0,0,'Autonomous(y/n)')
	keyPressed = scr.getch()
	
	if(keyPressed == ord('y') or keyPressed == ord('n')):
	      if(keyPressed == ord('y')):
	          return True
	      else:
	          return False
	elif(keyPressed != 0):
	      print('Invalid Input')
	      return getDriveMode()
	else:
		return getDriveMode()
	      
def initDrive():
	autonomous = getDriveMode()
	scr.nodelay(1)
	if(autonomous):
		autonomousDrive(1)
	
	userDrive()
	      
def autonomousDrive(mode):
	if (mode == 1):
		movements = ['forward', 'backwards', 'left', 'right']

		for x in movements:
			currentMovement = x

			if (currentMovement == 'forward'):
				goForward()
			elif (currentMovement == 'backwards'):
				goBackwards()
			elif (currentMovement == 'left'):
				goLeft()
			elif (currentMovement == 'right'):
				goRight()

			time.sleep(1)
			stopMoving()
	elif (mode == 'dance'):
		print("no.")

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
