from django.shortcuts import render
from django.http import HttpResponse
from .forms import FakeDataForm
from datetime import datetime,timedelta
from faker import Faker

import string
import random

import csv

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FakeDataForm(request.POST)
        if form.is_valid():
            fieldnames = form.cleaned_data.get('fieldnames')
            ranges = form.cleaned_data.get('ranges')
            datatypes = form.cleaned_data.get('datatypes')
            ## Actual Code ##
            field_names = list(map(str, fieldnames.split(" ")))
            n_f=len(field_names)
            m=[]
            # print(field_names)
            ranges = list(map(str, ranges.split(" ")))
            # print(ranges)
            datatypes = list(map(str, datatypes.split(" ")))
            # print(datatypes)
            for k in range(n_f):
                l2=[]
                l2.append(ranges[2*k])
                l2.append(ranges[2*k+1])
                m.append(l2)
            #### CSV Starts ###
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="fakedata.csv"'

            writer = csv.writer(response)
            writer.writerow(field_names)
             
            for i in range(10):
                row=[]
                for j in range(n_f):
                    if datatypes[j]=="i":
                        x=random.randint(int(m[j][0]),int(m[j][1]))
                        row.append(x)
                    elif datatypes[j]=="c":
                        x=""
                        x=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase) for _ in range(random.randint(int(m[j][0]),int(m[j][1]))))
                        row.append(x)
                    elif datatypes[j]=="d":
                        date_format = "%d/%m/%Y"
                        d1=datetime.strptime(m[j][0],date_format)
                        d2=datetime.strptime(m[j][1],date_format)
                        delta=d2-d1
                        f=random.randint(1,(abs(delta.days)))
                        x=(d1+timedelta(days=int(f)))
                        row.append(x)
                    elif datatypes[j]=="n":
                        fake = Faker()
                        x=fake.name()
                        row.append(x)
                    elif datatypes[j]=="e":
                        fake=Faker()
                        x=fake.email()
                        row.append(x)    

                writer.writerow(row)
            return response
    else:
        form = FakeDataForm()
    return render(request, 'index.html', {'form': form})
