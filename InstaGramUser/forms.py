from InstaGramUser import models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.MyUser
        fields = ['displayname', 'age']