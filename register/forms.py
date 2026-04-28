from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm): # Dentro dos colchetes é uma herança.
	class Meta:
		model = User
		fields = ("username", "password1", "password2")
	
	def __init__(self, *args, **kwargs):
		super(MyUserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
			'id': 'id_register_username',
			'class': ''
		})
		self.fields['password1'].widget.attrs.update({
			'id': 'id_register_password1',
			'class': ''
		})
		self.fields['password2'].widget.attrs.update({
			'id': 'id_register_password2',
			'class': ''
		})

class MyPasswordChangeForm(PasswordChangeForm): # Dentro dos colchetes é uma herança.

	def __init__(self, *args, **kwargs):
		super(MyPasswordChangeForm, self).__init__(*args, **kwargs)
		self.fields['old_password'].widget.attrs.update({
			'id': 'id_change_old_password',
			'class': ''
		})
		self.fields['new_password1'].widget.attrs.update({
			'id': 'id_change_password1',
			'class': ''
		})
		self.fields['new_password2'].widget.attrs.update({
			'id': 'id_change_password2',
			'class': ''
		})