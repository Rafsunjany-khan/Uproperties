from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage, name='home'),
    path('contact/',views.contact, name='contact'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)