from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . views import HomeView
from . import views

# write your urls here
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('order/<int:pk>/', views.order, name='order'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)