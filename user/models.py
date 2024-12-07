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
from importlib.metadata import requires

from django.db import models

# Create your models here.


from django.db import models

#
# 用户信息表
# authors sandy
# version 1.0.0 2024-12-04 13:13:13
class Account (models.Model):
    gid = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=52)
    password = models.CharField(max_length=52)
    is_lock = models.SmallIntegerField(blank=False, default=0)
    created_id = models.BigIntegerField(blank=False, default=1)
    created_time = models.DateTimeField(blank=False, auto_now=True)
    updated_id = models.BigIntegerField(blank=True, default=1)
    updated_time = models.DateTimeField(blank=True, auto_now=True)


class Security (models.Model):
    gid = models.BigIntegerField(primary_key=True)
    public_key = models.CharField(max_length=255)
    private_key = models.CharField(max_length=255)
    created_id = models.BigIntegerField(blank=False, default=1)
    created_time = models.DateTimeField(blank=False, auto_now=True)
    updated_id = models.BigIntegerField(blank=True, default=1)
    updated_time = models.DateTimeField(blank=True, auto_now=True)