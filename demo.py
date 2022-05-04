import requests
import base64


# 证件照合成请求地址
url = 'https://ai-xiaotong.com/fangpc/removebg'
# 向files里传入图片
files = {'file': open("test.jpg","rb")}

# 发送post请求
r = requests.post(url,files=files)
# 返回图像Base64结果
# print(r.json()["result"])

# 返回图像Base64转换为图片本地保存
with open("result.png", "wb") as fh:
    fh.write(base64.decodebytes(r.json()["result"].encode()))