import cv2 as cv
class Not_Found(Exception):
    pass
def find_camera():
    index=None
    for i in range(11):
        cap=cv.VideoCapture(i)
        if cap.isOpened() and cap.read()[0]:
            index=i
            print('successfully found')
            cap.release()
            break
        cap.release()
    if index is None:
        raise Not_Found()
    return index
def MS(interest_hsv,frame,track):
    interest_hist=cv.calcHist([interest_hsv],[0],None,[180],[0,180])#提取兴趣hsv图像的h通道，h通道的值域为[0,180)
    cv.normalize(interest_hist,interest_hist,0,255,cv.NORM_MINMAX)#归一化，把各个区间的像素个数映射到0-255的范围,是必要的操作，保证追踪的精确度
    term_crit=(cv.TERM_CRITERIA_EPS|cv.TERM_CRITERIA_COUNT,10,1)#meanshift的终止条件
    frame_hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)#将本帧图像也转换为hsv图像
    dst=cv.calcBackProject([frame_hsv],[0],interest_hist,[0,180],1)#直方图的反向映射
    ret,track=cv.meanShift(dst,track,term_crit)#执行meanshift
    return ret,track
def drawRec(frame,x,y,w,h):
    cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    return