from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, TextField, ForeignKey


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField()