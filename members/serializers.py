from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    """Serializer for member objects."""

    class Meta:
        model = Member
        fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'role')
