from django.conf.urls import url
from django.urls import path, include
from api import views

urlpatterns = [
    path('create/', views.audio_create, name='create'),
    path('list/<audioFileType>/', views.audio_list, name='list'),
    path('delete/<audioFileType>/<audioFileID>', views.audio_delete, name='delete'),
    path('update/<audioFileType>/<audioFileID>', views.audio_update, name='update'),
    url(r'^.*$', views.page_404, name="page_404")
]
