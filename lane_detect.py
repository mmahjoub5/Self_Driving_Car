import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()

	

	cv2.imshow('frame', hsv)
	lower_blue = np.array([60,40,40])
	upper_blue = np.array([150, 255, 255])
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()


	
