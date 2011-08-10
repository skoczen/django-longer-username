from django.utils.translation import ugettext as _
from django.contrib.auth import forms as auth_forms
from django import forms

from longerusername import MAX_USERNAME_LENGTH

def update_username_field(field):
    field.max_length = MAX_USERNAME_LENGTH()
    field.help_text = _("Required. Only letters, numbers, and @, ., +, -, or _ characters.")

class UserCreationForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        update_username_field(self.fields['username'])

class UserChangeForm(auth_forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        update_username_field(self.fields['username'])

class AuthenticationForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        update_username_field(self.fields['username'])
