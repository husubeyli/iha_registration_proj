from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text="The email field is required.")

    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        # labels = {
        #     'username': 'Ad',
        #     'email': 'Elektron poçt ünvanı'
        # }
        # error_messages = {
        #         "password_incorrect": _("Cari şifrə yanlışdır"),
        #         "password_mismatch": _("Şifrə təsdiqləməsi yanlışdır"),
        #         "email_unique": _("Bu elektron poct adressli istifadəçi artıq mövcuddur"),
        #         "phone_invalid" : _("Nömrənin son 7 rəqəmini daxil edin (yəni, prefixsiz)"),
        #         "short_password": _("Şifrə minimum 6 simvoldan ibarət olmalıdır"),
        #         "only_english_letters": _("Yalnız ingilis hərfləri"),
        #     }

        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists")
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username = username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists")
    
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user