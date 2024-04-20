from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage, name='home'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('service/',views.service, name='service'),
    path('properties/',views.properties, name='properties'),
    path('blog/',views.blog, name='blog'),
    path('add-properties/',views.addProperties, name='add-properties'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)