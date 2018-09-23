from django.conf.urls import url, include

urlpatterns = [
    url(r'^stock/', include('stockProject.stockApp.urls'))
]
