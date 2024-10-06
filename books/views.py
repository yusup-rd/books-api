from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer, BookUpdateSerializer
from .permissions import IsAuthorOrReadOnly
from .pagination import BooksPagination
from django_filters import rest_framework as filters


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
    pagination_class = BooksPagination


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def update(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = BookUpdateSerializer(
            book, data=request.data, partial=True, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)
