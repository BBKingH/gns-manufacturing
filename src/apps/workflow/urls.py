from django.urls import path, include
from django.views.generic import TemplateView

from .views import OrderListView, OrderUpdateView, OrderDetailView, switch_job

app_name = 'workflow'

    
urlpatterns = [
    path('', TemplateView.as_view(template_name='main/home.html'), name='home'),
    
    path('orders/', OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/update', OrderUpdateView.as_view(), name='order-update'),
    
    path('orders/switch_job/<int:order_id>/<int:stage_id>', switch_job, name='switch-job'),
]