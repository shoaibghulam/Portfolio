from django.contrib import admin
from .models import *
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    
    list_display=(
        'ReviewId',
        'ClientName',
        'clientReview'
    )

admin.site.register(About)
admin.site.register(Cv)
admin.site.register(SkillModel)
admin.site.register(ServiceModel)
admin.site.register(WorkModel)
admin.site.register(SettingModel)
admin.site.register(UsersModel)
admin.site.register(ContactModel)
admin.site.register(Review,ReviewAdmin)