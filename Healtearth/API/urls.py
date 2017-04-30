from django.conf.urls import include, url
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Healtearth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^search/$', views.search),
]
