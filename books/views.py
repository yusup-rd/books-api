from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

class BookFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name="genre", lookup_expr="iexact")

    class Meta:
        model = Book
        fields = ['genre']

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
    pagination_class = PageNumberPagination

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def update(self, request, *args, **kwargs):
        partial_data = {
            "price": request.data.get("price", None),
            "description": request.data.get("description", None),
            "title": request.data.get("title", None),
        }
        return super().update(request, partial=partial_data, *args, **kwargs)
