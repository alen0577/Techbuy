from django.urls import path
from avodha_app import views
app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/<int:shop_id>', views.detail, name='detail'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')

]
