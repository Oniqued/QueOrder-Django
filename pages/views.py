from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Review
from .forms import ReviewForm
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

def detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'pages/review_detail.html', context)

def contact(request):
    return render(request, 'pages/contact.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/signup.html')

