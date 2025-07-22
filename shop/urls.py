# from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path("",views.index,name="ShopHome"),
path("about/",views.about,name="aboutus"),
path("contact/",views.contact_view,name="contact"),
path("home/",views.home,name="home"),
path("tracker/",views.tracker,name="tracker"),
path("search/",views.search,name="search"),
path("productview/<int:myid>",views.prodView,name="productview"),
path("checkout/",views.checkout,name="checkout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)