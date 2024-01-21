from django.urls import path

from . import views


urlpatterns = [
    path('test/', views.PostListView.as_view(), name="Api-postlist")

]
