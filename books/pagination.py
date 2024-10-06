from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math


class BooksPagination(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        return Response({
            'current_page': self.page.number,
            'total_pages': math.ceil(self.page.paginator.count / self.page_size),
            'page_size': len(data),
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
