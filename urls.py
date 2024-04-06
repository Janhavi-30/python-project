from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('export/', views.export_to_excel, name='export_to_excel'),
]
