#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    // 打印 OpenCV 版本
    std::cout << "OpenCV 版本: " << CV_VERSION << std::endl;
    
    // 创建一个空白矩阵（OpenCV 核心数据结构）
    cv::Mat img = cv::Mat::zeros(300, 300, CV_8UC3);
    if (!img.empty()) {
        std::cout << "OpenCV 矩阵创建成功！配置完成 ✅" << std::endl;
    }
    return 0;
}