from django.urls import path
from .import views
urlpatterns = [
path("",views.index,name="Blog"),
path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
# path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]