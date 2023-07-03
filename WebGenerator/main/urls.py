from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('generator', views.generator, name='generator'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('prising', views.prising, name='prising'),
    path('success', views.success, name='success'),
    path('FAQs', views.FAQs, name='FAQs'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contacts', views.contacts, name='contacts'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
