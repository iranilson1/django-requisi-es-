# Django-requisições web POST e GET e manipulação adicionar, deletar e alterar.
## Fazendo requisições POST e GET usando o django e python, além de manipular informações de Adicionar, Deletar e Alterar do banco de dados pelo django.

Este projeto simples de cadastro de pessoas onde iremos aplicar os metodos post e get alem de manipular o arquivo de banco de dados diretamente pelo django

Inicialmente temos três bibliotecas importantes para o projeto
```
from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
```
Então inicialmente iremos cadastrar pessoas no banco de dados. E só uma observação, aqui não irei abordar sobre models, url ou views, entretanto para melhor entendimento deixarei o codigo feito no models criando suas tabelas no banco de dados.

### MODELS
A parte mais importante de um modelo  e a única parte requerida de um modelo  é a lista de campos de banco de dados que ele define. Campos são especificados através de atributos de classe. 
```
class Pessoas(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(unique=True, max_length=150)

	def __str__(self):
		return "%d-%s"%(self.id,self.nome)
```
### Requisição post e cadastramento
Esta parte pode estar dentro do views ou em uma pasta .py separada.Enfim, como mostrado abaixo estamos requisitando o metodo POST e cadastramento desta pessoa
```
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
```
- Pessoas: é uma classe presente no models mostrado inicialmente, onde criei a tabela recebendo somente nome.
- pessoa: é o objeto criado para receber e incluir o valor no banco de dados
- .save(): Aqui realizamos a finalização e o salvamento no banco de dados 

Basicamente se verifica no if se o metodo requerido é POST, se sim pegamos o 'nome' pelo metodo post e incluimos na variavel nomes. logo apos passamos o nome para a classe Pessoas e salvamos o objeto criado. A parte do contexto é um procedimento que não vou aprofundar, mas é facil de entender.

### Alterar
para altera um nome ja incluido voce so precisara realizar esses procedimentos.
```
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
```
o metodo segue praticamente igual ao cadastramento, então irei explicar somente como se da a alteração.
- pessoa = Pessoas.objects.get(id=id): todo o segredo esta aqui, estamos recebendo o id na função e comparando com o id da class Pessoas e guardando no objeto pessoa 
- pessoa.nome = nome: e aqui estamos passando o novo nome recebido com o que ja esta no banco de dados e assim subistituimos.

### Requisição GETDeletar
E por fim iremos deletar um nome que ja consta no banco de dados
```
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
```
É bem simples como podem ver, basicamente verificamos o metodo GET, e o objetico é fazer uma busca, então por isso o .objects.get(id=id) onde ele pega o id inicial e o id requisitado e apaga logo abaixo.
