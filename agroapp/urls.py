from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('crop/', views.crop_recommendation_view, name='crop_recommendation'),

    path('fertilizer/', views.fertilizer_recommendation_view, name='fertilizer_recommendation'),

    path(
    "disease-detection/",views.disease_detection,name="disease_detection"),
    path('chatbot/', views.chatbot_view, name='chatbot'),

    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register_view, name='register'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )