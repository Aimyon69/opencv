import cv2
import numpy as np  
print("OpenCV版本：", cv2.__version__)
print("NumPy版本：", np.__version__) 
img = np.zeros((500, 500, 3), dtype=np.uint8)
cv2.rectangle(img, (100, 100), (400, 400), (0, 0, 255), 3)
cv2.putText(img, "OpenCV Test", (150, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("Test Window", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()  