import cv2


cap2 = cv2.VideoCapture(1)

while 1:
  ret2, img2 = cap2.read()

  if ret2:
      cv2.imshow('img2',img2)

      k = cv2.waitKey(1) 
      if k == 27: #press Esc to exit
         break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
