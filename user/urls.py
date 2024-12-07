


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

from django.urls import path
from user import views as userViews

urlpatterns = [
     path('publickey', userViews.publickey),
     path('regrist', userViews.regrist),
     path('login', userViews.login),
     path('logout', userViews.logout),

     path('addUser', userViews.addUser),
     path('verifyCodeImage', userViews.verifyCodeImage)
]