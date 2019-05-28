from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, userMail, nickname, password=None):
        if not userMail:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            userMail=self.normalize_email(userMail),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, userMail, nickname, password):
        user = self.create_user(
            userMail=userMail,
            password=password,
            nickname=nickname,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    userMail = models.EmailField(
        verbose_name=_('Email address'),
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        verbose_name=_('Nickname'),
        max_length=30,
        unique=True
    )
    point = models.IntegerField(
        verbose_name=_('Point'),
        default=0
    )
    location = models.CharField(
        verbose_name=_('Location'),
        max_length=30
    )
    is_sharer = models.BooleanField(
        verbose_name=('Is sharer'),
        default=False
    )
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now
    )
    salt = models.CharField(
        verbose_name=_('Salt'),
        max_length=10,
        blank=True
    )
    
    objects = UserManager()

    USERNAME_FIELD = 'userMail'
    REQUIRED_FIELDS = ['nickname',]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.userMail