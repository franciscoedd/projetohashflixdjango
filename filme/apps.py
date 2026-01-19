from django.apps import AppConfig

class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        from .models import Usuario
        import os
        from django.db.utils import OperationalError

        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        if not email or not senha:
            # Se as variáveis não estão definidas, não faz nada
            return

        try:
            # Só cria se não existir
            if not Usuario.objects.filter(username="admin").exists():
                usuario = Usuario(
                    username="admin",
                    email=email,
                    is_active=True,
                    is_staff=True,
                    is_superuser=True
                )
                usuario.set_password(senha)  # Criptografa a senha
                usuario.save()
        except OperationalError:
            # Banco ainda não está pronto (migrations não aplicadas)
            pass

#    def ready(self):
#        from .models import Usuario
#        import os
#
#        email = os.getenv("EMAIL_ADMIN")
#        senha = os.getenv("SENHA_ADMIN")
#       usuarios = Usuario.objects.filter(email=email)
#       if not usuarios:
#           Usuario.objects.create(username="admin", email=email, password=senha, is_active=True, is_staff=True)