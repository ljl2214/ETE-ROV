import requests#导入requests库，用于发送HTTP请求与API进行交互

def normalize_output(text):#将AI的输出文本进行规范化处理，提取出left、right或center
    text = text.lower()
    if "left" in text:
        return "left"
    elif "right" in text:
        return "right"
    else:
        return "center"

def vla_decision(image_path):
    url = "http://localhost:11434/api/generate"

    prompt = "请判断图像中缆的位置，只能回答 left 或 center 或 right"

    with open(image_path, "rb") as f:#以二进制模式打开图片文件
        import base64
        image_base64 = base64.b64encode(f.read()).decode("utf-8")#将图片转换为Base64字符串，以便通过API传输

   
    response = requests.post(url, json={
        "model": "llava",
        "prompt": prompt,
        "images": [image_base64],
        "stream": False   
    })

    result = response.json()["response"]
    return normalize_output(result)

# 20260401 20：44 测试虚拟的Action
def control_robot(action):
    if action == "left":
        print("向右转 (yaw += 5°)")
    elif action == "right":
        print("向左转 (yaw -= 5°)")
    elif action == "center":
        print("保持直行 (yaw = 0°)")
    else:
        print("未知指令")


# 测试

#print("AI输出:", vla_decision("left.jpg"))#输出识别出的结果

result = vla_decision("left.jpg")
print("AI输出:", result)

control_robot(result)