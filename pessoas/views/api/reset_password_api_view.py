from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ResetPasswordAPIView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            usuario_id = user.id
            user.usuario_pessoa.uid = uid
            user.usuario_pessoa.token = token
            user.usuario_pessoa.save()
            user.save()

            # Envie o e-mail com o link de redefinição de senha
            reset_password_link = f"http://127.0.0.1:3000/reset-password-confirm/{usuario_id}/{uid}/{token}/"
            send_mail(
                'Redefinição de Senha',
                f'Para redefinir sua senha, clique no link a seguir: {reset_password_link}',
                'app.seeduca@zohomail.com',
                [email],
                fail_silently=False,
            )

        return Response({'message': 'Se existir um usuário com este e-mail, as instruções de redefinição de senha foram enviadas.'}, status=status.HTTP_200_OK)
