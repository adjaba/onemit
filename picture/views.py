from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic.list import ListView

import operator

from django.db.models import Q
from .models import Entry
from functools import reduce


def index(request):
    # return HttpResponse("Hello, world. You're at the pictures index. You should be seeing a picture")
    return render(request, 'base.html')

import pandas as pd
import numpy as np

def search(names):
    df = pd.read_csv('./picture/HACKmerged.csv', encoding = "ISO-8859-1")
    df2 = pd.read_csv('./picture/pixmerged.csv', encoding = "ISO-8859-1")
    dicty={}
    dicty[0] = ()
    counter = 0
    for i in names:
        i = i.upper()
        samebox = df.loc[df['name'] == i, 'boxNumber'].tolist()
        sameline = df.loc[df['name'] == i, 'lineNumber'].tolist()
        dicty[counter] = set(list(zip(samebox, sameline)))
        counter+=1

    ans = dicty[0].intersection(*dicty.values())

        
    return (list(ans)[0])

class ResultListView(ListView):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 10
    model= Entry
    template_name='result_list.html'

    def get_queryset(self):
        # result = super(ResultListView, self).get_queryset()
        result= Entry.objects.all()
        # print(result.count())

        query = self.request.GET.get('q')
        # result_list=[]
        # box_line_list=[]
        if query:
            query_list = query.split()
            return search(query_list)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['queryset'] = self.get_queryset()
        mapping = {}
        i = 0
        for y in range(15):
            for x in range(9):
                mapping[i] = str(i) + '.png'
                i += 1
        context['first']= context['queryset']
        context['image_name']= mapping[int(context['queryset'][0])]
        listy=['one/Screen Shot 2018-09-15 at 1.08.04 PM.png', 'one/Screen Shot 2018-09-15 at 1.08.56 PM.png', 'one/Screen Shot 2018-09-15 at 1.09.28 PM.png', 'one/Screen Shot 2018-09-15 at 1.11.19 PM.png', 'one/Screen Shot 2018-09-15 at 1.11.46 PM.png', 'one/Screen Shot 2018-09-15 at 1.12.43 PM.png', 'one/Screen Shot 2018-09-15 at 1.13.15 PM.png', 'one/Screen Shot 2018-09-15 at 1.13.38 PM.png', 'one/Screen Shot 2018-09-15 at 1.13.55 PM.png', 'two/Screen Shot 2018-09-15 at 1.16.49 PM.png', 'two/Screen Shot 2018-09-15 at 1.17.36 PM.png', 'two/Screen Shot 2018-09-15 at 1.18.02 PM.png', 'two/Screen Shot 2018-09-15 at 1.18.26 PM.png', 'two/Screen Shot 2018-09-15 at 1.18.47 PM.png', 'two/Screen Shot 2018-09-15 at 1.31.42 PM.png', 'two/Screen Shot 2018-09-15 at 1.32.27 PM.png', 'two/Screen Shot 2018-09-15 at 1.33.20 PM.png', 'two/Screen Shot 2018-09-15 at 1.33.50 PM.png', 'three/Screen Shot 2018-09-15 at 1.47.25 PM.png', 'three/Screen Shot 2018-09-15 at 1.47.51 PM.png', 'three/Screen Shot 2018-09-15 at 1.48.43 PM.png', 'three/Screen Shot 2018-09-15 at 1.49.19 PM.png', 'three/Screen Shot 2018-09-15 at 1.49.41 PM.png', 'three/Screen Shot 2018-09-15 at 1.50.44 PM.png', 'three/Screen Shot 2018-09-15 at 1.51.07 PM.png', 'three/Screen Shot 2018-09-15 at 1.51.32 PM.png', 'three/Screen Shot 2018-09-15 at 1.51.54 PM.png', 'four/Screen Shot 2018-09-15 at 1.53.16 PM.png', 'four/Screen Shot 2018-09-15 at 1.53.54 PM.png', 'four/Screen Shot 2018-09-15 at 1.54.16 PM.png', 'four/Screen Shot 2018-09-15 at 1.54.55 PM.png', 'four/Screen Shot 2018-09-15 at 1.55.40 PM.png', 'four/Screen Shot 2018-09-15 at 1.56.09 PM.png', 'four/Screen Shot 2018-09-15 at 1.56.38 PM.png', 'four/Screen Shot 2018-09-15 at 1.56.58 PM.png', 'four/Screen Shot 2018-09-15 at 1.57.16 PM.png', 'five/Screen Shot 2018-09-15 at 2.00.09 PM.png', 'five/Screen Shot 2018-09-15 at 2.01.34 PM.png', 'five/Screen Shot 2018-09-15 at 2.03.16 PM.png', 'five/Screen Shot 2018-09-15 at 2.03.46 PM.png', 'five/Screen Shot 2018-09-15 at 2.04.25 PM.png', 'five/Screen Shot 2018-09-15 at 2.05.03 PM.png', 'five/Screen Shot 2018-09-15 at 2.07.09 PM.png', 'five/Screen Shot 2018-09-15 at 2.07.39 PM.png', 'five/Screen Shot 2018-09-15 at 2.08.01 PM.png', 'six/Screen Shot 2018-09-15 at 2.11.21 PM.png', 'six/Screen Shot 2018-09-15 at 2.12.15 PM.png', 'six/Screen Shot 2018-09-15 at 2.12.43 PM.png', 'six/Screen Shot 2018-09-15 at 2.13.09 PM.png', 'six/Screen Shot 2018-09-15 at 2.13.39 PM.png', 'six/Screen Shot 2018-09-15 at 2.14.17 PM.png', 'six/Screen Shot 2018-09-15 at 2.14.40 PM.png', 'six/Screen Shot 2018-09-15 at 2.15.04 PM.png', 'six/Screen Shot 2018-09-15 at 2.15.20 PM.png', 'seven/Screen Shot 2018-09-15 at 2.27.57 PM.png', 'seven/Screen Shot 2018-09-15 at 2.28.21 PM.png', 'seven/Screen Shot 2018-09-15 at 2.28.55 PM.png', 'seven/Screen Shot 2018-09-15 at 2.29.25 PM.png', 'seven/Screen Shot 2018-09-15 at 2.29.49 PM.png', 'seven/Screen Shot 2018-09-15 at 2.30.13 PM.png', 'seven/Screen Shot 2018-09-15 at 2.30.38 PM.png', 'seven/Screen Shot 2018-09-15 at 2.30.59 PM.png', 'seven/Screen Shot 2018-09-15 at 2.31.13 PM.png', 'eight/Screen Shot 2018-09-15 at 2.32.24 PM.png', 'eight/Screen Shot 2018-09-15 at 2.33.04 PM.png', 'eight/Screen Shot 2018-09-15 at 2.33.22 PM.png', 'eight/Screen Shot 2018-09-15 at 2.33.51 PM.png', 'eight/Screen Shot 2018-09-15 at 2.34.12 PM.png', 'eight/Screen Shot 2018-09-15 at 2.34.39 PM.png', 'eight/Screen Shot 2018-09-15 at 2.35.03 PM.png', 'eight/Screen Shot 2018-09-15 at 2.35.55 PM.png', 'eight/Screen Shot 2018-09-15 at 2.36.08 PM.png', 'nine/Screen Shot 2018-09-15 at 2.37.44 PM.png', 'nine/Screen Shot 2018-09-15 at 2.38.11 PM.png', 'nine/Screen Shot 2018-09-15 at 2.38.33 PM.png', 'nine/Screen Shot 2018-09-15 at 2.38.50 PM.png', 'nine/Screen Shot 2018-09-15 at 2.39.11 PM.png', 'nine/Screen Shot 2018-09-15 at 2.39.41 PM.png', 'nine/Screen Shot 2018-09-15 at 2.40.03 PM.png', 'nine/Screen Shot 2018-09-15 at 2.40.28 PM.png', 'nine/Screen Shot 2018-09-15 at 2.40.42 PM.png', 'ten/Screen Shot 2018-09-15 at 2.41.48 PM.png', 'ten/Screen Shot 2018-09-15 at 2.42.14 PM.png', 'ten/Screen Shot 2018-09-15 at 2.43.56 PM.png', 'ten/Screen Shot 2018-09-15 at 2.44.18 PM.png', 'ten/Screen Shot 2018-09-15 at 2.44.37 PM.png', 'ten/Screen Shot 2018-09-15 at 2.44.58 PM.png', 'ten/Screen Shot 2018-09-15 at 2.45.13 PM.png', 'ten/Screen Shot 2018-09-15 at 2.45.29 PM.png', 'ten/Screen Shot 2018-09-15 at 2.45.42 PM.png', 'eleven/Screen Shot 2018-09-15 at 2.46.51 PM.png', 'eleven/Screen Shot 2018-09-15 at 2.47.21 PM.png', 'eleven/Screen Shot 2018-09-15 at 2.47.46 PM.png', 'eleven/Screen Shot 2018-09-15 at 2.48.03 PM.png', 'eleven/Screen Shot 2018-09-15 at 2.48.23 PM.png', 'eleven/Screen Shot 2018-09-15 at 2.48.48 PM.png', 'eleven/Screen Shot 2018-09-15 at 2.49.09 PM.png', 'eleven/Screen Shot 2018-09-15 at 2.49.32 PM.png', 'eleven/Screen Shot 2018-09-15 at 2.49.48 PM.png', 'twelve/Screen Shot 2018-09-15 at 2.50.48 PM.png', 'twelve/Screen Shot 2018-09-15 at 2.51.12 PM.png', 'twelve/Screen Shot 2018-09-15 at 2.51.32 PM.png', 'twelve/Screen Shot 2018-09-15 at 2.51.53 PM.png', 'twelve/Screen Shot 2018-09-15 at 2.52.10 PM.png', 'twelve/Screen Shot 2018-09-15 at 2.52.30 PM.png', 'twelve/Screen Shot 2018-09-15 at 2.52.51 PM.png', 'twelve/Screen Shot 2018-09-15 at 2.53.13 PM.png', 'twelve/Screen Shot 2018-09-15 at 2.53.27 PM.png', 'thirteen/Screen Shot 2018-09-15 at 3.06.09 PM.png', 'thirteen/Screen Shot 2018-09-15 at 3.06.46 PM.png', 'thirteen/Screen Shot 2018-09-15 at 3.07.14 PM.png', 'thirteen/Screen Shot 2018-09-15 at 3.08.24 PM.png', 'thirteen/Screen Shot 2018-09-15 at 3.08.49 PM.png', 'thirteen/Screen Shot 2018-09-15 at 3.09.10 PM.png', 'thirteen/Screen Shot 2018-09-15 at 3.09.35 PM.png', 'thirteen/Screen Shot 2018-09-15 at 3.09.57 PM.png', 'thirteen/Screen Shot 2018-09-15 at 3.10.17 PM.png', 'forteen/Screen Shot 2018-09-15 at 3.11.46 PM.png', 'forteen/Screen Shot 2018-09-15 at 3.12.09 PM.png', 'forteen/Screen Shot 2018-09-15 at 3.12.46 PM.png', 'forteen/Screen Shot 2018-09-15 at 3.13.07 PM.png', 'forteen/Screen Shot 2018-09-15 at 3.13.25 PM.png', 'forteen/Screen Shot 2018-09-15 at 3.14.07 PM.png', 'forteen/Screen Shot 2018-09-15 at 3.14.25 PM.png', 'forteen/Screen Shot 2018-09-15 at 3.14.49 PM.png', 'forteen/Screen Shot 2018-09-15 at 3.15.04 PM.png', 'fifteen/Screen Shot 2018-09-15 at 3.17.00 PM.png', 'fifteen/Screen Shot 2018-09-15 at 3.17.30 PM.png', 'fifteen/Screen Shot 2018-09-15 at 3.17.45 PM.png', 'fifteen/Screen Shot 2018-09-15 at 3.18.14 PM.png', 'fifteen/Screen Shot 2018-09-15 at 3.18.36 PM.png', 'fifteen/Screen Shot 2018-09-15 at 3.20.23 PM.png', 'fifteen/Screen Shot 2018-09-15 at 3.20.46 PM.png', 'fifteen/Screen Shot 2018-09-15 at 3.21.10 PM.png', 'fifteen/Screen Shot 2018-09-15 at 3.21.23 PM.png']
        context['text_name']= listy[int(context['queryset'][0])]
        return context

