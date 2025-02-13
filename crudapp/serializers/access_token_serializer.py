import secrets

from rest_framework import serializers

from crudapp.models import AccessToken


class AccessTokenSerializer(serializers.ModelSerializer):
    """Serializer for AccessToken with validation and token management."""

    class Meta:
        model = AccessToken
        fields = ['user', 'token', 'token_time_limit', 'created']

    @staticmethod
    def generate_token(user):
        """Generate a new secure token for a user."""
        token = secrets.token_urlsafe(32)
        return AccessToken.objects.create(user=user, token=token)