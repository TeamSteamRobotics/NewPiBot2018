#!/usr/bin/python
import pigpio
import curses
import time
scr=curses.initscr()
scr.nodelay(1)
pi=pigpio.pi()
ai1 = 17
ai2 = 27
bi1 = 10
bi2 = 9
pi.write(5, 1)
while True:
	key=scr.getch()
	if (key == ord('w')):
		pi.set_PWM_dutycycle(2,255)
                pi.set_PWM_dutycycle(3,255)
		pi.write(ai1, 1)
                pi.write(ai2, 0)
                pi.write(bi1, 1)
                pi.write(bi2, 0)
		print('w')
	elif (key == ord('s')):	
		pi.set_PWM_dutycycle(2,255)
                pi.set_PWM_dutycycle(3,255)
                pi.write(ai1, 0)
                pi.write(ai2, 1)
                pi.write(bi1, 0)
                pi.write(bi2, 1)
		print('s')
	elif (key == ord('a')):
                pi.set_PWM_dutycycle(2,255)
                pi.set_PWM_dutycycle(3,255)
                pi.write(ai1, 1)
                pi.write(ai2, 0)
                pi.write(bi1, 0)
                pi.write(bi2, 1)
                print('a')
        elif (key == ord('d')):
                pi.set_PWM_dutycycle(2,255)
                pi.set_PWM_dutycycle(3,255)
                pi.write(ai1, 0)
                pi.write(ai2, 1)
                pi.write(bi1, 1)
                pi.write(bi2, 0)
                print('d')
        elif (key == ord('q')):
                break
        else:
		pi.set_PWM_dutycycle(2,0)
                pi.set_PWM_dutycycle(3,0)
		print('stop')
	curses.flushinp()
	time.sleep(.04)

curses.endwin()
