from django.urls import path

from .views import homeView,aboutUsView


urlpatterns = [
  path('', homeView.as_view(), name='home'),
  path('about-us', aboutUsView.as_view(), name='about_us')
]