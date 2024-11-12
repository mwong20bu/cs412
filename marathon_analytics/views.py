from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Result
import plotly
import plotly.graph_objects as go 

# Create your views here.

class ResultsListView(ListView):
    '''View to display list of results'''
    template_name = "marathon_analytics/results.html"
    model = Result
    context_object_name = "results"
    paginate_by = 50

    def get_queryset(self):
        '''Return the set of Results '''

        #use the superclass version of the queryset
        qs = super().get_queryset()

        #arbitrarily returning a subset of it 
        #return qs[:25]

        #if we have a search parameter, use it to filter the queryset
        if 'city' in self.request.GET:
            city = self.request.GET['city']
            if city: #not an empty string -- there is a city (to avoid returning all results)
                qs = qs.filter(city__icontains=city)

        #now that pagination is being used, don't need to break into subsets
        return qs
    
class ResultDetailView(DetailView):
    '''View to show detail page for one result.'''
    template_name = 'marathon_analytics/result_detail.html'
    model = Result
    context_object_name = 'r'

    def get_context_data(self, **kwargs):
        '''Add some data to the context object, including graphs'''
        #storing result of superclass call 
        context = super().get_context_data(**kwargs)
        r = context['r']

        #building graph
        x = [f'Runners Passed by {r.first_name}', f'Runners who Passed {r.first_name}']
        y = [r.get_runners_passed(), r.get_runners_passed_by()]
        #print(f'x={x}')
        #print(f'y={y}')
        fig = go.Bar(x=x, y=y)
        graph_div = plotly.offline.plot({"data":[fig]}, auto_open=False, output_type="div")
        
        #adding graph to context data
        context['graph_div'] = graph_div

        #building pie chart of first half and second half 
        x = ['first half time', 'second half time']
        first_half_time_seconds = (r.time_half1.hour * 3600 + 
                                  r.time_half1.minute * 60 + 
                                  r.time_half1.second)
        
        second_half_time_seconds = (r.time_half2.hour * 3600 + 
                                  r.time_half2.minute * 60 + 
                                  r.time_half2.second)

        y = [first_half_time_seconds, second_half_time_seconds]
        #print(f'x={x}')
        #print(f'y={y}')
        fig = go.Pie(labels=x, values=y)
        pie_div = plotly.offline.plot({"data": [fig]}, auto_open = False, output_type="div")

        #adding the pie chart to context data
        context['pie_div'] = pie_div
        
        return context