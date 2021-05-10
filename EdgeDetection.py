import cv2

cam = cv2.VideoCapture(0)

while True:
    _, image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 30, 100)

    cv2.imshow("LiveVideo", image)
    cv2.imshow("Edges", edges)
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()