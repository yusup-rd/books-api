from rest_framework import serializers
from rest_framework.exceptions import APIException
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model including all fields."""

    class Meta:
        model = Book
        fields = '__all__'


class BookUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating specific fields of the Book model."""

    class Meta:
        model = Book
        fields = ['title', 'description', 'price']

    def validate(self, attrs):
        """Validate the input data for the update operation."""

        request_data = self.context['request'].data
        disallowed_fields = {
            x for x in request_data.keys() if x not in self.Meta.fields
        }
        invalid_fields = disallowed_fields.intersection(request_data.keys())

        if invalid_fields:
            allowed_fields_str = ", ".join(self.Meta.fields)
            exception = APIException(
                detail=f"You are not allowed to update the {
                    ', '.join(invalid_fields)} fields. "
                f"Fields allowed: {allowed_fields_str}."
            )
            exception.status_code = 400
            raise exception

        return attrs
