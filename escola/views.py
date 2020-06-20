# from django.shortcuts import render -> somente se fosse para redenrizar uma pagina
from rest_framework import viewsets
from escola.models import Aluno
from escola.serializer import AlunoSerializer

# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    