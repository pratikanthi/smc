from django.conf.urls import patterns, include, url
from django.contrib import admin
from restaurant import views
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),

    url(r'^$',views.base),
    url(r'^restaurants/$',views.index),
    url(r'^restaurants/(?P<slug>[\w\-]+)/?$',views.fetch_restaurant),
    url(r'^comments/', include('django_comments.urls')),

)



admin.site.site_header = settings.ADMIN_SITE_HEADER
