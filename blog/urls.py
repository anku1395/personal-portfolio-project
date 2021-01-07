from django.urls import path
from . import views
# app_name is not mandatory if not given then the code followed by app name is written
app_name = 'blog'
#<!--<a href="{% url 'detail' blog.id %}"><h2>{{blog.title}}</h2></a> this can also be done-->
urlpatterns = [
    path("", views.all_blogs,name='all_blogs'),
    path("<int:blog_id>/", views.detail,name='detail'),
]