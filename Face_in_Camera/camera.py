import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

# Загружаем каскады для глаз.
eyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FPS, 24) # Частота кадров

while(True):
    ret, img = cap.read()
    img = cv2.flip(img, 1)  # Поворот камеры
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2, # араметр, указывающий, на сколько уменьшается размер изображения при каждом масштабе изображения. Он используется для создания масштабной пирамиды
        minNeighbors= 10,   #Параметр, указывающий, сколько соседей должен иметь каждый прямоугольник-кандидат для его сохранения. (чем выше , тем больше точность)
        minSize=(20, 20)  # Минимально возможный размер объекта. Объекты меньшего размера игнорируются.
    )
    color = (0,255,0)
    thickness = 2
    for (x,y,w,h) in faces:
        #print(x,y,w,h)
        cv2.rectangle(img,(x,y),(x+w,y+h),color , thickness)
        roi_gray = gray[y:y+h, x:x+w]  # Вырезаем область с лицами
        roi_color = img[y:y+h, x:x+w]

        eyes = eyeCascade.detectMultiScale(
        roi_gray,              #
        scaleFactor=1.2,       # Ищем глаза в области с лицом
        minNeighbors=4,
        minSize=(5, 5),
        )
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)  


    cv2.imshow('img', img)
    #cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()