# from django.urls import path, include
# from rest_framework import routers
# from account_book.views import AccountBookViewSet

# router = routers.DefaultRouter()
# router.register("", AccountBookViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]

from django.urls import path
from account_book import views

urlpatterns = [
    path("", views.AccountBookListAPIView.as_view(), name="list_view"),
]
