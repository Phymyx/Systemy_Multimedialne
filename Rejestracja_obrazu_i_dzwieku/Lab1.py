import cv2
import pyaudio

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("kamerka.avi") #przechwytywanie z pliku

(grabbed, frame) = cap.read()
fshape = frame.shape
fheight = fshape[0]
fwidth = fshape[1]
#print(fwidth, fheight)

fourcc = cv2.VideoWriter_fourcc(*'x264')
out = cv2.VideoWriter('test2.avi', fourcc, 20.0, (fwidth, fheight))


if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?. Exiting...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame, 0)
    #cut = frame[0:720, 0:1280]
    out.write(frame)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

cap.get(cv2.CAP_PROP_FRAME_WIDTH)
cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

