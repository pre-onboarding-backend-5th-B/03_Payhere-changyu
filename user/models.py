from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    # 일반 유저 생성
    def create_user(self, email, name, password):
        if not email:
            raise ValueError("Users must have an email")
        if not name:
            raise ValueError("Users must have an name")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 유저 생성
    def create_superuser(self, email, name, password):
        superuser = self.create_user(
            email=email,
            name=name,
            password=password,
        )

        superuser.is_admin = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=100, unique=True, blank=False)
    name = models.CharField(verbose_name="name", max_length=100, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return f"email: {self.email} / name: {self.name}"

    class Meta:
        db_table = "user"
