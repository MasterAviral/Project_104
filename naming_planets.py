import cv2

img=cv2.imread("PRO-104-Project/solar-system.jpg")


sun="Sun"
cv2.putText(img,
           sun,
           (40,60),
           cv2.FONT_HERSHEY_DUPLEX,
           2,
           (0,255,255))

mercury="Mercury"
cv2.putText(img,
            mercury,
           (110,190),
           cv2.FONT_HERSHEY_DUPLEX,
           0.5,
           (255,255,255))           

venus="Venus"
cv2.putText(img,
            venus,
           (180,178),
           cv2.FONT_HERSHEY_DUPLEX,
           0.6,
           (255,255,255))

earth="Earth"
cv2.putText(img,
            earth,
           (280,268),
           cv2.FONT_HERSHEY_DUPLEX,
           0.6,
           (255,255,255))    

moon="Moon"
cv2.putText(img,
            moon,
           (320,159),
           cv2.FONT_HERSHEY_DUPLEX,
           0.49,
           (173,212,255))                   

mars="Mars"
cv2.putText(img,
            mars,
           (380,180),
           cv2.FONT_HERSHEY_DUPLEX,
           0.65,
           (255,255,255))

jupiter="Jupiter"
cv2.putText(img,
            jupiter,
           (490,80),
           cv2.FONT_HERSHEY_DUPLEX,
           0.9,
           (255,255,255)) 

saturn="Saturn"
cv2.putText(img,
            saturn,
           (690,120),
           cv2.FONT_HERSHEY_DUPLEX,
           0.8,
           (255,255,255)) 
uranus="Uranus"
cv2.putText(img,
            uranus,
           (930,145),
           cv2.FONT_HERSHEY_DUPLEX,
           0.8,
           (255,255,255))  

neptune="Neptune"
cv2.putText(img,
            neptune,
           (1080,145),
           cv2.FONT_HERSHEY_DUPLEX,
           0.8,
           (255,255,255))


cv2.imshow("output",img)
cv2.waitKey(0)



