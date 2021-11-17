from django.contrib import admin
from accounts.models import User, Post, Response, Action

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Response)
admin.site.register(Action)
# Register your models here.
