from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trades import views


urlpatterns = [
    path('user/register', views.UserView.as_view()),
    path('stock/list', views.StockListView.as_view()),
    path('stock/create', views.StockCreateView.as_view()),
    path('stock/<int:pk>/', views.StockUpdateView.as_view()),
    path('trading/list', views.TradeListView.as_view()),
    path('trading/buy', views.TradeBuyView.as_view()),
    path('trading/sell', views.TradeSellView.as_view()),
    path('trading/total', views.TradeTotalView.as_view()),
]
