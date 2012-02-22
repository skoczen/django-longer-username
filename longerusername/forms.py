from django.utils.translation import ugettext as _
from django.core.validators import MaxLengthValidator
from django.contrib.auth import forms as auth_forms
from django import forms

from longerusername import MAX_USERNAME_LENGTH

def update_username_field(field):
    field.widget.attrs['maxlength'] = MAX_USERNAME_LENGTH()
    field.max_length = MAX_USERNAME_LENGTH()
    field.help_text = _("Required, %s characters or fewer. Only letters, "
                        "numbers, and characters such as @.+_- are "
                        "allowed." % MAX_USERNAME_LENGTH())

    # we need to find the MaxLengthValidator and change its
    # limit_value otherwise the auth forms will fail validation
    for v in field.validators:
        if isinstance(v, MaxLengthValidator):
            v.limit_value = MAX_USERNAME_LENGTH()

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
