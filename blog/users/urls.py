#进行users子应用的视图路由

from django.urls import path
from users.views import RegisterView
from users.views import ImageCodeView
from users.views import SmsCodeView
from users.views import LoginView
from users.views import LogoutView
from users.views import ForgetPasswordView
from users.views import UserCenterView
from users.views import WriteBlogView

urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('register/',RegisterView.as_view(), name='register'),

    # 图片验证码的路由
    path('imagecode/', ImageCodeView.as_view(), name='imagecode'),

    # 短信验证码的路由
    path('smscode/', SmsCodeView.as_view(), name='smscode'),

    # 登录的路由
    path('login/', LoginView.as_view(), name='login'),

    # 退出的路由
    path('logout/', LogoutView.as_view(), name='logout'),

    # 忘记密码的路由
    path('forgetpassword/', ForgetPasswordView.as_view(), name='forgetpassword'),

    # 用户中心的路由
    path('center/', UserCenterView.as_view(), name='center'),

    # 写博客的路由
    path('writeblog/', WriteBlogView.as_view(), name='writeblog'),
]