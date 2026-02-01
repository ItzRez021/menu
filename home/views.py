from django.shortcuts import render,get_object_or_404
from django.views import View
from django.conf import settings
from .models import Food_And_Drinks,Category

# Create your views here.

class HomePage(View):
    template_name = 'home/start.html'
    def get(self,request):
        return render(request,self.template_name,{'MU':settings.MEDIA_URL})
    

class MenuPage(View):
    template_name = 'home/menu.html'
    def get(self,request):
        CAT = Category.objects.all().order_by('-id')
        FAD = Food_And_Drinks.objects.all()
        return render(request,self.template_name,{'MU':settings.MEDIA_URL,'CAT':CAT,'FAD':FAD})
    
class MenuFilteredPage(View):
    template_name = 'home/menu.html'
    def get(self,request,*args,**kwargs):
        cat_pk = kwargs['pk']
        cat  = get_object_or_404(Category,pk=cat_pk)
        CAT = Category.objects.all().order_by('-id')
        FAD = Food_And_Drinks.objects.filter(category=cat)
        return render(request,self.template_name,{'MU':settings.MEDIA_URL,'CAT':CAT,'FAD':FAD,'cat_pk':cat_pk})