from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from post.forms import QuerySubmitForm, AnswerForm
from post.models import Query, Category, Answer
from django.template.defaultfilters import slugify
from post.forms import CHOICES

def index(request):
    form = QuerySubmitForm()
    recent_queries = Query.objects.all()
    categories = Category.objects.all()
    return render(request,"index.html", {"form":form,"queries":recent_queries,"categories":categories})


@login_required
def submit(request):
    new_query = Query.objects.create(

                    title=request.POST['query_title'],
                    query_details = request.POST['query_text'],
                    query_by = request.user,
                    query_slug = slugify(request.POST['query_title'])

                    )


    new_query.save()

    return HttpResponse("Your query has been submitted "+request.POST['query_cat'])

def fetch_query(request,slug):
    query = Query.objects.get(query_slug=slug)
    if request.method == 'POST':

        form = AnswerForm(request.POST)

        if form.is_valid():
            new_answer = Answer.objects.create(

                        answer_text = request.POST['answer'],
                        answer_to_query = query,
                        answer_by = request.user

            )
            new_answer.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnswerForm()

    answers = Answer.objects.filter(answer_to_query = query)
    return render(request,"query.html",{"query":query,"form":form,"answers":answers},)



def fetch_category(request,slug):
    category = Category.objects.get(cat_slug=slug)
    return render(request,"category.html",{"category":category,},)



def profile(request):
    return render(request,"profile.html")
