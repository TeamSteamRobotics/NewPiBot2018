import pigpio
import time
pi=pigpio.pi()
pi.set_mode(4,pigpio.INPUT)
counter=0
prevVal=False
while True:
	val=(pi.read(4)==1)
	if val != prevVal:
		counter += 1
	prevVal=val
	print(counter)
#	print(pi.read(4))
