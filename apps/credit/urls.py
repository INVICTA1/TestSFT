from rest_framework.routers import SimpleRouter

from credit.views import ManufacturerAPIView
from django.urls import path

router = SimpleRouter(trailing_slash=False)

urlpatterns = [
    path('manufacturer/<int:contract_id>', ManufacturerAPIView.as_view()),

]
urlpatterns += router.urls
