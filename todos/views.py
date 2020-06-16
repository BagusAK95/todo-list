from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Todo
from .serializers import TodoSerializer
from .pagination import CustomPagination

class get_delete_update_todo(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return todo

    # Get a todo
    def get(self, request, pk):

        todo = self.get_queryset(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a todo
    def put(self, request, pk):
        
        todo = self.get_queryset(pk)

        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a todo
    def delete(self, request, pk):

        todo = self.get_queryset(pk)

        todo.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
   

class get_post_todos(ListCreateAPIView):
    serializer_class = TodoSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
       todos = Todo.objects.all()
       return todos

    # Get all todos
    def get(self, request):
        todos = self.get_queryset()
        paginate_queryset = self.paginate_queryset(todos)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new todo
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

