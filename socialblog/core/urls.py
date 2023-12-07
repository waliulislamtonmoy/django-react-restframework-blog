
from django.contrib import admin
from django.urls import path,include


from django.conf import settings
from django.conf.urls.static import static
from core import views
from App_Url import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("api/",include("App_Url.urls")),
    
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
