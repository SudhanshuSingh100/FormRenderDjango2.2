from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,HttpResponse

from .forms import UserForm
from .models import UserModel
# Create your views here.
from django.views.generic.edit import CreateView

#class IndexCreate(CreateView):
#    model = UserModel
#    fields = ['username', 'title', 'first_name', 'last_name',
#                  'mother_name', 'father_name','email_id',
#                  'secret_code',' address', 'date']

#def index_view(request):
 #   my_form = UserForm()
  #  context = {
   #     'form' : my_form
    #}
 #   return render(request, "index.html", context)
#
def index_view(request):
    # if this is a POST request we need to process the form data
    my_form = UserForm(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        my_form = UserForm(request.POST or None)
        # check whether it's valid:
        if my_form.is_valid():
            #now data is good
            # process the data in form.cleaned_data as required
            # ...
            UserModel.objects.create(**my_form.cleaned_data)


            # redirect to a new URL:
            return HttpResponseRedirect('/success/')
        my_form = UserModel.objects.all()

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'index.html', {'form': my_form})

# after updating it will redirect to detail_View
def detail_view(request):
    return render(request, "success.html")

