from django.shortcuts import render, redirect
from django.urls import reverse
from httpx import post
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from .models import Skill, Services, PortfolioImage, PortfolioInfo, Blog, Priz, CustomerOpinion, BlogSingle, User, \
    Comment


# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get('email')
        message = request.POST.get('message')
        full_message = f"{email} dan sizga quyidagi habar keldi:\n\n\n{message}"

        try:
            send_mail(
                f'{name} sizga habar yubordi.',
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER, ],
                fail_silently=False,
            )
            return redirect('index')
        except Exception as e:
            print(f"Email yuborishda xato: {e}")
            return HttpResponse(f"Xato yuz berdi : {e}")

    skills = Skill.objects.all()
    services = Services.objects.all()
    blog = Blog.objects.all()
    priz = Priz.objects.all()
    customer_opinion = CustomerOpinion.objects.all()
    main_portfolio = PortfolioInfo.objects.all()
    image_portfolio = PortfolioInfo.objects.all()
    personal_info = User.objects.all()
    users = User.objects.filter(id=request.user.id).first()
    return render(request, 'index.html',
                  {'skills': skills, 'services': services, 'blog': blog, 'priz': priz,
                   'customer_opinion': customer_opinion, 'main_portfolios': main_portfolio, 'personal': personal_info,
                   'user': users, 'image_portfolio': image_portfolio})


def blog_single(request):
    blog = Blog.objects.all()
    blog_article = BlogSingle.objects.all()
    return render(request, 'blog-single.html', {'blog_article': blog_article, 'blog': blog})


def portfolio_details(request, id):
    portfolio = PortfolioInfo.objects.filter(id=id).first()
    portfolios = PortfolioInfo.objects.all()
    return render(request, 'portfolio-details.html', {'portfolio': portfolio, 'portfolios': portfolios})


def send_message(message):
    url = f'https://api.telegram.org/bot6108967749:AAH7aVD7nSyHk6FZjdOjLWdHbYiVFkS_6rU/sendmessage'
    params = {
        'chat_id': 5467465403,
        'text': message
    }
    post(url, params=params)


def commentfunc(request, pk):
    blog = Blog.objects.filter(id=pk).first()
    personal_info = User.objects.first()
    if not blog:
        return redirect('error_page')

    if request.POST:
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        post_id = pk
        text = request.POST.get('text')
        if fullname and post_id and text and email:
            Comment.objects.create(
                fullname=fullname, email=email, post_id_id=post_id, text=text)
            return redirect(reverse('post', args=(pk,)))

    searchs = ''
    if request.GET:
        key = request.GET.get('s')
        searchs = BlogSingle.objects.filter(title__contains=key)

    comments = Comment.objects.filter(post_id=pk).order_by('created_at')
    return render(request, 'blog-single.html',
                  {'comments': comments, 'searchs': searchs, 'blog': blog, 'personal_info': personal_info})
