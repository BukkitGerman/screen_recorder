#!/usr/bin/python

import sys, numpy, keyboard, cv2, pyautogui

if len(sys.argv) == 3:
	filename = sys.argv[1]+ '.mp4'
	codec = cv2.VideoWriter_fourcc(*'mp4v')
	vid = cv2.VideoWriter(filename+"", codec, 30.0, (int(sys.argv[2].split("x")[0]), int(sys.argv[2].split("x")[1])))

	print('Aufnahme gestartet...')
	while True:
		img = pyautogui.screenshot()
		numpy_frame = numpy.array(img)
		frame = cv2.cvtColor(numpy_frame, cv2.COLOR_BGR2RGB)
		vid.write(frame)
		if keyboard.is_pressed('x'):
			print('Aufnahme gestoppt...')
			break
	cv2.destroyAllWindows()
	vid.release()
else:
	print("Usage: python recorder.py <filename> <resolution (e.g 1920x1080)>")
