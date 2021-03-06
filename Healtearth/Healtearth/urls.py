from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Healtearth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('API.urls')),
    url(r'^$', views.index),
    url(r'^form/$', views.form),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)