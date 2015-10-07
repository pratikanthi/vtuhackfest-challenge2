from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from post.forms import QuerySubmitForm, AnswerForm
from post.models import Query, Category, Answer, UserProfile
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

                    title=request.POST.get('query_title'),
                    query_details = request.POST.get('query_text'),
                    query_by = request.user,
                    query_slug = slugify(request.POST.get('query_title')),
                    query_cat = Category.objects.get(id=request.POST.get('query_cat')),

                    )


    new_query.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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

    else:
        form = AnswerForm()
    answers = Answer.objects.filter(answer_to_query = query)
    return render(request,"query.html",{"query":query,"form":form,"answers":answers},)



def fetch_category(request,slug):
    category = Category.objects.get(cat_slug=slug)
    queries = Query.objects.filter(query_cat=category)
    return render(request,"category.html",{"category":category,"queries":queries},)


def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    queries = Query.objects.filter(query_by = request.user )
    answers = Answer.objects.filter(answer_by = request.user)
    return render(request,"profile.html",{"user_profile":user_profile,"queries":queries,"answers":answers,})


def fetch_user(request,slug):
    user = User.objects.get(username=slug)
    queries = Query.objects.filter(query_by = user )
    answers = Answer.objects.filter(answer_by = user)

    if request.user == user:
        return HttpResponseRedirect("/accounts/profile")
    else:
        return render(request,"user.html",{"userr":user,"queries":queries,"answers":answers,},)
