import cv2 as cv
import function
try:
    index=function.find_camera()
except function.Not_Found :
    print('Error:camera not found,check for link')
    exit(1)
else:
    cap=cv.VideoCapture(index)
    fps=cap.get(5)
    print(fps)
    frame_hei=int(cap.get(4))
    frame_wid=int(cap.get(3))
    face_cas = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cas = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
    out=cv.VideoWriter('D:\Code\Opencv\MsPlusFd\\cap.avi',cv.VideoWriter_fourcc('M','J','P','G'),25,(frame_wid,frame_hei))
    while(cap.isOpened()):
        ret,frame=cap.read()
        if ret==True:
            frame_gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            faceRects=face_cas.detectMultiScale(frame_gray,scaleFactor=1.05,minNeighbors=8,minSize=(55,55))
            for face in faceRects:
                x,y,w,h=face
                cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            cv.imshow('frame',frame)
            out.write(frame)
        if cv.waitKey(int(1000/fps))&0xff==ord('1'):
            break
    cap.release()
    cv.destroyAllWindows()
            




    
        
