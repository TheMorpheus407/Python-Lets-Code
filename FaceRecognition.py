import cv2
capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("files/haarcascade_frontalface_default.xml")
while True:
    _, im = capture.read()
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(im_gray)  # [(0,0,500,500), (650, 700, 500,500)]
    for x, y, width, height in faces:
        cv2.rectangle(im, (x, y), (x + width, y + height), color=(0, 0, 255), thickness=5)
    cv2.imshow("Kamera", im)
    if cv2.waitKey(1) == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()