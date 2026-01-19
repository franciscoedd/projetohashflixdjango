from django.apps import AppConfig
from django.db.utils import ProgrammingError, OperationalError


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        from .models import Usuario
        import os

        username = "admin"
        email = os.environ.get("EMAIL_ADMIN", "eduardo-francisco@hotmail.com")
        senha = os.environ.get("SENHA_ADMIN", "Botafogo!2024")

        try:
            # Verifica se o usuário já existe
            if not Usuario.objects.filter(username=username).exists():
                usuario = Usuario(
                    username=username,
                    email=email,
                    is_active=True,
                    is_staff=True,
                    is_superuser=True
                )
                usuario.set_password(senha)  # cria hash da senha
                usuario.save()
        except (OperationalError, ProgrammingError):
            # Ignora erros durante migrate ou se a tabela ainda não existe
            # Evita que o ready() quebre ao iniciar o Django
            pass

        print("EMAIL =", os.environ.get("EMAIL_ADMIN"))
        print("PASSWORD =", os.environ.get("SENHA_ADMIN"))

        #usuarios = Usuario.objects.filter(email=email)
        # if not usuarios:
        #    Usuario.objects.create(username="admin", email=email, is_active=True, is_staff=True)
        #    Usuario.set_password(senha)  # isso faz o hash da senha
        #    Usuario.save()