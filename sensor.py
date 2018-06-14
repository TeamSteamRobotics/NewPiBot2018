import ToFSensor.python.VL53L0X as tof

sensor = tof.VL53L0X()

sensor.start_ranging(tof.VL53L0X_BETTER_ACCURACY_MODE)

def get_distance():
	return sensor.get_distance()

