from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trades import views
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    path('user/register', views.UserView.as_view()),
    path('trading/list', views.TradeListView.as_view()),
    path('trading/buy', views.TradeBuyView.as_view()),
    path('trading/sell', views.TradeSellView.as_view()),
    path('trading/total', views.TradeTotalView.as_view()),
]

urlpatterns += [
    url(r'^api-token-auth/', authtoken_views.obtain_auth_token)
]
