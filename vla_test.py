import numpy as np
import cv2
from llava.model import LlavaLlamaForCausalLM, LlavaConfig

# 初始化模型
config = LlavaConfig()
model = LlavaLlamaForCausalLM(config)  # CPU模式即可

# 读取图像
img_path = "../images/test1.jpg"
img = cv2.imread(img_path)

# 模拟推理输出动作向量
# 因为你的显卡太小，本机先用模拟值
action_vector = np.array([0.0, 0.0, 5.0])  # yaw +5°

# 保存为 CSV，MATLAB/Simscape 读取
np.savetxt("../vla_output.csv", action_vector, delimiter=',')
print("动作向量已保存:", action_vector)