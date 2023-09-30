from django.shortcuts import render, redirect
from .models import Lanches, Almocos, Tabela
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def site(request):
  lanches = Lanches.objects.all()
  almocos = Almocos.objects.all()
  tabela = Tabela.objects.all()
  return render(request,"site.html", context={ "lanches": lanches , "almocos": almocos, "tabela": tabela})

@login_required
def create_almoco(request):
  if request.method == "POST":
    Almocos.objects.create(
      titulo = request.POST["titulo"],
      localizacao = request.POST["localizacao"],
      notaComida = request.POST["notacomida"],
      notaPreco = request.POST["notapreco"]
    )
    return redirect("site")
  return render(request, "formsAlmoco.html")

@login_required
def create_lanche(request):
  if request.method == "POST":
    Lanches.objects.create(
      titulo = request.POST["titulo"],
      localizacao = request.POST["localizacao"],
      melhorLanche = request.POST["melhorlanche"],
      nota = request.POST["nota"]
    )
    return redirect("site")
  return render(request, "formsLanche.html")

@login_required
def create_tabela(request):
  if request.method == "POST":
    Tabela.objects.create(
      restaurante = request.POST["restaurante"],
      nota = request.POST["nota"]
    )
    return redirect("site")
  return render(request, "formsTabela.html")

@login_required
def update_lanche(request, id):
  lanches = Lanches.objects.get(id = id), 
  if request.method == "POST":
      lanches.titulo = request.POST["titulo"] 
      lanches.localizacao = request.POST["localizacao"]
      lanches.melhorLanche = request.POST["melhorlanche"]
      lanches.nota = request.POST["nota"]
      lanches.save()
      return redirect("site")
  return render(request, "formsLanche.html",  context={"action":"Atualizar", lanches:"lanche"})

@login_required
def update_almoco(request, id):
  almocos = Almocos.objects.get(id = id), 
  if request.method == "POST":
      almocos.titulo = request.POST["titulo"] 
      almocos.localizacao = request.POST["localizacao"]
      almocos.melhorLanche = request.POST["melhorlanche"]
      almocos.nota = request.POST["nota"]
      almocos.save()
      return redirect("site")
  return render(request, "formsAlmoco.html",  context={"action":"Atualizar", almocos: "almoco"})

@login_required
def delete_lanche(request, id):
  lanches = Almocos.objects.get(id = id), 
  if request.method == "POST":
      lanches.delete()
      return redirect("site")
  return render(request, "areyousureLanche.html",context={lanches:"lanche"}) 

@login_required
def delete_almoco(request, id):
  almocos = Almocos.objects.get(id = id), 
  if request.method == "POST":
      almocos.delete()
      return redirect("site")
  return render(request, "areyousureAlmoco.html",context={almocos:"almoco"})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST['username'],
      request.POST['email'],
      request.POST['password']);
    user.save()
    return redirect("login")
  return render(request, "register.html", context={"action":"Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect("site")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")