from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('find/', views.ResultListView.as_view(), name='result_list_view'),
    # path('', views.get_name, name='index/get-name/'),
]