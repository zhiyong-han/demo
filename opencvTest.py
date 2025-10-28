# ...existing code...
import numpy as np
import cv2
import os

def create_red_image(path='red_24x24.png'):
    # 创建 24x24 的 BGR 图像，红色在 OpenCV 中为 (0,0,255)
    img = np.zeros((24, 24, 3), dtype=np.uint8)
    img[:] = (0, 0, 255)
    cv2.imwrite(path, img)
    return os.path.abspath(path)

if __name__ == '__main__':
    out = create_red_image()
    print(out)
