from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('about/',views.about,name='about'),
    path('home/',views.home,name='home'),
    path('', views.main, name='main page'),
    path('category/<int:cid>/',views.category_images,name='category image'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
