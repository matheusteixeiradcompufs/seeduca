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
    """
    Uma API view para enviar e-mails de redefinição de senha.

    Esta view permite que os usuários solicitem a redefinição de senha, envia um e-mail com um link
    de redefinição de senha e processa a solicitação.

    Para usar esta view, os usuários devem fornecer um email válido no corpo da solicitação POST.

    Uma vez que o email é verificado e associado a um usuário, um token único é gerado e salvo junto
    com o UID do usuário. Um email é então enviado para o endereço fornecido com um link contendo
    o UID, o token e o ID do usuário para redefinir a senha.

    As permissões para esta view são definidas como AllowAny, permitindo que qualquer usuário,
    autenticado ou não, acesse esta API.
    """
    permission_classes = [
        AllowAny,  # Permite acesso a qualquer usuário, autenticado ou não
    ]

    @staticmethod
    def post(request):
        """
        Processa a solicitação POST para redefinir a senha.

        Recebe um email no corpo da solicitação POST, verifica se o email está associado a um usuário
        e, em caso afirmativo, envia um email com um link de redefinição de senha.

        Retorna uma resposta com uma mensagem indicando se o email foi enviado com sucesso ou se não
        existe um usuário com o email fornecido.

        :param request: A solicitação HTTP enviada pelo cliente.
        :return: Uma resposta HTTP indicando o resultado da operação.
        """
        email = request.data.get('email')  # Obtém o email do corpo da solicitação

        user = User.objects.filter(email=email).first()  # Verifica se o email está associado a um usuário

        if user:
            # Gera um token único para redefinição de senha e codifica o UID do usuário
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            usuario_id = user.id

            # Salva o token e o UID no objeto de usuário
            user.usuario_pessoa.uid = uid
            user.usuario_pessoa.token = token
            user.usuario_pessoa.save()
            user.save()

            # Constrói o link de redefinição de senha
            reset_password_link = f"http://127.0.0.1:3000/reset-password-confirm/{usuario_id}/{uid}/{token}/"

            # Envia o email de redefinição de senha para o endereço fornecido
            send_mail(
                'Redefinição de Senha',
                f'Para redefinir sua senha, clique no link a seguir: {reset_password_link}',
                'app.seeduca@zohomail.com',
                [email],
                fail_silently=False,
            )

            # Retorna uma resposta indicando que as instruções foram enviadas com sucesso
            return Response(
                {'message': 'As instruções de redefinição de senha foram enviadas.'},
                status=status.HTTP_200_OK
            )
        else:
            # Retorna uma resposta indicando que não existe um usuário com o email fornecido
            return Response(
                {'message': 'Não existe um usuário com esse email.'},
                status=status.HTTP_404_NOT_FOUND
            )
