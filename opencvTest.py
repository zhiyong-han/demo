import os
import numpy as np

# 尝试导入 cv2，不可用时回退到 Pillow
try:
    import cv2
    _cv2_ok = True
except Exception:
    _cv2_ok = False
    from PIL import Image

def create_red_image(path='red_24x24.png'):
    if _cv2_ok:
        # 创建 24x24 的 BGR 图像，红色在 OpenCV 中为 (0,0,255)
        img = np.zeros((24, 24, 3), dtype=np.uint8)
        img[:] = (0, 0, 255)
        cv2.imwrite(path, img)
    else:
        # Pillow 使用 RGB 顺序
        img = Image.new('RGB', (24, 24), (255, 0, 0))
        img.save(path)
    return os.path.abspath(path)

if __name__ == '__main__':
    out = create_red_image()
    print(out)