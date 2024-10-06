from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math


class BooksPagination(PageNumberPagination):
    """Custom pagination class for books."""
    page_size = 5

    def get_paginated_response(self, data):
        """Construct the response for paginated data."""
        total_count = self.page.paginator.count
        total_pages = math.ceil(total_count / self.page_size)

        return Response({
            'current_page': self.page.number,
            'total_pages': total_pages,
            'page_size': len(data),
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
