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
import os

from django.conf import ENVIRONMENT_VARIABLE, Settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.functional import LazyObject

# 由于Django内部连接MySQL时使用的是MySQLdb模块，而python3中还无此模块，所以需要使用pymysql来代替

# 如下设置放置的与project同名的配置的 __init__.py文件中

# import pymysql

# pymysql.install_as_MySQLdb()


# 常量的声明
SUCCESS = 200
FIAL = 300

USER_SESSION_KEY = ""

# 尝试修改常量的值会导致错误
# MY_CONSTANT = "New Value"  # 这会抛出异常

# 如果你想要创建一个真正的常量（不能更改的变量），可以使用类似下面的方法
class _const:
    class ConstError(TypeError): pass

    def __setitem__(self, key, value):
        raise self.ConstError(f"Can't rebind const ({key})")
        # 这里可以加入更多的逻辑来阻止变量的修改

    def __setattr__(self, key, value):
        raise self.ConstError(f"Can't rebind const ({key})")

class LazySettings(LazyObject):
    """
    A lazy proxy for either global Django settings or a custom settings object.
    The user can manually configure settings prior to using them. Otherwise,
    Django uses the settings module pointed to by DJANGO_SETTINGS_MODULE.
    """

    def _setup(self, name=None):
        """
        Load the settings module pointed to by the environment variable. This
        is used the first time settings are needed, if the user hasn't
        configured settings manually.
        """
        settings_module = os.environ.get(ENVIRONMENT_VARIABLE)
        if not settings_module:
            desc = ("setting %s" % name) if name else "settings"
            raise ImproperlyConfigured(
                "Requested %s, but settings are not configured. "
                "You must either define the environment variable %s "
                "or call settings.configure() before accessing settings."
                % (desc, ENVIRONMENT_VARIABLE)
            )

        self._wrapped = Settings(settings_module)

settings = LazySettings()