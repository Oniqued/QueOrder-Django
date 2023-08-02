from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Review
from .models import Contact

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Review, ReviewAdmin)
admin.site.register(Contact)