from django.urls import path
from home.views import IndexView
from home.views import DetailView

urlpatterns = [
    path('', IndexView.as_view(),name='index'),

    #定义详情页面的路由
    path('detail/', DetailView.as_view(),name='detail'),
]