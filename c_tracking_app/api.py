from rest_framework import generics
from rest_framework.response import Response
from .models import Tracking
from .serializers import *


class TrackingListAPI(generics.RetrieveAPIView):
    serializer_class = TrackingSerializer

    def get(self, request, *args, **kwargs):
        queryset = Activity.objects.filter(is_active=True)
        queryset = Tracking.objects.filter(student__activity__)
        return Response({"seguimientos": SeguimientoSerializer(queryset, many=True).data})


class UpdateSeguimientoAPI(generics.GenericAPIView):
    serializer_class = UpdateSeguimientoSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        seguimiento = Seguimiento.objects.get(pk=kwargs["id"])
        serializer = self.get_serializer(instance=seguimiento, data=request.data)
        serializer.is_valid(raise_exception=True)
        seguimiento = serializer.save()
        return Response({
            "seguimiento":
            SeguimientoSerializer(seguimiento,
                              context=self.get_serializer_context()).data
        })