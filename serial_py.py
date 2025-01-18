import serial
import keyboard

KEY = ['q', 'a', 'w', 's', 'e', 'd', 'r', 'f', 't', 'g']
angle = [90, 90, 90, 90, 90]
serial = serial.Serial( port='COM3', baudrate=9600 )

def send_angle(arr):
	result = ''
	for i in angle:
		if i < 0:
			i = 0
		elif i > 180:
			i = 180
		result += str(i)
	serial.write(result.encode())

send_angle(angle)
while True:
	for i, k in enumerate(KEY):
		if is_pressed(k):
			angle[i//2] += 1 if i % 2 == 0 else -1
	send_angle(angle)
	if is_pressed('esc'):
		break	
	
serial.close()
	
			