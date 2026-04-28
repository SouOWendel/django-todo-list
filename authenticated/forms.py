from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(
		required=True,
		widget=forms.TextInput(attrs={
			'id': 'id_login_username',
			'class': '',
		})
	)
	password = forms.CharField(
		required=True,
		widget=forms.PasswordInput(attrs={
			'id': 'id_login_password',
			'class': '',
		})
	)