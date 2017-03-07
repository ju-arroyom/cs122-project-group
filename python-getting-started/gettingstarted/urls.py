from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import newsapp.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
#app_name = 'newsapp'

urlpatterns = [
    url(r'^basic_piazza/', include('basic_piazza.urls')),
    url(r'^admin/', admin.site.urls),
]