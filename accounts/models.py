from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.db import models


class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, user_id, password, **extra_fields):
        if not user_id:
            raise ValueError('The given user_id must be set')
        # email = self.normalize_email(email)
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_id, password, **extra_fields)

    def create_superuser(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(user_id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=20, primary_key=True, help_text='ユーザーID')
    user_name = models.CharField(max_length=20, null=True)
    follow_cnt = models.IntegerField(default=0)
    follower_cnt = models.IntegerField(default=0)
    user_pro = models.CharField(max_length=200, null=True)
    email = models.EmailField(blank=True, null=True)

    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_sen = models.CharField(max_length=350)
    post_time = models.DateTimeField(default=timezone.now)
    post_code = models.CharField(max_length=350)
    like_cnt = models.IntegerField()
    users_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Response(models.Model):
    res_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    users_id = models.IntegerField()
    posts_id = models.IntegerField()
    hen_sen = models.CharField(max_length=350)
    hen_code = models.CharField(max_length=350)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Action(models.Model):
    res_id = models.IntegerField()
    users_id = models.IntegerField()
    posts_id = models.IntegerField()
    action_cnt = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.OneToOneField(Response, on_delete=models.CASCADE)
