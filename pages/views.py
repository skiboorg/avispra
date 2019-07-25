from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .models import *
#from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from .forms import CreateForm
from .forms import *
import json

def index(request):
    new_form = CreateForm()
    page_info = Page.objects.first()
    title = page_info.index_title
    description = page_info.index_description
    keywords = page_info.index_keywords
    return render(request, 'index.html', locals())

def robots(request):
    return render(request, 'robots.txt')

def sitemap(request):
    return render(request, 'sitemap.xml', content_type = "application/xhtml+xml")

def createForm(request):
    return_dict = {}
    if request.POST:

        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                new_form = Forms(file=request.FILES['file'])
            except MultiValueDictKeyError:
                new_form = False
            form.save()
            return_dict['result'] = 'ok'
        else:
            return_dict['result'] = 'error'
            return_dict['errors'] = form.errors
            print(form.errors)
    return JsonResponse(return_dict)
  #  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def about(request):

    new_form = CreateForm()
    page_info = Page.objects.first()
    title = page_info.about_title
    description = page_info.about_description
    keywords = page_info.about_keywords
    header_section1 = page_info.about_header_section1
    text1_section1 = page_info.about_text1_section1
    text2_section1 = page_info.about_text2_section1
    header_section2 = page_info.about_header_section2
    text1_section2 = page_info.about_text1_section2
    header_section3 = page_info.about_header_section3

    slider = AboutSlider.objects.filter(is_active=True)
    clients = AboutPageClients.objects.filter(is_active=True)
    works = AboutPageWork.objects.filter(is_active=True)

    return render(request, 'about.html', locals())


def portfolio(request):
    new_form = CreateForm()
    categories = Category.objects.filter(is_active=True)
    page_info = Page.objects.first()
    title = page_info.category_main_title
    description = page_info.category_main_description
    keywords = page_info.category_main_keywords

    return render(request, 'category_main.html', locals())

def portfolio_cat(request,cat_name_slug):
    new_form = CreateForm()
    category = Category.objects.get(name_slug=cat_name_slug)
    if category:
        items = Item.objects.filter(category=category)
        title = category.title
        description = category.description
        keywords = category.keywords
    return render(request, 'category.html', locals())

def portfolio_item(request,cat_name_slug,item_name):
    new_form = CreateForm()
    item = Item.objects.get(name_slug=item_name)
    category = Category.objects.get(name_slug=cat_name_slug)
    if item:
        images= ItemImage.objects.filter(item=item)
        title = item.title
        description = item.description
        keywords = item.keywords
    return render(request, 'item.html', locals())

def contacts(request):
    page_info = Page.objects.first()
    title = page_info.contact_title
    description = page_info.contact_description
    keywords = page_info.contact_keywords
    contact_header_section1 = page_info.contact_header_section1
    contact_text1_section1 = page_info.contact_text1_section1
    contact_header_section2 = page_info.contact_header_section2
    contact_text1_section2 = page_info.contact_text1_section2
    return render(request, 'contacts.html', locals())

def services(request):
    new_form = CreateForm()
    page_info = Page.objects.first()
    title = page_info.services_item_title
    description = page_info.services_item_description
    keywords = page_info.services_item_keywords

    all_services = Services.objects.all()

    header_section1 = page_info.services_header_section1
    services_text1_section1 = page_info.services_text1_section1
    return render(request, 'services.html', locals())

def changeInfo(request):
    return_dict = {}
    print(request.POST)
    target = request.POST.get('target')
    data = request.POST.get('data')
    if target == 'about_text1_section1':
        page = Page.objects.get(id=1)
        page.about_text1_section1 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'about_text2_section1':
        page = Page.objects.get(id=1)
        page.about_text2_section1 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'about_text1_section2':
        page = Page.objects.get(id=1)
        page.about_text1_section2 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'contact_text1_section1':
        page = Page.objects.get(id=1)
        page.contact_text1_section1 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'contact_text1_section2':
        page = Page.objects.get(id=1)
        page.contact_text1_section2 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'services_text1_section1':
        page = Page.objects.get(id=1)
        page.services_text1_section1 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'

    return JsonResponse(return_dict)

def changeHeader(request):
    return_dict = {}
    print(request.POST)
    target = request.POST.get('target')
    data = request.POST.get('data')
    if target == 'about_header_section1':
        page = Page.objects.get(id=1)
        page.about_header_section1 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'about_header_section2':
        page = Page.objects.get(id=1)
        page.about_header_section2 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'about_header_section3':
        page = Page.objects.get(id=1)
        page.about_header_section3 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'contact_header_section1':
        page = Page.objects.get(id=1)
        page.contact_header_section1 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'contact_header_section2':
        page = Page.objects.get(id=1)
        page.contact_header_section2 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'service_header_section1':
        page = Page.objects.get(id=1)
        page.services_header_section1 = data
        page.save(force_update=True)
        return_dict['result'] = 'success'

    return JsonResponse(return_dict)

def saveSEO(request):
    return_dict = {}
    print(request.POST)
    target = request.POST.get('target')
    title = request.POST.get('title')
    description = request.POST.get('description')
    keywords = request.POST.get('keywords')
    if target == 'about':
        page = Page.objects.get(id=1)
        page.about_title = title
        page.about_description = description
        page.about_keywords = keywords
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'contacts':
        page = Page.objects.get(id=1)
        page.contact_title = title
        page.contact_description = description
        page.contact_keywords = keywords
        page.save(force_update=True)
        return_dict['result'] = 'success'
    elif target == 'service':
        page = Page.objects.get(id=1)
        page.services_item_title = title
        page.services_item_description = description
        page.services_item_keywords = keywords
        page.save(force_update=True)

        return_dict['result'] = 'success'

    return JsonResponse(return_dict)

def changeImg(request):

    return_dict = {}
    print(request.POST)
    target = request.POST.get('target')
    id = int(request.POST.get('id'))
    file = request.POST.get('file')

    if target == 'client':
        client_img = AboutPageClients.objects.get(id=id)
        form = AboutClientsForm(request.POST, request.FILES, instance=client_img)
        if form.is_valid():
            form.save()

        return_dict['result'] = 'success'
    elif target == 'work':
        work_img = AboutPageWork.objects.get(id=id)
        form = AboutWorkForm(request.POST, request.FILES, instance=work_img)
        if form.is_valid():
            form.save()

        return_dict['result'] = 'success'
    elif target == 'about_header_section3':
        page = Page.objects.get(id=1)
        page.about_header_section3 = ''
        page.save(force_update=True)
        return_dict['result'] = 'success'

    return JsonResponse(return_dict)

def saveServiceInfo(request):
    return_dict = {}
    print(request.POST)
    mode = request.POST.get('mode')
    header = request.POST.get('header')
    id = int(request.POST.get('id'))
    text = request.POST.get('text')

    if mode == 'update':
        service = Services.objects.get(id=id)
        service.header = header
        service.text = text
        service.save(force_update=True)
    if mode == 'new':
        Services.objects.create(header=header, text=text).save()


    return JsonResponse(return_dict)