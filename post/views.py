from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from post.forms import QuerySubmitForm
from post.models import Query, Category, Answer

def index(request):
    form = QuerySubmitForm()
    recent_queries = Query.objects.all()
    return render(request,"index.html", {"form":form,"queries":recent_queries})

def submit(request):
    new_query = Query.objects.create(
                    title=request.POST['query_title'],
                    query_details = request.POST['query_text'],
                    query_by = request.user,
                    )

    new_query.Catgeory = request.POST['query_cat']
    new_query.save()

    return HttpResponse("Your query has been submitted "+request.POST['query_cat'])
