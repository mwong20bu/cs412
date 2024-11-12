from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Voter
import plotly
import plotly.graph_objects as go 

# Create your views here.
class VotersListView(ListView):
    '''View to display list of voters'''
    template_name = "voter_analytics/voters.html"
    model = Voter
    context_object_name = "voters"
    paginate_by = 100

    def get_queryset(self):
        '''Return the set of Results '''

        #use the superclass version of the queryset
        qs = super().get_queryset()

        #with pagination is being used, don't need to break into subsets
        #return qs

        #adding filter parameters
        if 'party' in self.request.GET:
            party = self.request.GET['party']
            if party: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(party__icontains=party)
        
        if 'min_dob' in self.request.GET:
            min_dob = self.request.GET['min_dob']
            if min_dob == "":
                qs = qs
            else: 
                min_dob = min_dob + "-01-01"
                qs = qs.filter(dob__gt=min_dob)

        if 'max_dob' in self.request.GET:
            max_dob = self.request.GET['max_dob']
            if max_dob == "":
                qs = qs
            else: 
                max_dob = max_dob + "-12-31"
                qs = qs.filter(dob__lt=max_dob)
        
        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET['voter_score']
            if voter_score == "":
                qs = qs
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(voter_score=voter_score)

        if 'v20state' in self.request.GET:
            v20state = self.request.GET['v20state']
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(v20state=v20state)

        if 'v21town' in self.request.GET:
            v21town = self.request.GET['v21town']
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(v21town=v21town)

        if 'v21primary' in self.request.GET:
            v21primary = self.request.GET['v21primary']
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(v21primary=v21primary)

        if 'v22general' in self.request.GET:
            v22general = self.request.GET['v22general']
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(v22general=v22general)

        if 'v23town' in self.request.GET:
            v23town = self.request.GET['v23town']
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(v23town=v23town)
        
        return qs

        #now that pagination is being used, don't need to break into subsets

class VoterDetailView(DetailView):
    '''A view to display detail information about a single Voter'''
    template_name = "voter_analytics/voter_detail.html"
    model = Voter
    context_object_name = "v"

    def get_context_data(self, **kwargs):
        '''Add some data to the context object, including graphs'''
        #storing result of superclass call 
        context = super().get_context_data(**kwargs)
        v = context['v']

        #getting number of people per party
        return context
    
