from django.conf import settings as s
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

if s.DEBUG:
    urlpatterns += static(
        s.MEDIA_URL, document_root=s.MEDIA_ROOT
    )
