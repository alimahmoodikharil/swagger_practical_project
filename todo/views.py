from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ToDo
from .serializers import ToDoSerializer


class ToDoListView(APIView):
    def get(self, request):
        items = ToDo.objects.all()
        serializer = ToDoSerializer(items, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = ToDoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ToDoDeatilView(APIView):
    def get(self,request, pk):
        item = ToDo.objects.get(id=pk)
        serializer = ToDoSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        item = ToDo.objects.get(id=pk)
        item.delete

        return Response({"message":"item deleted successfully"}, status= status.HTTP_204_NO_CONTENT)