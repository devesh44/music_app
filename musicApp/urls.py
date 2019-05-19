from django.urls import path
from . import views
app_name = 'music'
urlpatterns = [
	path('',views.album_list,name='album_list'),
	path('album/<int:pk>/', views.album_detail, name='album_detail'),
	path('album/add' , views.AlbumCreate.as_view(), name='album-add'),
]
