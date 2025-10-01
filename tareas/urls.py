from django.urls import path
from . import views
app_name = "tareas"
urlpatterns = [
 path('', views.TareaListView.as_view(), name="lista"),
 path('nuevo/', views.TareaCreateView.as_view(), name="crear"),
 path('<int:pk>/', views.TareaDetailView.as_view(), name='detalle'),
 path('<int:pk>/editar/', views.TareaUpdateView.as_view(),name="editar"),
 path('<int:pk>/eliminar/', views.TareaDeleteView.as_view(),name="eliminar"),
]