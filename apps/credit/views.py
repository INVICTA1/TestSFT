from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from credit.models import Manufacturer, ProductInCreditApplication


class ManufacturerAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        contract_id = self.kwargs.get('contract_id')
        manufacturers = Manufacturer.objects.filter(
            products__id__in=ProductInCreditApplication.objects.filter(
                credit_application__contract__id=contract_id
            )).distinct().values('id')

        return Response({'manufacturers': manufacturers}, status=status.HTTP_200_OK)
