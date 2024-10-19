from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('detect_deepfake/', views.detect_deepfake, name='detect_deepfake'),
    path('video-analyses/', views.VideoAnalysisList.as_view(), name='video-analysis-list'),
    path('video-analyses/<int:pk>/', views.VideoAnalysisDetail.as_view(), name='video-analysis-detail'),
]
