from django.contrib import admin
from post.models import Query, Answer, Category, UserProfile

class QueryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'query_slug':('title',),}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'cat_slug':('cat_name',),}

class AnswerAdmin(admin.ModelAdmin):
    pass

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Query,QueryAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
