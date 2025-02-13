import secrets

from rest_framework import serializers
from django.utils import timezone

from crudapp.models import AccessToken


class AccessTokenSerializer(serializers.ModelSerializer):
    """Serializer for AccessToken with validation and token management."""
    token_time_limit = serializers.SerializerMethodField()

    class Meta:
        model = AccessToken
        fields = ['user', 'token', 'token_time_limit', 'created']

    def validate_token_time_limit(self, obj):
        """Check if the token is still valid based on TTL."""
        return timezone.now() < obj.created + timezone.timedelta(milliseconds=obj.token_time_limit)

    @staticmethod
    def generate_token(user):
        """Generate a new secure token for a user."""
        token = secrets.token_urlsafe(32)
        return AccessToken.objects.create(user=user, token=token)