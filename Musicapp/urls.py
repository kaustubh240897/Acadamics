from django.conf.urls import include,url
from django.contrib import admin
from .views import home_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page , name='home'),
    url(r'^music/', include('music.urls')),

]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

