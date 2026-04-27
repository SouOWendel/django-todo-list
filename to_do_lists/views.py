from django.shortcuts import render
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
		form = TarefaForm()
		context = {
			'message': 'Hello, world!',
			'form': form,
			'tarefasConcluidas': tarefasConcluidas,
			'tarefasNaoConcluidas': tarefasNaoConcluidas,
		}
		return render(request, 'to_do_lists/index.html', context)
	else:
		return render(request, 'to_do_lists/index.html')