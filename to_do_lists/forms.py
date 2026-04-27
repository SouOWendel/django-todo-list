from django import forms

class TarefaForm(forms.Form):
	tarefa = forms.CharField(
		max_length=500,
		required=True,
		widget=forms.TextInput(attrs={
			'id': 'id_tarefa',
			'class': '',
			'placeholder': 'Digite sua tarefa...'
		})
	)