from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def cadastrarPessoas(request):
	if(request.method == 'POST'):
		nomes = request.POST['nome']
		pessoa = Pessoas(nome=nomes)
		pessoa.save()

	#contexto
	mensagem = 'Teste'
	alert = 'alert-success'
	listaPessoas = Pessoas.objects.all()

	context={'mensagem':mensagem, 'alert':alert, 'listaPessoas':listaPessoas}
	render(request, 'pessoas.html', context)


def alterarPessoas(request, id=None):
	if(request.method =='POST'):
		nome = request.POST['nome']
		pessoa = Pessoas.objects.get(id=id)
		pessoa.nome = nome
		pessoa.save()

	#contexto
	mensagem = 'Teste'
	alert = 'alert-success'
	listaPessoas = Pessoas.objects.all()

	context={'mensagem':mensagem, 'alert':alert, 'listaPessoas':listaPessoas}
	render(request, 'pessoas.html', context)


def deletarPessoas(request, id=None):
	if(request.method == 'GET'):
		pessoa = Pessoas.objects.get(id=id)
		pessoa.delete()

	#contexto
	mensagem = 'Teste'
	alert = 'alert-success'
	listaPessoas = Pessoas.objects.all()

	context={'mensagem':mensagem, 'alert':alert, 'listaPessoas':listaPessoas}
	render(request, 'pessoas.html', context)


