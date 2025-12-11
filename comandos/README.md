Iniciar o projeto Django

```
python -m venv venv
. venv\Scripts\activate
pip install django
django-admin startproject project .
python manage.py startapp contact

```
Configurar o git

```
git config --global user.name "Seu nome"
git config --global user.email "seu_email@gmail.com"
git config --global init.defaultBranch main
git init
git add .
git commit -m "Mensagem"
git remote add origin URL_DO_GIT

```
Migrando a base de dados do Django
```
python manage.py makemigrations
python manage.py migrate
```
Criando e modificando a senha de um super usuário Django

```
python manage.py createsuperuser
python manage.py changepassword USERNAME

```
# python (no shell)

# importe o módulo
from contact.models import Contact
# cria um contato (lazy)
# retorna o contato
contact = Contact(**fields)
contact.save()
# cria um contato (não lazy)
# retorna o contato
contact = Contact.objects.create(**fields)
# seleciona um contato com id 2
# retorna o contato
contact = Contact.objects.get(pk=2)
# edita um contato
# retorna o contato
contact.field_name1 = 'new value 1'
contact.field_name2 = 'new value 2'
contact.save()
# apaga um contato
# depende da base de dados, geralmente retorna o número de valores manipulados na base de dados
contact.delete()
# seleciona todos os contatos ordenando por id DESC
# retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# seleciona contatos usando filtros
# retorna QuerySet[]
contactos = Contact.objects.filter(**filters).order_by('-id')