from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


FAIL = '<h1>Fail</h1>'


def user(request):
    if request.method != 'GET':
        return HttpResponse(FAIL)

    return JsonResponse({
        #'login': request.json.login,
        'login':  "UserLogin",
        'pictures': [
            'picture1:base64::Format',
            'picture2:base64::Format',
            'picture3:base64::Format'
        ]
    })


def sign_in(request):
    if request.method != 'GET':
        return HttpResponse(FAIL)

    data = {
        'status': 'fail',
        'token': 'no-token'
    }
    if request.json.login == request.json.password:
        data['status'] = 'ok'
        data['token'] = request.json.login + '-token'
    return JsonResponse(data)


def sign_up(request):
    if request.method != 'GET':
        return HttpResponse(FAIL)

    data = {
        'status': 'fail'
    }
    if request.json.login == request.json.password:
        data['status'] = 'ok'
    return JsonResponse(data)


def add_picture(request):
    if request.method != 'GET':
        return HttpResponse(FAIL)
    pass
