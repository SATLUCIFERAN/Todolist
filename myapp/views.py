from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist


#GET data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() # ดึงข้อมูลจาก model Todolist,คล้าย ๆ กับ "SELECT * from Todolist"
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
    

#Post data(save data to database)
@api_view(['POST'])
def post_todolist(request):
    if request.method ==  'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def update_todolist(request,TID):

    todo = Todolist.objects.get(id= TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'update'
            return Response(data=data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id= TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data,status=statuscode)














data = [
    {
        "title":"อันว่าดนตรีคืออะไร",
        "subtitle":"คือการทำให้เพื่อนบ้านรำคาญ",
        "image_url":"https://raw.githubusercontent.com/SATLUCIFERAN/BasicAPI/main/piano.jpg",
        "detail":"99999999999999999999999"
    },
 
    {
        "title":"Saxophone คือ",
        "subtitle":"เพื่อนที่ดีที่สุดของเรา",
        "image_url":"https://raw.githubusercontent.com/SATLUCIFERAN/BasicAPI/main/piano.jpg",
        "detail":"3333333333333333333333333333"
    },
    {
        "title":"ระนาดเอกคือ คือ",
        "subtitle":"คุณครูของเราที่สอนสั่งเรามา",
        "image_url":"https://raw.githubusercontent.com/SATLUCIFERAN/BasicAPI/main/piano.jpg",
        "detail":"4444444444444444444444444444"
    },
    {
        "title":"Piano(Upright) คือ",
        "subtitle":"เพื่อนที่ดีที่สุดของเรา",
        "image_url":"https://raw.githubusercontent.com/SATLUCIFERAN/BasicAPI/main/piano.jpg",
        "detail":"3333333333333333333333333333"
    }
]



def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii':False})
