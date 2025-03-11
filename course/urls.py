from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.home, name='login'),
    path('del/<int:id>/', views.dele, name='delete_course'),
    path('add/', views.add ,name="add_cource"),
    path('update/<int:id>/',views.update ,name="update_cource")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)