from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Healtearth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('API.urls')),
    url(r'^$', views.form),
]
