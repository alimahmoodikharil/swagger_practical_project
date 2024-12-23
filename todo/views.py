from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from .models import ToDo
from .serializers import ToDoSerializer


class ToDoListView(APIView):
    @swagger_auto_schema(
            operation_description='retrieve all todos',
            responses={200: ToDoSerializer(many=True)}
    )

    def get(self, request):
        items = ToDo.objects.all()
        serializer = ToDoSerializer(items, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
            operation_description='Create new todo',
            request_body=ToDoSerializer,
            responses= {
                201: openapi.Response("Created", ToDoSerializer),
                400: "Bad request"
            }
    )


    def post(self, request):
        serializer = ToDoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ToDoDeatilView(APIView):
    @swagger_auto_schema(
        operation_description="Show the detail of one specific TODO",
        manual_parameters=[
            openapi.Parameter(
            "pk", openapi.IN_PATH, description="PK of TODO", type=openapi.TYPE_INTEGER
            )
        ],
        responses={
             200: ToDoSerializer,
             404: "No content(Not Found)"
        }
    )


    def get(self,request, pk):
        item = ToDo.objects.get(id=pk)
        serializer = ToDoSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="delete a ToDo",
        responses={
            204: "No Content",
            404: "Not Found",
        }
    )


    def delete(self, request, pk):
        item = ToDo.objects.get(id=pk)
        item.delete

        return Response({"message":"item deleted successfully"}, status= status.HTTP_204_NO_CONTENT)