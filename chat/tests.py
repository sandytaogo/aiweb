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
from django.test import TestCase

# Create your tests here.
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import tensorflow as tf

# 加载预训练的模型和分词器
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')



def generate_response(input_text):
    tf.config.list_physical_devices('GPU')
    # 对输入文本进行编码
    input_ids = tokenizer.encode(input_text, return_tensors='tf')

    # 设置模型为随机预测模式
    past = None
    # 设置输出的最大长度
    max_length = 1000
    # 设置温度，越高越接近随机猜测，一般情况下需要调整
    temperature = 0.7

    # 生成文本
    # max_length 指定生成文本的最大长度
    # num_return_sequences 指定生成的文本序列数量
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    # 使用模型生成输出
    #output = model.generate(input_ids, max_length=max_length, past=past, temperature=temperature)

    # 解码生成的输出
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response

# 示例聊天
while True:
    user_input = input("用户输入: ")
    if user_input.strip() != '':
        response = generate_response(user_input)
        print("聊天机器人回复: ", response)