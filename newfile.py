import cv2

cap = cv2.VideoCapture(0)

def edit(frame):
	cv2.rectangle(frame, (10,10), (30,30), (255,0,0), 2)
	frame = cv2.resize(frame, None, fx=0.9, fy=0.9)
	return frame

while True:
	print("Remote changes is here")
	ret, frame = cap.read()
	print(f"Here we edit on the same file")
	print(f"Lets check it again")

	if not ret:
		break

	cv2.imshow("frame", frame)
	if cv2.waitKey(1) == ord("q"):
		break


	print("Changes has been brought here!")

cap.release()
cv2.destroyAllWindows()
