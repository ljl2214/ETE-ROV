# from PIL import Image

# def simple_vla_decision(image_path):
#     # 模拟AI输出（第一步先不用真实模型）
    
#     # 你先手动写规则（后面再换AI）
#     if "left" in image_path:
#         return "left"
#     elif "right" in image_path:
#         return "right"
#     else:
#         return "center"

# # 测试
# result = simple_vla_decision("right.jpg")
# print("AI输出:", result)

import cv2
import numpy as np

def detect_cable_position(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("图片读取失败")
        return "center"

    # 转灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 简单二值化（假设缆是亮/暗）
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    h, w = thresh.shape

    # 分三块
    left = thresh[:, :w//3]
    center = thresh[:, w//3:2*w//3]
    right = thresh[:, 2*w//3:]

    # 统计“缆”的像素数量
    left_sum = np.sum(left)
    center_sum = np.sum(center)
    right_sum = np.sum(right)

    # 判断位置
    if left_sum > center_sum and left_sum > right_sum:
        return "left"
    elif right_sum > center_sum and right_sum > left_sum:
        return "right"
    else:
        return "center"


# 测试
result = detect_cable_position("middle.jpg")
print("AI输出:", result)