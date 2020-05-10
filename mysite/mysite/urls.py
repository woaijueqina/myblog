from django.conf.urls import include, url
from django.contrib import admin
from blog.views import *



urlpatterns = [
    url(r'',include('blog.urls', namespace='blog')),
    url(r'^admin/', admin.site.urls),
    # url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^blog/', blog.views.post_detail),
]


#import debug_toolbar
#urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
