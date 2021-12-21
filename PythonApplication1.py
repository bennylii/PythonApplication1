
#导入cv模块
#(”cv2”中的”2”并不表示OpenCV的版本号。
#OpenCV是基于C/C++的，”cv”和”cv2”表示的是底层C API和C++API的区别。
#”cv2”表示使用的是C++API。这主要是一个历史遗留问题，是为了保持向后兼容性。)
import cv2
#读取图像
img = cv2.imread('E:/122211.jpg')
#创建窗口并显示图像
cv2.namedWindow('Image')
cv2.imshow('Image',img)
cv2.waitKey(0) #这里等待时间为0毫秒，意味着时任意键终止的
#释放窗口
cv2.destroyAllWindows()