from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Review
from .forms import ReviewForm
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.core.paginator import Paginator

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def service(request):
    return render(request, 'pages/service.html')

# def review(request):
#     page = request.GET.get('page', '1')
#     review_list = Review.objects.order_by('-create_date')
#     paginator = Paginator(review_list, 5)
#     page_obj = paginator.get_page(page)
#     context = {'review_list': page_obj}
#     return render(request, 'pages/review.html', context)
#
# def review_create(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.author = request.user
#             review.create_date = timezone.now()
#             review.save()
#             return redirect('page:review')
#     else:
#         form = ReviewForm()
#     context = {'form': form}
#     return render(request, 'pages/review.html', context)

def review(request):
    if request.method == 'POST':
        # POST 요청일 경우 리뷰 생성 처리
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.create_date = timezone.now()
            review.save()
            return redirect('pages:review')
    else:
        # GET 요청일 경우 리뷰 목록 페이지 표시
        page = request.GET.get('page', '1')
        review_list = Review.objects.order_by('-create_date')
        paginator = Paginator(review_list, 5)
        page_obj = paginator.get_page(page)
        form = ReviewForm()

    context = {'review_list': page_obj, 'form': form}
    return render(request, 'pages/review.html', context)

@login_required(login_url='common:login')
def review_modify(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pages:review', review_id=review.id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.modify_date = timezone.now()  # 수정일시 저장
            review.save()
            return redirect('pages:review', review_id=review.id)
    else:
        form = ReviewForm(instance=review)
    context = {'form': form}
    return render(request, 'pages/review.html', context)

def detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'pages/review_detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print('contact 호출')
        if form.is_valid():
            contact = form.save(commit=False)
            contact.create_date = timezone.now()
            contact.save()
            return redirect('pages:contact')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'pages/contact.html', context)


def contact_detail(request, contact_id):
    contact_index = get_object_or_404(Contact, pk=contact_id)
    context = {'contact': contact}
    return render(request, 'pages/contact_detail.html', context)

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/signup.html')

