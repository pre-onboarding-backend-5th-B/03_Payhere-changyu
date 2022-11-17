# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.generics import get_object_or_404
# from .models import AccountBook
# from .serializers import AccountBookSerializer


# class AccountBookViewSet(viewsets.ModelViewSet):
#     serializer_class = AccountBookSerializer
#     queryset = AccountBook.objects.all()

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user.pk)

#     def perform_create(self, serializer):
#         account_book = get_object_or_404(AccountBook, user=self.request.user.pk)
#         serializer.save(account_book=account_book)
#         return super().perform_create(serializer)

#     def perform_destroy(self, instance):
#         instance.is_delete = True
#         instance.save()
#         return super().perform_destroy(instance)

from rest_framework.generics import ListAPIView

from .serializers import AccountBookSerializer

from .models import AccountBook


class AccountBookListAPIView(ListAPIView):
    queryset = AccountBook.objects.all()
    serializer_class = AccountBookSerializer

    def get(self, request):
        return self.queryset.filter(user=request.user.pk)
