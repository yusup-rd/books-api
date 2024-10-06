from rest_framework import generics
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer, BookUpdateSerializer
from .permissions import IsAuthorOrReadOnly
from .pagination import BooksPagination
from django_filters import rest_framework as filters


class BookFilter(filters.FilterSet):
    """Filter class for filtering books based on genre."""
    genre = filters.CharFilter(field_name="genre", lookup_expr="iexact")

    class Meta:
        model = Book
        fields = ['genre']


class BookListCreateView(generics.ListCreateAPIView):
    """View for listing and creating books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
    pagination_class = BooksPagination


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, or deleting a specific book."""
    queryset = Book.objects.all()
    permission_classes = [IsAuthorOrReadOnly]

    def get_serializer_class(self):
        """Select serializer based on the request method."""
        if self.request.method in ['PUT', 'PATCH']:
            return BookUpdateSerializer
        return BookSerializer

    def update(self, request, *args, **kwargs):
        """Handle the update operation using the appropriate serializer."""
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
