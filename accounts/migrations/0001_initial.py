# Generated by Django 3.2.5 on 2021-11-11 02:35

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('follow_cnt', models.IntegerField(default=0)),
                ('follower_cnt', models.IntegerField(default=0)),
                ('user_pro', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_sen', models.CharField(max_length=350)),
                ('post_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_code', models.CharField(max_length=350)),
                ('like_cnt', models.IntegerField()),
                ('users_id', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('res_id', models.AutoField(primary_key=True, serialize=False)),
                ('users_id', models.IntegerField()),
                ('posts_id', models.IntegerField()),
                ('hen_sen', models.CharField(max_length=350)),
                ('hen_code', models.CharField(max_length=350)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_id', models.IntegerField()),
                ('users_id', models.IntegerField()),
                ('posts_id', models.IntegerField()),
                ('action_cnt', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.post')),
                ('response', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.response')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
