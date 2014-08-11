from django.conf.urls import patterns, include, url
<<<<<<< HEAD
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from contact import views
from GDG import views
=======
from contact import views
>>>>>>> 0c1c288339fb2536a9d5dbd259d0a4f3cf8d8572
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
<<<<<<< HEAD
    url(r'^$', 'GDG.views.home'),
=======
    url(r'^$', 'contact.views.home'),
>>>>>>> 0c1c288339fb2536a9d5dbd259d0a4f3cf8d8572
    url(r'contactus^$', 'contact.views.contactus'),
    # url(r'^GDG/', include('GDG.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
<<<<<<< HEAD
urlpatterns += staticfiles_urlpatterns()	
=======
>>>>>>> 0c1c288339fb2536a9d5dbd259d0a4f3cf8d8572
