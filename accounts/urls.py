# from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('signup/', views.signup, name='signup'),
path("signin", views.signin, name="signin")



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)