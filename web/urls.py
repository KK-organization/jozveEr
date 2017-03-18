from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.signinpage),
    url(r'^home/(?P<token>.+)/', views.homepage, name='homepage'),
    url(r'^signupattempt/', views.signup_attempt),
    url(r'^signinattempt/', views.signin_attempt),
    url(r'^signin/',views.signinpage),
    url(r'^signup/',views.signuppage),
    url(r'^uploadafile/',views.upload),
    url(r'^signout/(?P<token>.+)/', views.signout)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)