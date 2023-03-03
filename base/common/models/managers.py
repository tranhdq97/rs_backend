from django.contrib.auth.base_user import BaseUserManager
from django.core.management.base import CommandError

from base.common.constant import message


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        if self.filter(is_admin=True).exists():
            raise CommandError(message.ALREADY_HAVE_SUPER_STAFF)

        user = self.create_user(email, password=password, **kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user
