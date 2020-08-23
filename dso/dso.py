from rest_framework import generics
from .serializers import *
from .models import *

# Read Only API -- GET

class ReadOneView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = relationsSerializer
    queryset = relations.objects.all()

class ReadAllView(generics.ListAPIView):
    queryset=relations.objects.all()
    serializer_class = relationsSerializer
    
    # def get_serializer_class(self,filename):
    #     print(filename)
    #     queryset=relations.objects.all()
    #     if(filename=='relations'):
    #         serializer_class = relationsSerializer
    #     elif(filename=='relation_desc'):
    #         serializer_class = relationDescSerializer
    #     elif(filename=='relation_hierarchy'):
    #         serializer_class = relationHierarchySerializer

# # Read n Write API -- POST
class ReadnWriteView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = relationsSerializer
    queryset = relations.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class ReadnUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = relationsSerializer
    queryset = relations.objects.all()

class ReadnDeleteView(generics.RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = relationsSerializer
    queryset = relations.objects.all()

class ReadnUpdatenDeleteView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = relationsSerializer
    queryset = relations.objects.all()

# # Delete API -- DELETE
class DeleteView(generics.DestroyAPIView):
    lookup_field='id'
    serializer_class = relationsSerializer
    queryset = relations.objects.all()

    def perform_destroy(self, serializer):
        serializer.delete()

# # Update API -- PUT, PATCH
class UpdateView(generics.UpdateAPIView):
    lookup_field='id'
    serializer_class = relationsSerializer
    queryset = relations.objects.all()
    
    def perform_update(self, serializer):
        serializer.save()