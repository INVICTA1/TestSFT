from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from credit.models import CreditApplication


class ManufacturerAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        contract_id = self.kwargs.get('contract_id')
        manufacturers = set()
        credit_applications = CreditApplication.objects.prefetch_related('products__manufacturer').filter(
            contracts__id=contract_id
        ).distinct()
        for credit_application in credit_applications:
            manufacturer = credit_application.products.values_list('manufacturer__id').distinct()
            manufacturers.update(manufacturer)
        return Response({'manufacturers': manufacturers}, status=status.HTTP_200_OK)
