from django.contrib import admin
from django.urls import path
from api.views import ListCryptoCurrencyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListCryptoCurrencyView.as_view()),
]
