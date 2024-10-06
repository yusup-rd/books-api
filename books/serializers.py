from rest_framework import serializers
from rest_framework.exceptions import APIException
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'price']

    def validate(self, attrs):
        request_data = self.context['request'].data
        disallowed_fields = ['publication_date', 'author', 'genre']

        for field in disallowed_fields:
            if field in request_data:
                allowed_fields_str = ", ".join(self.Meta.fields)
                exception = APIException(
                    detail=f"You are not allowed to update the {field} field. "
                    f"Fields allowed: {allowed_fields_str}."
                )
                exception.status_code = 400
                raise exception

        return attrs
