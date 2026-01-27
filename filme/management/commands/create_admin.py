from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Cria o superuser admin se não existir"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        if not email or not senha:
            self.stdout.write(
                self.style.WARNING(
                    "EMAIL_ADMIN ou SENHA_ADMIN não definidos"
                )
            )
            return

        user, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            }
        )

        if created:
            user.set_password(senha)
            user.save()
            self.stdout.write(
                self.style.SUCCESS("Superuser admin criado com sucesso")
            )
        else:
            self.stdout.write(
                self.style.NOTICE("Superuser admin já existe")
            )
