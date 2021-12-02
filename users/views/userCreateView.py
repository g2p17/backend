from django.http                               import response
from drf_yasg2                                 import openapi
from drf_yasg2.utils                           import swagger_auto_schema
from rest_framework                            import status, views
from rest_framework.response                   import Response
from rest_framework_simplejwt.serializers      import TokenObtainPairSerializer


from users.serializers.userSerializer   import UserSerializer

class UserCreateView(views.APIView):

    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Response('Success response', TokenObtainPairSerializer),
        },
    )
    def post(self, request, *args, **kwargs):
        '''
        Creates a new user (admin/customer)
        '''

        if 'role' in request.data.keys():
            if request.data['role'] == 'admin':
                request.data['role'] = 'customer'

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        token_data = {"username":request.data['username'],
                      "password":request.data['password']}
        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)
