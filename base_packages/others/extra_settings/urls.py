from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()


#Must be defined before auto discover and urlpatterns var. So when there is root url
#injection, we first insert root url to this, then the last line will insert it to real urlpatterns
default_app_url_patterns = []

from djangoautoconf import auto_conf_urls
auto_conf_urls.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += default_app_url_patterns