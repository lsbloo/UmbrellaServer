from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.views import APIView


class UserLogin(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        # caso queria fazer alguma personalização faça aqui
        return obtain_jwt_token(request)
