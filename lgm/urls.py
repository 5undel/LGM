from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('base.urls')),
    path('membership/', include('membership.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('crossfit/', include('crossfit.urls')),
    path('pt/', include('pt.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'lgm.views.handler404'
handler500 = 'lgm.views.handler500'