from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.response import Response

class testView():
    # queryset=relations.objects.all()
    # serializer_class = relationsSerializer

    def p_req(request):
        if(request.method=='GET'):
            render(request,str("Test"))
        # return Response()