class GraphListView(ListView):
    template_name = "voter_analytics/graphs.html"
    model = Voter
    context_object_name = "voters"

    def get_queryset(self):
        '''Return the set of Results '''

        #use the superclass version of the queryset
        qs = super().get_queryset()

        #with pagination is being used, don't need to break into subsets
        #return qs

        #adding filter parameters
        if 'party' in self.request.GET:
            party = self.request.GET['party']
            if party: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(party__icontains=party)
        
        if 'min_dob' in self.request.GET:
            min_dob = self.request.GET['min_dob']
            if min_dob == "":
                qs = qs
            else: 
                min_dob = min_dob + "-01-01"
            #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(dob__gt=min_dob)

        if 'max_dob' in self.request.GET:
            max_dob = self.request.GET['max_dob']
            if max_dob == "": 
                qs = qs
            else: 
                max_dob = max_dob + "-12-31"
             #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(dob__lt=max_dob)
        
        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET['voter_score']
            if voter_score == "":
                qs = qs
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(voter_score=voter_score)

        if 'v20state' in self.request.GET:
            v20state = self.request.GET['v20state']
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(v20state=v20state)

        if 'v21town' in self.request.GET:
            v21town = self.request.GET['v21town']
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(v21town=v21town)

        if 'v21primary' in self.request.GET:
            v21primary = self.request.GET['v21primary']
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(v21primary=v21primary)

        if 'v22general' in self.request.GET:
            v22general = self.request.GET['v22general']
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(v22general=v22general)

        if 'v23town' in self.request.GET:
            v23town = self.request.GET['v23town']
            if voter_score: #not an empty string -- there is a party (to avoid returning all results)
                qs = qs.filter(v23town=v23town)
        return qs
    
    def get_context_data(self, **kwargs):
        '''Add some data to the context object, including graphs'''
        #storing result of superclass call 
        context = super().get_context_data(**kwargs)

        qs = context['voters']

        #building date of birth bar graph
        y1913 = len(qs.filter(dob__icontains="1913"))
        y1914 = len(qs.filter(dob__icontains="1914"))
        y1915 = len(qs.filter(dob__icontains="1915"))
        y1916 = len(qs.filter(dob__icontains="1916"))
        y1917 = len(qs.filter(dob__icontains="1917"))
        y1918 = len(qs.filter(dob__icontains="1918"))
        y1919 = len(qs.filter(dob__icontains="1919"))
        y1920 = len(qs.filter(dob__icontains="1920"))
        y1921 = len(qs.filter(dob__icontains="1921"))
        y1922 = len(qs.filter(dob__icontains="1922"))
        y1923 = len(qs.filter(dob__icontains="1923"))
        y1924 = len(qs.filter(dob__icontains="1924"))
        y1925 = len(qs.filter(dob__icontains="1925"))
        y1926 = len(qs.filter(dob__icontains="1926"))
        y1927 = len(qs.filter(dob__icontains="1927"))
        y1928 = len(qs.filter(dob__icontains="1928"))
        y1929 = len(qs.filter(dob__icontains="1929"))
        y1930 = len(qs.filter(dob__icontains="1930"))
        y1931 = len(qs.filter(dob__icontains="1931"))
        y1932 = len(qs.filter(dob__icontains="1932"))
        y1933 = len(qs.filter(dob__icontains="1933"))
        y1934 = len(qs.filter(dob__icontains="1934"))
        y1935 = len(qs.filter(dob__icontains="1935"))
        y1936 = len(qs.filter(dob__icontains="1936"))
        y1937 = len(qs.filter(dob__icontains="1937"))
        y1938 = len(qs.filter(dob__icontains="1938"))
        y1939 = len(qs.filter(dob__icontains="1939"))
        y1940 = len(qs.filter(dob__icontains="1940"))
        y1941 = len(qs.filter(dob__icontains="1941"))
        y1942 = len(qs.filter(dob__icontains="1942"))
        y1943 = len(qs.filter(dob__icontains="1943"))
        y1944 = len(qs.filter(dob__icontains="1944"))
        y1945 = len(qs.filter(dob__icontains="1945"))
        y1946 = len(qs.filter(dob__icontains="1946"))
        y1947 = len(qs.filter(dob__icontains="1947"))
        y1948 = len(qs.filter(dob__icontains="1948"))
        y1949 = len(qs.filter(dob__icontains="1949"))
        y1950 = len(qs.filter(dob__icontains="1950"))
        y1951 = len(qs.filter(dob__icontains="1951"))
        y1952 = len(qs.filter(dob__icontains="1952"))
        y1953 = len(qs.filter(dob__icontains="1953"))
        y1954 = len(qs.filter(dob__icontains="1954"))
        y1955 = len(qs.filter(dob__icontains="1955"))
        y1956 = len(qs.filter(dob__icontains="1956"))
        y1957 = len(qs.filter(dob__icontains="1957"))
        y1958 = len(qs.filter(dob__icontains="1958"))
        y1959 = len(qs.filter(dob__icontains="1959"))
        y1960 = len(qs.filter(dob__icontains="1960"))
        y1961 = len(qs.filter(dob__icontains="1961"))
        y1962 = len(qs.filter(dob__icontains="1962"))
        y1963 = len(qs.filter(dob__icontains="1963"))
        y1964 = len(qs.filter(dob__icontains="1964"))
        y1965 = len(qs.filter(dob__icontains="1965"))
        y1966 = len(qs.filter(dob__icontains="1966"))
        y1967 = len(qs.filter(dob__icontains="1967"))
        y1968 = len(qs.filter(dob__icontains="1968"))
        y1969 = len(qs.filter(dob__icontains="1969"))
        y1970 = len(qs.filter(dob__icontains="1970"))
        y1971 = len(qs.filter(dob__icontains="1971"))
        y1972 = len(qs.filter(dob__icontains="1972"))
        y1973 = len(qs.filter(dob__icontains="1973"))
        y1974 = len(qs.filter(dob__icontains="1974"))
        y1975 = len(qs.filter(dob__icontains="1975"))
        y1976 = len(qs.filter(dob__icontains="1976"))
        y1977 = len(qs.filter(dob__icontains="1977"))
        y1978 = len(qs.filter(dob__icontains="1978"))
        y1979 = len(qs.filter(dob__icontains="1979"))
        y1980 = len(qs.filter(dob__icontains="1980"))
        y1981 = len(qs.filter(dob__icontains="1981"))
        y1982 = len(qs.filter(dob__icontains="1982"))
        y1983 = len(qs.filter(dob__icontains="1983"))
        y1984 = len(qs.filter(dob__icontains="1984"))
        y1985 = len(qs.filter(dob__icontains="1985"))
        y1986 = len(qs.filter(dob__icontains="1986"))
        y1987 = len(qs.filter(dob__icontains="1987"))
        y1988 = len(qs.filter(dob__icontains="1988"))
        y1989 = len(qs.filter(dob__icontains="1989"))
        y1990 = len(qs.filter(dob__icontains="1990"))
        y1991 = len(qs.filter(dob__icontains="1991"))
        y1992 = len(qs.filter(dob__icontains="1992"))
        y1993 = len(qs.filter(dob__icontains="1993"))
        y1994 = len(qs.filter(dob__icontains="1994"))
        y1995 = len(qs.filter(dob__icontains="1995"))
        y1996 = len(qs.filter(dob__icontains="1996"))
        y1997 = len(qs.filter(dob__icontains="1997"))
        y1998 = len(qs.filter(dob__icontains="1998"))
        y1999 = len(qs.filter(dob__icontains="1999"))
        y2000 = len(qs.filter(dob__icontains="2000"))
        y2001 = len(qs.filter(dob__icontains="2001"))
        y2002 = len(qs.filter(dob__icontains="2002"))
        y2003 = len(qs.filter(dob__icontains="2003"))
        y2004 = len(qs.filter(dob__icontains="2004"))
        y2005 = len(qs.filter(dob__icontains="2005"))

        x = ["1913", "1914", "1915", "1916", "1917", "1918", "1919", "1920", "1921", "1922", "1923", 
             "1924", "1925", "1926", "1927", "1928", "1929", "1930", "1931", "1932", "1933", "1934", 
             "1935", "1936", "1937", "1938", "1939", "1940", "1941", "1942", "1943", "1944", "1945", 
             "1946", "1947", "1948", "1949", "1950", "1951", "1952", "1953", "1954", "1955", "1956", 
             "1957", "1958", "1959", "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967", 
             "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", 
             "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", 
             "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", 
             "2001", "2002", "2003", "2004", "2005"]
        y = [y1913, y1914, y1915, y1916, y1917, y1918, y1919, y1920, y1921, y1922, y1923, y1924, y1925, 
             y1926, y1927, y1928, y1929, y1930, y1931, y1932, y1933, y1934, y1935, y1936, y1937, y1938, 
             y1939, y1940, y1941, y1942, y1943, y1944, y1945, y1946, y1947, y1948, y1949, y1950, y1951, 
             y1952, y1953, y1954, y1955, y1956, y1957, y1958, y1959, y1960, y1961, y1962, y1963, y1964, 
             y1965, y1966, y1967, y1968, y1969, y1970, y1971, y1972, y1973, y1974, y1975, y1976, y1977, 
             y1978, y1979, y1980, y1981, y1982, y1983, y1984, y1985, y1986, y1987, y1988, y1989, y1990, 
             y1991, y1992, y1993, y1994, y1995, y1996, y1997, y1998, y1999, y2000, y2001, y2002, y2003, 
             y2004, y2005]

        fig = go.Bar(x=x, y=y)
        graph_dob_div = plotly.offline.plot({"data":[fig]}, auto_open=False, output_type="div")

        context['graph_dob_div'] = graph_dob_div
        

        #party pie chart
        u = len(qs.filter(party="U"))
        d = len(qs.filter(party="D"))
        r = len(qs.filter(party="R"))
        cc = len(qs.filter(party="CC"))
        l = len(qs.filter(party="L"))
        t = len(qs.filter(party="T"))
        o = len(qs.filter(party="O"))
        g = len(qs.filter(party="G"))
        j = len(qs.filter(party="J"))
        q = len(qs.filter(party="Q"))
        ff = len(qs.filter(party="FF"))

        x = ['U', 'D', 'R', 'CC', 'L', 'T', 'O', 'G', 'J', 'Q', 'FF']
        y = [u, d, r, cc, l, t, o, g, j, q, ff]

        fig = go.Pie(labels=x, values=y)
        graph_party_div = plotly.offline.plot({"data":[fig]}, auto_open=False, output_type="div")

        context['graph_party_div'] = graph_party_div

        #building a graph for showing past 5 election history
        v20state = len(qs.filter(v20state="TRUE"))
        v21town = len(qs.filter(v21town="TRUE"))
        v21primary = len(qs.filter(v21primary="TRUE"))
        v22general = len(qs.filter(v22general="TRUE"))
        v23town = len(qs.filter(v23town="TRUE"))

        x = ['2020 state', '2021 town', '2021 primary', '2022 general', '2023 town']
        y = [v20state, v21town, v21primary, v22general, v23town]

        fig = go.Bar(x=x, y=y)
        graph_voting_hist_div = plotly.offline.plot({"data":[fig]}, auto_open=False, output_type="div")

        context['graph_voting_hist_div'] = graph_voting_hist_div
        return context



