from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^index', views.index, name='index'),
    
    # 成绩列表
    url(r'^scorelists/', views.scorelists, name='scorelists'),
    url(r'^delete_score_by_id/', views.delete_score_by_id, name='delete_score_by_id'),
	
] 
