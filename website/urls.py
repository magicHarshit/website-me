from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()

from django.views.generic import TemplateView
from website.views import ContactView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="temp_1.html"), name='home'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^resume/$', TemplateView.as_view(template_name="qualification.html"), name='resume'),
    #url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()