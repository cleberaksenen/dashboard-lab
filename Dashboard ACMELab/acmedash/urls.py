from django.contrib import admin
from django.urls import path
from app.views import Amostras, New_amostra, HomePageView, LaboratorioPageView, SC2BarChartView, Detail_amostra
from accounts.views import register_view, login_view, logout_view

    
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('laboratorio/', LaboratorioPageView.as_view(), name='laboratorio'),
    path('admin/', admin.site.urls),
    path('sc2dash/', Amostras.as_view(), name='amostras_list'),
    path('sc2cadastro/', New_amostra.as_view(), name='new_amostra'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sc2_dashboard/', SC2BarChartView.as_view(), name='sc2_dashboard'),
    path('SC2/<int:pk>/', Detail_amostra.as_view(), name='detalhes_amostra'),
]
