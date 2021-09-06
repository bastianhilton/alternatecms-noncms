from channels.http import AsgiHandler
from channels.routing import URLRouter
from django.apps import apps
from django.conf import settings
from django.conf.urls import url
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
#from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
#from django.views.decorators.csrf import csrf_exempt
from django.views.i18n import JavaScriptCatalog
#from rest_framework import routers, serializers, viewsets
from two_factor.urls import urlpatterns as tf_urls
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

#from .schema import schema

admin.autodiscover()

schema = ...

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include(apps.get_app_config('oscar').urls[0])),
    url(r"^blog/", include("pinax.blog.urls", namespace="pinax_blog")),
    url(r"^ajax/images/", include("pinax.images.urls", namespace="pinax_images")),
    path("api/", include("oscarapi.urls")),
    url(r"^badges/", include("pinax.badges.urls", namespace="pinax_badges")),
    url(r"^announcements/", include("pinax.announcements.urls", namespace="pinax_announcements")),
    url(r"^messages/", include("pinax.messages.urls", namespace="pinax_messages")),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    path('api-auth/', include('rest_framework.urls')),
    path('payments/', include('payments.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('captcha/', include('captcha.urls')),
    path('search/', include('haystack.urls')),
    path('', include(tf_urls)),
    path('', include(tf_twilio_urls)),
]

application = URLRouter([
    re_path(r"", AsgiHandler),
])

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
admin.site.site_header = 'AlternateCMS' # Don't Remove
admin.site.site_title = 'AlternateCMS' # Don't Remove