from users.models.user    import User
from rest_framework       import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'password', 'identity_document',  'phone_number', 'name', 'email']

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        return {
            'id'      : user.id,
            'name'    : user.name,
            'email'   : user.email,
            'username': user.username,
            'phone_number': user.phone_number,
            'identity_document' : user.identity_document,
        }