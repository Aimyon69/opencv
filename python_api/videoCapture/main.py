import define
import cv2 as cv
try:
    index=define.find_camera()
except define.Not_Found :
    print('Not found')
    exit(1)
else:
    cap=cv.VideoCapture(index)
    fps=cap.get(cv.CAP_PROP_FPS)
    print(f'img_fps={fps}')
    frame_wid=int(cap.get(3))
    frame_hei=int(cap.get(4))
    print(f'img_wid={frame_wid},img_hei={frame_hei}')
    out=cv.VideoWriter('D:\Code\Opencv\\videoCapture\\cap.avi',cv.VideoWriter_fourcc('M','J','P','G'),25,(frame_wid,frame_hei))
    while(cap.isOpened()):
        ret,frame=cap.read()
        if ret==True :
            cv.imshow('Video',frame)
            out.write(frame)
        if cv.waitKey(int(1000/fps))&0xff==ord('q'):
            break
    cap.release()
    out.release()
    cap.destroyAllwindows()



