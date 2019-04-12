from django.shortcuts import render
from django.http import JsonResponse

from .serializers import ListSerializer, ListSerializer2,TaskSerializer
from .models import TaskList,Task
from django.views.decorators.csrf import csrf_exempt
from .models import TaskList,Task
import json
# Create your views here.


@csrf_exempt
def lists(request):
    if request.method == 'GET':
        all_lists = TaskList.objects.all()
        ser=ListSerializer(all_lists,many=True)
        return JsonResponse(ser.data, safe=False,status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        ser=ListSerializer2(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201)
        return JsonResponse(ser.errors)

@csrf_exempt
def task_list_detail(request,pk):
    try:
        li = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)},safe=False)
    if request.method=='GET':
        ser=ListSerializer(li)
        return JsonResponse(ser.data,status=200)
    elif request.method=="PUT":
        data=json.loads(request.body)
        ser=ListSerializer(instance=li,data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=200)
        return JsonResponse(ser.errors)
    elif request.method=='DELETE':
        li.delete()
        return JsonResponse({},status=204)

@csrf_exempt
def list_tasks(request,pk):
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    if request.method =='GET':
        tasks = list.task_set.all()
        ser = TaskSerializer(tasks, many=True)
        return JsonResponse(ser.data, safe=False,status=200)
    # elif request.method=="PUT":
    #     data=json.loads(request.body)
    #     ser=TaskSerializer(data=data)
    #     if ser.is_valid():
    #         ser.save()
    #         return JsonResponse(ser.data,status=200)
    #     return JsonResponse(ser.errors)


