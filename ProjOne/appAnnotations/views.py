from django.shortcuts import render
from django.views import View
from .models import Info, Bank
from django.db.models.functions import Length
from django.db.models import F


class PageHome(View):
    def get(self, request):
        data = []
        infos = Info.objects.all()
        for info in infos:
            # if info.title != None:
            # if info.title != '':
            if info.title:
                data.append(info)
        print(data)
        
        print(Info.objects.exclude(title=None))
        return render(request, 'appAnnotations/home.html')



class PageTestAnnotations(View):
    def get(self, request):
        # for info in Info.objects.exclude(title=None):
        #     print(len(info.title))
        
        objects_infos = Info.objects.exclude(title=None).annotate(
            title_len=Length('title')
        )
        for info in objects_infos:
            print(info.title_len)
        
        # operations_infos = Info.objects.annotate(
        #     result = F('balance') + 500
        # )
        operations_infos = Info.objects.annotate(
            result = F('balance') + F('balance_two')
        )
        for opt in operations_infos:
            print(opt.result)
        return render(request, 'appAnnotations/test_annot.html')
    

class PageBank(View):
    def get(self, request):
        object_bank = Bank.objects.annotate(
            result=F('balance')*F('percent')/100/365*30
        )
        for i in object_bank:
            print(i.result, i.balance)
        
        # print(request.session['age'])
        print(request.session.__dict__)
        request.session['age'] = 10
        
        return render(request, 'appAnnotations/bank.html', {
            'banks': object_bank
        })
        