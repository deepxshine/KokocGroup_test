from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/', include('rates.urls')),
]


handler404 = 'core.views.tr_handler404'
handler500 = 'core.views.tr_handler500'
