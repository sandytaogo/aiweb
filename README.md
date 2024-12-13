
<div align="center">
<!-- Title: -->
  <a href="https://github.com/sandytaogo/aiweb">
    <!--<img src="" height="100"> -->
  </a>
  <h1><a href="https://github.com/sandytaogo/">Artificial intelligence (AI)</a> - Python</h1>
<!-- Labels: -->
  <!-- First row: -->
  <a href="https://gitpod.io/#https://github.com/sandytaogo/aiweb">
    <img src="https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod&style=flat-square" height="20" alt="Gitpod Ready-to-Code">
  </a>
  <a href="https://github.com/sandytaogo/Python/blob/master/CONTRIBUTING.md">
    <img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square" height="20" alt="Contributions Welcome">
  </a>
  <img src="https://img.shields.io/github/repo-size/sandytaogo/Python.svg?label=Repo%20size&style=flat-square" height="20">
  <a href="https://the-algorithms.com/discord">
    <img src="https://img.shields.io/discord/808045925556682782.svg?logo=discord&colorB=7289DA&style=flat-square" height="20" alt="Discord chat">
  </a>
  <a href="https://gitter.im/sandytaogo/community">
    <img src="https://img.shields.io/badge/Chat-Gitter-ff69b4.svg?label=Chat&logo=gitter&style=flat-square" height="20" alt="Gitter chat">
  </a>
  <!-- Second row: -->
  <br>
  <a href="https://github.com/sandytaogo/Python/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/sandytaogo/Python/build.yml?branch=master&label=CI&logo=github&style=flat-square" height="20" alt="GitHub Workflow Status">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" height="20" alt="pre-commit">
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/static/v1?label=code%20style&message=black&color=black&style=flat-square" height="20" alt="code style: black">
  </a>

[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![actions](https://github.com/alibaba/spring-cloud-alibaba/workflows/Integration%20Testing/badge.svg)](https://github.com/alibaba/spring-cloud-alibaba/actions)

<!-- Short description: -->
  <h3>All algorithms implemented in Python - for share</h3>
</div>

## Overview
artificial intelligence (AI), the ability of a digital computer or computer-controlled robot to perform tasks commonly associated with intelligent beings. The term is frequently applied to the project of developing systems endowed with the intellectual processes characteristic of humans, such as the ability to reason, discover meaning, generalize, or learn from past experience. Since their development in the 1940s, digital computers have been programmed to carry out very complex tasks—such as discovering proofs for mathematical theorems or playing chess—with great proficiency. Despite continuing advances in computer processing speed and memory capacity, there are as yet no programs that can match full human flexibility over wider domains or in tasks requiring much everyday knowledge. On the other hand, some programs have attained the performance levels of human experts and professionals in executing certain specific tasks, so that artificial intelligence in this limited sense is found in applications as diverse as medical diagnosis, computer search engines, voice or handwriting recognition, and chatbots.
****
<img src="ai_overview.jpg" width="100%">

### Pytorch 采用
Pytorch是torch的python版本，是由Facebook开源的神经网络框架，专门针对 GPU 加速的深度神经网络（DNN）编程。Torch 是一个经典的对多维矩阵数据进行操作的张量（tensor ）库，在机器学习和其他数学密集型应用有广泛应用。
Pytorch的计算图是动态的，可以根据计算需要实时改变计算图。
由于Torch语言采用 Lua，导致在国内一直很小众，并逐渐被支持 Python 的 Tensorflow 抢走用户。作为经典机器学习库 Torch 的端口，PyTorch 为 Python 语言使用者提供了舒适的写代码选择。

### 智能语音识别
引入自然语言处理，语音识别模块<br>
https://github.com/Uberi/speech_recognition


### 环境依赖
 
https://pypi.org/

pip-compile --upgrade requirements.in

pip install ddddocr -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install facenet-pytorch

pip install torch torchvision torchaudio

pip install transformers

pip install -r requirements.in

pip install --upgrade pip

python.exe -m pip install --upgrade pip

### 其他常用命令：

   python manage.py createsuperuser

   python manage.py startapp appname

   python manage.py syncdb

   python manage.py makemigrations

   python manage.py migrate --fake

   python manage.py migrate --fake-initial

   python manage.py migrate --fake <appname>

   python manage.py clean cache

   python manage.py clear_cache --cache defualt # 清理特定缓存

   python manage.py clear_cache --all # 清空全部缓存

   python manage.py runserver 0.0.0.0

   python manage.py dbshell

### 优化辅助分析
https://docs.python.org/zh-cn/3.13/library/gc.html

https://docs.djangoproject.com/

https://shields.io/

https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Mandarin/

https://github.com/ShenDezhou/Chinese-PreTrained-GPT/tree/main

https://gitcode.com/mirrors/google-bert/bert-base-chinese/tree/main

