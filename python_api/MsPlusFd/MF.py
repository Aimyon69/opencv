import cv2 as cv
import function
try:
    index=function.find_camera()
except function.Not_Found:
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
    detectInterval=2*int(fps)
    interest_hsv_list=list()
    track=None
    #接着写检测的逻辑：
    while(cap.isOpened()):
        #先做初始工作，读取此帧图像：
        ret,frame=cap.read()
        if ret==True:
            #读取正常，开始操作
            if detectInterval==2*int(fps):
                #使用人脸检测更新兴趣区域和track数组
                frame_gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
                track=face_cas.detectMultiScale(frame_gray,scaleFactor=1.05,minNeighbors=8,minSize=(55,55))#track已更新
                interest_hsv_list.clear()#更新前先清除缓存
                #更新前需要判断是否检测到人脸
                if len(track)==0:
                    #没检测到人脸，等待下一帧图像再进行检测
                    detectInterval=2*int(fps)-1
                else:
                    #人脸出现，更新兴趣列表
                    for face in track:
                        x,y,w,h=face
                        interest_hsv_list.append(cv.cvtColor(frame[y:y+h,x:x+w],cv.COLOR_BGR2HSV))#兴趣区域更新完毕
                        function.drawRec(frame,x,y,w,h)#这一帧图像由检测技术给出检测框
                    print('detect track\n')
            else:
                #其余时间由meanshift追踪人脸，减小性能消耗
                #由于算法实现，兴趣数组和track数组的长度是一样的(第一维),而且是一一对应的,且一定能保证非空
                #遍历两个数组经行meanshift：
                loss_flag=False
                for i in range(len(track)):
                    ret_ms,track[i]=function.MS(interest_hsv_list[i],frame,track[i])
                    if ret_ms==False:
                        #目标丢失
                        loss_flag=True
                    else:
                        function.drawRec(frame,track[i][0],track[i][1],track[i][2],track[i][3])#追踪成功就更新框
                print('MS track\n')
                if loss_flag==True:
                    #丢失目标，下一帧进行人脸检测
                    detectInterval=2*int(fps)-1
                    print('track fail')
                #如果未触发，追踪成功
            #读取失败:等待下一帧图像或者退出
        detectInterval=(detectInterval+1)%(2*int(fps)+1)#更新计数器
        cv.imshow('frame',frame)
        out.write(frame)
        if cv.waitKey(int(1000/fps))&0xff==ord('1'):
            break
    cap.release()
    cv.destroyAllWindows()

                
            


                


