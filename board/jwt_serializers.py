from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer
)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)
        token["username"] = user.username
        token["roles"] = list(
            user.groups.values_list("name", flat=True)
        )
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
            "roles": list(
                self.user.groups.values_list("name", flat=True)
            ),
        }
        return data