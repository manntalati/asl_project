import cv2 as cv

cap = cv.VideoCapture(0)
i = 1
while i <= 5000:
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    if (i % 50 == 0):
        cv.imwrite(f'C:/Users/Mann/demos/asl/train/Z_train/Z_{int(i / 50)}.png', frame)
    if cv.waitKey(1) == ord('a'):
        break

    i+=1

cap.release()
cv.destroyAllWindows()
