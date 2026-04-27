import cv2 as cv
class Not_Found(Exception) :
    pass
def find_camera():
    index=None 
    for i in range(11):
        cap=cv.VideoCapture(i)
        if cap.isOpened() and cap.read()[0]:
            index=i
            print("successfully find")
            cap.release()
            break
        cap.release()
    if index==None :
        raise Not_Found()
    return index
    