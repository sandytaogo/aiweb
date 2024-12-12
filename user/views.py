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
from django.conf import settings
from django.shortcuts import render ,HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import logging
from util.codeimg import check_code

from util import sm2util

from io import BytesIO

from django import forms

from user.models import Security, Account

# 导入会话中间件使用的会话模块
from django.contrib.sessions.models import Session
logger = logging.getLogger(__name__)

# Create your views here.

class BandContactForm(forms.Form) :
    userName = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

def publickey(request):
    securitys = Security.objects.filter(gid=1)
    response = JsonResponse({"publickey":securitys[0].public_key, "privatekey" : securitys[0].private_key})
    return response

def regrist(request) :
    return render(request, 'addUser.html')

def addUser(request) :
    return render(request, 'addUser.html')

@require_http_methods(["GET"])
def verifyCodeImage(request) :
    img, code = check_code()
    stream = BytesIO()
    img.save(stream, 'png')
    request.session['login_verify_code'] = code
    request.session.set_expiry(300)
    response = HttpResponse(stream.getvalue())

    response['Content-Type']= "image/jpeg"
    response['Pragma'] = "No-cache"
    response['Cache-Control'] = "no-cache"
    return response

@csrf_exempt
@transaction.atomic
@require_http_methods(["POST"])
def login(request) :
    userName = request.POST.get("userName")
    if userName == None :
        return JsonResponse({"code": 300, "msg": "用户账号名称不能为空"})
    password = request.POST.get("password")
    if password == None :
        return JsonResponse({"code": 300, "msg": "用户账号密码不能为空"})

    validateCode = request.POST.get("validateCode")
    if validateCode == None :
        return JsonResponse({"code": 300, "msg": "验证码不能为空"})
    login_verify_code = request.session.get("login_verify_code")
    if login_verify_code == None:
        return JsonResponse({"code": 300, "msg": "验证码不能为空非法访问"})
    if validateCode.lower() != login_verify_code.lower() :
        return JsonResponse({"code": 300, "msg": "验证码不正确"})

    request.session.delete('login_verify_code')
    securitys = Security.objects.filter(gid=1)

    sm2 = sm2util.SM2Util(pub_key=securitys[0].public_key, pri_key=securitys[0].private_key)
    password = sm2.DecryptHex(password)

    userAccount = Account.objects.filter(user_name=userName)
    if len(userAccount) == 0:
        return JsonResponse({"code": 300, "msg": "账号或密码错误"})
    if userAccount[0].password != password:
        return JsonResponse({"code": 300, "msg": "账号或密码错误"})


    del request.session['login_verify_code']
    request.session['user'] = {'userName':userAccount[0].user_name, 'userId':userAccount[0].gid}
    request.session.set_expiry(7200)

    logger.info("login user[gid=%s, username=%s]", userAccount[0].gid, userAccount[0].user_name)

    return JsonResponse({"code": 200, "msg": "登录成功"})

def logout(request) :
    # 清除过期的 Session 数据
    request.session.clear_expired()
    # 删除某一个数据
    #del request.session['name']
    # 清空所有的数据
    request.session.flush()

    #response = HttpResponse('login.html')
    #response.delete_cookie(settings.SESSION_COOKIE_NAME)
    return redirect('/login')