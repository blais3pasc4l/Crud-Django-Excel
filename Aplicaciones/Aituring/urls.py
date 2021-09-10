from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarModelo/', views.registrarModelo),
    path('edicionModelo/<codigo>', views.edicionModelo),
    path('editarModelo/', views.editarModelo),
    path('eliminarModelo/<codigo>', views.eliminarModelo)
]