from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("El cliente debe tener un username.")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username = username, 
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id       = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=20, unique=True)
    identity_document = models.CharField('Identity Document', max_length=20, unique=True)
    phone_number = models.CharField('Phone Number',   max_length=100, unique=True)
    password = models.CharField('Password', max_length=256)
    name     = models.CharField('Name',     max_length=50)
    email    = models.EmailField('Email',   max_length=100, unique=True)
    role    = models.CharField('Role',   max_length=15, default="customer")
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects        = UserManager()
    USERNAME_FIELD = 'username'