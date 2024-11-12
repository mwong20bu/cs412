from django.db import models

# Create your models here.
class Result(models.Model):
    '''
    Store/represent the data from one runner at the Chicago Marathon 2023.
    BIB,First Name,Last Name,CTZ,City,State,Gender,Division,
    Place Overall,Place Gender,Place Division,Start TOD,Finish TOD,Finish,HALF1,HALF2
    '''
    # identification
    bib = models.IntegerField()
    first_name = models.TextField()
    last_name = models.TextField()
    ctz = models.TextField()
    city = models.TextField()
    state = models.TextField()
    # gender/division
    gender = models.CharField(max_length=6)
    division = models.CharField(max_length=6)
    # result place
    place_overall = models.IntegerField()
    place_gender = models.IntegerField()
    place_division = models.IntegerField()
    # timing-related
    start_time_of_day = models.TimeField()
    finish_time_of_day = models.TimeField()
    time_finish = models.TimeField()
    time_half1 = models.TimeField()
    time_half2 = models.TimeField()

    def __str__(self):
        '''Return a string representation of this model instance.'''
        return f'{self.first_name} {self.last_name} ({self.city}, {self.state}), {self.time_finish}'
    
    def get_runners_passed(self): 
        '''Return the number of runners who started before this Result and finished after.'''
        #filter for results who had an earlier start time
        start_first = Result.objects.filter(start_time_of_day__lt=self.start_time_of_day)
        #of those who started first, filter for those whose end times are later than self's
        passed = start_first.filter(finish_time_of_day__gt=self.finish_time_of_day)
        return len(passed)
    
    def get_runners_passed_by(self):
        '''Return the number of runners who started after this Result and finished earlier.'''
        #filter for results who had an earlier start time
        start_after = Result.objects.filter(start_time_of_day__gt=self.start_time_of_day)
        #of those who started first, filter for those whose end times are later than self's
        passed_by = start_after.filter(finish_time_of_day__lt=self.finish_time_of_day)
        return len(passed_by)

def load_data():
    '''Function to load data records from CSV file into Django model instances.'''

    #delete all records: this is so that duplicate old data is deleted -- only use if that's what you want
    Result.objects.all().delete()

    #then start opening file and reading lines
    filename = '2023_chicago_results.csv'
    f = open(filename)
    f.readline() # discard headers

    # to read a single line
    # line = f.readline().strip() #note: strip is needed because of newline char
    # fields = line.split(',')
    # print(fields)
    # for i in range(len(fields)):
    #   print(f'fields[{i}] = {fields[i]}')

    for line in f: 
        try: 
            fields = line.split(',')
                
        # create a new instance of Result object with this record from CSV
            result = Result(bib=fields[0],
                            first_name=fields[1],
                            last_name=fields[2],
                            ctz = fields[3],
                            city = fields[4],
                            state = fields[5],
                            
                            gender = fields[6],
                            division = fields[7],
                            place_overall = fields[8],
                            place_gender = fields[9],
                            place_division = fields[10],
                        
                            start_time_of_day = fields[11],
                            finish_time_of_day = fields[12],
                            time_finish = fields[13],
                            time_half1 = fields[14],
                            time_half2 = fields[15],
                        )
            print(f'Created result: {result}')
            result.save()
        
        except:
            print(f"Exception occurred: {fields}.")
    
    #After the loop
    print("done.")