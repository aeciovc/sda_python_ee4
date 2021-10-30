from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.forms import CharField, Textarea

from users.models import Profile


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'email']

    biography = CharField(
        label='Tell us your story with movies', widget=Textarea, min_length=40
    )

    def save(self, commit=True):
        self.instance.is_active = False
        new_user = super().save(commit)

        # We should assign Customers group permission
        customer_group = Group.objects.get(name='Customers')
        new_user.groups.add(customer_group)

        biography = self.cleaned_data['biography']
        profile = Profile(biography=biography, user=new_user)
        if commit:
            profile.save()
        return new_user
