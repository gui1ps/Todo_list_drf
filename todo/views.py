from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from todo.models import Todo
from todo.serializers import TodoSerializer

def get_instance(pk):
    try:
        return Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_tasks(request):
    all_tasks=Todo.objects.all()
    all_tasks_serializer=TodoSerializer(all_tasks,many=True)
    return Response(all_tasks_serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_task(request):
    task_serializer=TodoSerializer(data=request.data)
    if task_serializer.is_valid():
        task_serializer.save()
        return Response(task_serializer.data,status=status.HTTP_201_CREATED)
    return Response(task_serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET'])
def get_task(request,pk):
    task=get_instance(pk)
    tasks_serializer=TodoSerializer(task)
    return Response(tasks_serializer.data,status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_task(request,pk):
    task=get_instance(pk)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update(request,pk):
    task=get_instance(pk)
    task_serializer=TodoSerializer(task,data=request.data)
    if task_serializer.is_valid():
        task_serializer.save()
        return Response(task_serializer.data,status=status.HTTP_200_OK)
    return Response(task_serializer.errors,status=status.HTTP_400_BAD_REQUEST)