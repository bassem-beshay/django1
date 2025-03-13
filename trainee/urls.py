from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('sign_up/',views.sign , name='sign_up') ,
    path('profile/' , views.pro , name='profile'),
    path('login/', views.log , name = 'login')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)