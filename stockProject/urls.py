from django.conf.urls import url, include
from stockProject.stockApp import views

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^types/$', views.TypeList.as_view()),
]