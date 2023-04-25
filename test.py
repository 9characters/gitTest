import cv2

cap = cv2.VideoCapture(0)

def edit(frame):
	cv2.rectangle(frame, (10,10), (30,30), (255,0,0), 2)
	frame = cv2.resize(frame, None, fx=0.9, fy=0.9)
	return frame

while True:
	ret, frame = cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
	frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	
	cv2.rectangle(frame, (10,10), (30,30), (255,0,0), 2)

	frame = cv2.resize(frame, None, fx=0.9, fy=0.9)

	if not ret:
		break

	cv2.imshow("frame", frame)
	if cv2.waitKey(1) == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()
