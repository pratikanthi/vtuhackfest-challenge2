from django import forms
from post.models import Category

CHOICES_SET = Category.objects.all()
CHOICES = []

for cat in CHOICES_SET: CHOICES.append([str(cat.id),str(cat.cat_name)])
res = [tuple(a) for a in CHOICES]
CHOICES = tuple(CHOICES)

# for cat in CHOICES_SET:CHOICES.append(cat.cat_name)

class QuerySubmitForm(forms.Form):
    query_title = forms.CharField(label="Title",max_length=255)
    query_text = forms.CharField(label="Details",widget=forms.Textarea)
    query_cat = forms.ChoiceField(label="Category",choices=CHOICES)

class AnswerForm(forms.Form):
    answer = forms.CharField(label="Your answer",widget=forms.Textarea)
