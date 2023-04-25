import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
	
	if not ret:
		break

	cv2.imshow("frame", frame)
	if cv2.waitKey(1) == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()
