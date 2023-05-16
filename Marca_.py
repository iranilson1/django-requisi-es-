from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from .models import *



@login_required(redirect_field_name='',login_url="index")
def pessoas(request):
	if(request.method == 'GET'):
		listaPessoa = Pessoas.objects.all().order_by('nome')
		context = {"listaPessoa":listapessoa}
		return render(request, 'pessoas.html', context)
	else:
		return render(request, 'nao-autorizado.html')


@login_required(redirect_field_name='',login_url="index")
def cadastrarPessoa(request):
	if(request.method == 'POST'):
		mensagem = ''
		alert = 'alert-success'
		try:
			nome = request.POST['nome']
			pessoa = Pessoas(nome=nome)
			pessoa.save()
			mensagem = 'Pessoa "%s" foi cadastrada com sucesso.'%(nome)

		except Exception as e:
			mensagem = 'Erro ao cadastrar Pessoa. Consulte o responsável e informe: "%s"'%(str(e))
			alert = 'alert-danger'

		listaPessoa = Pessoas.objects.all()
		context={'mensagem':mensagem, 'alert':alert, 'listaPessoa':listaPessoa}
		return render(request, 'cadastraPessoa.html', context)
	
	elif(request.method == 'GET'):
		return render(request, 'cadastraPessoa.html')
	
	else:
		return render(request, 'nao-autorizado.html')


@login_required(redirect_field_name='',login_url="index")
def alterarPessoa(request, codigo=None):
	if(request.method =='POST'):
		mensagem = ''
		alert = 'alert-success'
		try:
			nome = request.POST['nome']
			pessoa = Pessoas.objects.get(id=int(codigo))
			nomeAntigo = pesssoa.nome
			pessoa.nome = nome
			pessoa.save()
			mensagem = 'Pessoa "%s" foi alterada com sucesso para "%s".'%(nomeAntigo, nome)
		except Exception as e:
			mensagem = 'Erro ao alterar Pessoa. Consulte o responsável e informe: "%s"'%(str(e))
			alert = 'alert-danger'

		listaPessoa = Pessoa.objects.all().order_by('nome')
		context={'mensagem':mensagem, 'alert':alert, 'listaPessoa':listaPessoa}
		return render(request,'pessoa.html',context)
	elif(request.method == 'GET'):
		try:
			pessoa=Pessoas.objects.get(id=int(codigo))
			context={'pessoa':pessoa}
			return render(request, 'alteraPessoa.html', context=context)
		except Exception as e:
			mensagem = 'Erro ao alterar pessoa. Consulte o responsável e informe: "%s"'%(str(e))
			alert = 'alert-danger'
			listaPessoa = Pessoa.objects.all().order_by('nome')

			context={'mensagem':mensagem, 'alert':alert, 'listaPessoa':listaPessoa}
			return render(request,'pessoas.html',context)
	else:
		return render(request, 'nao-autorizado.html')


@login_required(redirect_field_name='',login_url="index")
def deletarpessoa(request, codigo=None):
	if(request.method == 'GET'):
		mensagem = ''
		alert = 'alert-success'
		try:
			pessoa = Pesoas.objects.get(id=int(codigo))
			pessoa.delete()
			mensagem = 'pessoa "%s" foi deletada com sucesso.'%(pessoa.nome)
		
		except Exception as e:
			mensagem = 'Erro ao deletar pessoa. Consulte o responsável e informe: "%s"'%(str(e))
			alert = 'alert-danger'

		listaPessoa = pessoas.objects.all().order_by('nome')
		context={'mensagem':mensagem, 'alert':alert,'listaPessoa':listaPessoa}
		return render(request,'pessoa.html',context)
	else:
		return render(request, 'nao-autorizado.html')


@login_required(redirect_field_name='',login_url='index')
def pesquisarPessoas(request):
	if(request.method=='GET'):
		filtro = request.GET.get('filtro', None)
		pessoas = [str(x) for x in Pessoas.objects.filter(nome__icontains = filtro).order_by('nome')]
		data = {'pessoas':pessoas}
		return JsonResponse(data)




