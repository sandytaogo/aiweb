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
import speech_recognition as sr
import logging
# Create your views here.

#  from facenet_pytorch import fnmatch

logger = logging.getLogger(__name__)

def voiceToText(request) :
    audio_file = '/tmp/audio/.wav'
    msg = None
    try:
        r = sr.Recognizer()
        from_data = request.POST
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
        msg = r.recognize_sphinx(audio_data=audio, language="zh_CN")
    except Exception as e :
        msg = '我好像没听懂你说了什么'
        logger.error(e)
    finally:
        logger.info("finish...")
    return JsonResponse({"code": 200, "msg": msg})

