from rest_framework.generics import (
                                        ListCreateAPIView,
                                        RetrieveUpdateDestroyAPIView,
                                    )
from perfumes_blog.models import Perfume
from .serializers import PerfumeSerializer
from .permissions import IsOwnerOrReadOnly
class PerfumesListView(ListCreateAPIView):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer
    def perform_create(self, serializer):
        serializer.save()

class PerfumesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer
    permission_classes = (IsOwnerOrReadOnly, )


