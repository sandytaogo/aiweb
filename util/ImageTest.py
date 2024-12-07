#  Copyright 2024-2034 the original author or authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from PIL import Image, ImageDraw, ImageFont

# 创建图片
img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
# 在图片查看器中打开
# img.show()

# 保存在本地
with open('code.png', 'wb') as f:
    img.save(f, format='png')
# 创建画笔，用于在图片上画任意内容

img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
# 画点
img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
# 第一个参数：表示坐标
# 第二个参数：表示颜色
draw.point([100, 100], fill="red")
draw.point([300, 300], fill=(255, 255, 255))
#画线
img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
# 第一个参数：表示起始坐标和结束坐标
# 第二个参数：表示颜色
draw.line((100, 100, 100, 300), fill='red')
draw.line((100, 100, 300, 100), fill=(255, 255, 255))
# 画圆

img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
# 第一个参数：表示起始坐标和结束坐标（圆要画在其中间）
# 第二个参数：表示开始角度
# 第三个参数：表示结束角度
# 第四个参数：表示颜色
draw.arc((100, 100, 300, 300), 0, 90, fill="red")
# 写文本

img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
# 第一个参数：表示起始坐标
# 第二个参数：表示写入内容
# 第三个参数：表示颜色
draw.text([0, 0], 'python', "red")
#特殊字体文字

img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
draw = ImageDraw.Draw(img, mode='RGB')
# 第一个参数：表示字体文件路径
# 第二个参数：表示字体大小
font = ImageFont.truetype("kumo.ttf", 28)
# 第一个参数：表示起始坐标
# 第二个参数：表示写入内容
# 第三个参数：表示颜色
# 第四个参数：表示颜色
draw.text([0, 0], 'python', "red", font=font)












