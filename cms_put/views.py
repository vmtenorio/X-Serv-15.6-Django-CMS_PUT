from django.shortcuts import render
from cms_put.models import Page
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def cms_put(request, rec):
    if request.method == "GET":
        try:
            page = Page.objects.get(name=rec)
            return HttpResponse(page.page)
        except ObjectDoesNotExist:
            return HttpResponse("Content not found", status=404)
    elif request.method == "PUT":
        page = Page(name=rec, page=request.body)
        page.save()
        return HttpResponse("Succesfully added page: " + rec)
    else:
        return HttpResponse("Method not allowed", status=405)
