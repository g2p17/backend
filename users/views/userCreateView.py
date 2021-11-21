from rest_framework                          import generics
from rest_framework_simplejwt.serializers    import TokenObtainPairSerializer
from users.serializers.userSerializer        import UserSerializer
from users.models.user import User
from users.serializers.userSerializer import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    def post(self, request, *args, **kwargs):
        '''
        Creates a user (admin/customer)
        '''
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        token_data = {"username":request.data['username'],
                      "password":request.data['password']}
        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        return super().post(request, *args, **kwargs)