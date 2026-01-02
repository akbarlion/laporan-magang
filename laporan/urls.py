from django.urls import path
from . import views

urlpatterns = [
    path('', views.LaporanListView.as_view(), name='laporan_list'),
    path('laporan/tambah/', views.LaporanCreateView.as_view(), name='laporan_create'),
    path('laporan/<int:pk>/', views.LaporanDetailView.as_view(), name='laporan_detail'),
    path('laporan/<int:pk>/edit/', views.LaporanUpdateView.as_view(), name='laporan_update'),
    path('laporan/<int:pk>/hapus/', views.LaporanDeleteView.as_view(), name='laporan_delete'),
]
