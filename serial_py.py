import serial
import keyboard
import threading
import time

KEY_MAP = {'q' : (0, 1), 'a' : (0, -1),
		   'w' : (1, 1), 's' : (1, -1),
		   'e' : (2, 1), 'd' : (2, -1),
		   'r' : (3, 1), 'f' : (3, -1),
		   't' : (4, 1), 'g' : (4, -1)}
angle = [90, 90, 90, 90, 90]
port, rate = 'COM3', 9600

def change_angle_by_key(angle, k):
	idx, value = KEY_MAP[k][0], KEY_MAP[k][1]
	angle[idx] += value
	if angle[idx] < 0:
		angle[idx] = 0
	elif angle[idx] > 180:
		angle[idx] = 180

def do_pressed_key(k):
	while keyboard.is_pressed(k):
		change_angle_by_key(angle, k)
		time.sleep(0.1)

def key_thread(k):
	thread = threading.Thread(target = do_pressed_key, args = (k, ))
	thread.start()

def send_angle(ser, angle):
	result = ','.join( map(str, angle) )
	result += '\n'
	ser.write(result.encode())

with serial.Serial(port, rate) as ser:
	for k in KEY_MAP:
		keyboard.add_hotkey(k, lambda x = k : key_thread(x))
	print(angle)
	send_angle(ser, angle)
	keyboard.wait('esc')

	









	
			
