from django.conf.urls import url, include
# from rest_framework import routers
from stockProject.stockApp import views

# router = routers.DefaultRouter()
# router.register(r'products', views.ProductViewSet)
# router.register(r'types', views.TypeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^types/$', views.TypeList.as_view()),
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]