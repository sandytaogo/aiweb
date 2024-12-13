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
from django.http import JsonResponse
from django.shortcuts import render
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, BertTokenizer, AutoTokenizer, AutoModelForMaskedLM

# Create your views here.

def gpt2(request) :
    # 加载预训练的模型和分词器
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    input_text = request.POST.get("msg")
    # 对输入文本进行编码
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
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
    # output = model.generate(input_ids, max_length=max_length, past=past, temperature=temperature)
    # 解码生成的输出
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return JsonResponse({'code':200, 'msg':response})


def pgtchinese(request) :
    tokenizer = BertTokenizer.from_pretrained("../model/gpt2_L-12_H-768_A-12_CN")
    # add the EOS token as PAD token to avoid warnings
    model = GPT2LMHeadModel.from_pretrained("../model/gpt2_L-12_H-768_A-12_CN", pad_token_id=0)
    # encode context the generation is conditioned on 远上寒山石径斜
    input_ids = tokenizer.encode('你好', return_tensors='pt')
    # generate text until the output length (which includes the context length) reaches 50
    greedy_output = model.generate(input_ids, max_length=50)
    print("Output:\n" + 100 * '-')
    print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))

def bertbasechinese(request):
    tokenizer = AutoTokenizer.from_pretrained("../model/bert-base-chinese")
    model = AutoModelForMaskedLM.from_pretrained("../model/bert-base-chinese")
    #tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")
    # add the EOS token as PAD token to avoid warnings
    #model = GPT2LMHeadModel.from_pretrained("bert-base-chinese", pad_token_id=0)
    # encode context the generation is conditioned on 远上寒山石径斜
    input_ids = tokenizer.encode('今天天气怎么样', return_tensors='pt')
    # generate text until the output length (which includes the context length) reaches 50
    greedy_output = model.generate(input_ids, max_length=50)
    print("Output:\n" + 100 * '-')
    print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))


if __name__ == "__main__" :
    #pgtchinese(None)
    bertbasechinese(None)