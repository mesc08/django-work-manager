from .models import todolist
from rest_framework import viewsets, permissions
from .serializers import todolistSerializer


class todolistViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = todolistSerializer

    def get_queryset(self):
        return todolist.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
