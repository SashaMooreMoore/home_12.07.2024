from django.shortcuts import render
from django.views import View

class PageSession(View):
    def get(self, request):
        return render(request, 'appSessions/index.html')

    def post(self, request):
        # print(request.POST['csrfmiddlewaretoken'])
        # print(request.POST['first_name'])
        # print(request.POST['date'])
        # print(request.POST['range'])
        
        product = request.POST['product']
        cart = request.session.get('cart', {})
        if not cart:
            request.session['cart'] = {}
        
        cart[product] = cart.get(product, 0) + 1
        
        request.session['cart'] = cart
        
        print(request.session.__dict__)
        return render(request, 'appSessions/index.html')
        