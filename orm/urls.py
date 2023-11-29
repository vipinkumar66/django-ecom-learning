from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("inventory.urls", namespace="store"))
]
if settings.DEBUG == True:
    # This is only used for the development environment and not the production one
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
