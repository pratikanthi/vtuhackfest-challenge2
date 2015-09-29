from django.contrib import admin
from post.models import Query, Answer, Category

class QueryAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class AnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Query,QueryAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Answer,AnswerAdmin)
