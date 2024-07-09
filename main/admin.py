from django.contrib import admin
from .models import Skill, PortfolioImage, Services, PortfolioInfo, Blog, Priz, CustomerOpinion, User, BlogSingle
from .forms import SkillForm, ServiceForm, PortfolioDetailsForm, BlogForm, PrizForm, CustomerOpForm, PersonalInfoForm, \
    BlogDetailsForm


class PersonalAdmin(admin.ModelAdmin):
    form = PersonalInfoForm


class SkillAdmin(admin.ModelAdmin):
    form = SkillForm


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceForm


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    fields = ['image']
    extra = 3


class PortfolioInfoAdmin(admin.ModelAdmin):
    form = PortfolioDetailsForm
    list_display = ('name', 'category', 'client', 'project_date', 'project_url')
    inlines = [PortfolioImageInline]


class BlogAdmin(admin.ModelAdmin):
    form = BlogForm


class PrizAdmin(admin.ModelAdmin):
    form = PrizForm


class CustomerOpAdmin(admin.ModelAdmin):
    form = CustomerOpForm


class BlogDetailsAdmin(admin.ModelAdmin):
    form = BlogDetailsForm


admin.site.register(User, PersonalAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Services, ServiceAdmin)
admin.site.register(PortfolioInfo, PortfolioInfoAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Priz, PrizAdmin)
admin.site.register(CustomerOpinion, CustomerOpAdmin)
admin.site.register(BlogSingle, BlogDetailsAdmin)
