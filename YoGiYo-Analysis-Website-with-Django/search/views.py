from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Restaurants, MenuAnalysis, MenuImg, Wordclouds, Menus
from django.contrib import messages

# Create your views here.
def searching(request):
    if request.method=='POST':
        srch = request.POST['srh']       
        if srch:
            match = Restaurants.objects.filter(restaurant__icontains=srch)
            
            if match:
                return render(request, 'search/search.html', {'sr':match})
            else:
                messages.error(request, '검색 결과가 없습니다.')
        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'search/search.html')



def analysis(request, id):
    rest=get_object_or_404(Restaurants, id=id)
    return render(request, 'search/analysis.html',{'restaurant':rest})
    
    
def menu(request, id):
    rest=get_object_or_404(Restaurants, id=id)
    menu_by_average=MenuAnalysis.objects.filter(restaurant=rest.restaurant).order_by('-average') # 평균별점 큰 순서대로 정렬
    menu_by_count=MenuAnalysis.objects.filter(restaurant=rest.restaurant).order_by('-order_times') # 리뷰갯수 많은 순서대로 정렬
    return render(request, 'search/menu.html', {'rest':rest, 'menu_by_average':menu_by_average, 'menu_by_count':menu_by_count})
    
    
def image(request, id):
    rest=get_object_or_404(Restaurants, id=id) # Restaurants 테이블의 id값이 'id'인 음식점 row를 rest라 함
    menulist=Menus.objects.filter(restaurant=rest.restaurant) # Menus 테이블에서 음식점명이 rest와 같은 음식점 row들을 menulist라 함
    realmenulist=[]
    for menu in menulist:
        a=MenuImg.objects.filter(restaurant=rest.restaurant, menu=menu.menu)
        if a:
            realmenulist.append(menu)
    return render(request, 'search/image.html', {'rest':rest, 'menulist':realmenulist})

def imageview(request, id, mnid):
    rest=get_object_or_404(Restaurants, id=id) # Restaurants 테이블의 id값이 'id'인 음식점 row를 rest라 함
    mn=Menus.objects.get(id=mnid)
    imglist=MenuImg.objects.filter(restaurant=rest.restaurant, menu=mn.menu)
    return render(request, 'search/imageview.html', {'m':mn, 'imglist':imglist})
    
def keyword(request, id):
    rest=get_object_or_404(Restaurants, id=id) # Restaurants 테이블의 id값이 'id'인 음식점 row를 rest라 함
    obj = Wordclouds.objects.filter(restaurant=rest.restaurant)
    if obj:
        posword=obj.filter(pn='pos')
        negword=obj.filter(pn='neg')
        return render(request, 'search/keyword.html', {'rest':rest, 'pos':posword, 'neg':negword})
    else:
        messages.error(request, '리뷰가 존재하지 않아 분석할 수 없습니다.')
            