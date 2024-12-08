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
#
import base64
import sys
from io import BytesIO
import requests
import ddddocr
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By


def main() :

    print('Python %s on %s' % (sys.version, sys.platform))

    # 指定chromedriver的路径
    driver_path = '/path/to/chromedriver'
    #driver = webdriver.Chrome()  # 创建浏览器对象 谷歌浏览器
    # 使用chromedriver创建一个webdriver对象
    #driver = webdriver.Chrome(executable_path=driver_path)

    start = time.time()
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    #options.capabilities['browserName'] == 'chrome'
    #options.add_argument("--disable-application-cache")
    #options.add_argument("--disk-cache-size=0")
    #options.add_argument("--media-cache-size=0")

    driver = webdriver.Chrome(options = options)

    # 打开一个网页
    driver.get('http://127.0.0.1:8000/login/') #访问网址 百度

    end = time.time()
    print(end - start)

    time.sleep(1)

    driver.implicitly_wait(100)
    xpath = By.XPATH
    kwinput = driver.find_element(By.NAME,'userName')
    # 清除现有文本（如果需要）
    kwinput.clear()
    # 输入新文本
    kwinput.send_keys("admin")

    kwinput = driver.find_element(By.NAME, 'password')
    # 清除现有文本（如果需要）
    kwinput.clear()
    # 输入新文本
    kwinput.send_keys("admin")
    kwinput.click()
    time.sleep(5)

    # 定位到图片元素
    image_element = driver.find_element(By.CSS_SELECTOR, 'img.verify-code')
    # 获取图片的实际URL
    image_url = image_element.get_attribute('src')
    try :
        # 在浏览器中直接下载图片
        response = requests.get(image_url)
        img_context = response.content
        # 将图片转换为PIL图片对象
        image = Image.open(BytesIO(img_context))
        # 保存图片
        image.save('verify-code-image.png')

        file_obj = open('verify-code-image.png', mode='r', encoding=None)
        byte_img = file_obj.buffer
        # 初始化 OCR 实例
        ocr = ddddocr.DdddOcr()
        # 使用 OCR 处理图片
        img_base64 = base64.b64encode(byte_img).decode('utf-8')
        code = ocr.classification(img_base64)
        print(code)

        # 在页面上进行一些操作，例如点击一个按钮
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn-success')
        button.click()
        time.sleep(5)
        pass
    except Exception as e:
        # 处理异常
        print(f"An error occurred: {e}")
    finally:
        # 关闭浏览器
        driver.quit()

if __name__ == '__main__' :
    main()