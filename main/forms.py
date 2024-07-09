from django import forms

from .models import Skill, Services, PortfolioInfo, Blog, Priz, CustomerOpinion, BlogSingle, User


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'tel_num', 'image', 'about_me', 'email', 'job']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'percentage']

    def clean_percentage(self):
        percentage = self.cleaned_data.get('percentage')
        if percentage < 0 or percentage > 100:
            raise forms.ValidationError('Percentage must be between 0 and 100.')
        return percentage


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'description']


class PortfolioDetailsForm(forms.ModelForm):
    class Meta:
        model = PortfolioInfo
        fields = ['category', 'client', 'project_url', 'example_detail', 'client_url', 'project_date']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'category', 'description', 'image']


class PrizForm(forms.ModelForm):
    class Meta:
        model = Priz
        fields = ['title', 'amount']


class CustomerOpForm(forms.ModelForm):
    class Meta:
        model = CustomerOpinion
        fields = ['name', 'description']


class BlogDetailsForm(forms.ModelForm):
    class Meta:
        model = BlogSingle
        fields = ['title', 'name', 'job', 'comment', 'article', 'main_data']
