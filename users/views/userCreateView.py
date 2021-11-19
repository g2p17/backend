from rest_framework                          import status, views
from rest_framework.response                 import Response

from users.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"state":"Success"}, status=status.HTTP_201_CREATED)