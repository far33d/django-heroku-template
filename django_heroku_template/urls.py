from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_heroku_template.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from django_jinja import views as jv

handler400 = jv.BadRequest.as_view()
handler403 = jv.PermissionDenied.as_view()
handler404 = jv.PageNotFound.as_view()
handler500 = jv.ServerError.as_view()
