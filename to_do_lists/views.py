from django.shortcuts import render, redirect
from .forms import TarefaForm
from .models import Tarefa

def index(request):
	if request.user.is_authenticated:
		tarefasTotal = Tarefa.objects.filter(user=request.user)
		if tarefasTotal is not None:
			tarefasConcluidas = []
			tarefasNaoConcluidas = []
			for tarefa in tarefasTotal:
				if tarefa.concluido == True:
					tarefasConcluidas.append(tarefa)
				else:
					tarefasNaoConcluidas.append(tarefa)
		else:
			tarefasConcluidas = None
			tarefasNaoConcluidas = None

		if request.method == 'POST':
			form = TarefaForm(request.POST)
			if form.is_valid(): # Confere se há erros.
				usuario = request.user
				tarefa = form.cleaned_data['tarefa']
				concluido = False
				novaTarefa = Tarefa.objects.create(
					user=usuario, tarefa=tarefa, concluido=concluido
				)
				novaTarefa.save()
				return redirect('index')
		else:
			form = TarefaForm()
			
			context = {
				'form': form,
				'tarefasConcluidas': tarefasConcluidas,
				'tarefasNaoConcluidas': tarefasNaoConcluidas,
			}
			return render(request, 'to_do_lists/index.html', context)
	else:
		return render(request, 'to_do_lists/index.html')