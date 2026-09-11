from django.contrib import admin
from django.urls import path, include
from agroapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('', include('agroapp.urls')),
]