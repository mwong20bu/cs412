from django.db import models

# Create your models here.
class Voter(models.Model):
    # identification
    voter_id = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    street_num = models.TextField()
    street_name = models.TextField()
    apt_num = models.TextField()
    zipcode = models.TextField()
    dob = models.DateField()
    date_of_registration = models.DateField()
    party = models.CharField(max_length=3)
    precinct_num = models.IntegerField()
    v20state = models.TextField()
    v21town = models.TextField()
    v21primary = models.TextField()
    v22general = models.TextField()
    v23town = models.TextField()
    voter_score = models.IntegerField()

    def __str__(self):
        '''Return a string representation of this model instance.'''
        return f'{self.first_name} {self.last_name} ({self.party}, {self.zipcode}, {self.dob})'

def load_data():
    '''Function to load data records from CSV file into Django model instances.'''

    #delete all records: this is so that duplicate old data is deleted -- only use if that's what you want
    Voter.objects.all().delete()

    #then start opening file and reading lines
    filename = 'newton_voters.csv'
    f = open(filename)
    headers = f.readline() # discard headers

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
            voter = Voter(voter_id=fields[0],
                            first_name=fields[2],
                            last_name=fields[1],
                            street_num = fields[3],
                            street_name = fields[4],
                            apt_num = fields[5],
                            zipcode = fields[6],
                            dob = fields[7],
                            date_of_registration = fields[8],
                            party = fields[9].strip(),
                            precinct_num = fields[10],
                            v20state = fields[11],
                            v21town = fields[12],
                            v21primary = fields[13],
                            v22general = fields[14],
                            v23town = fields[15],
                            voter_score = fields[16]
                        )
            print(f'Created voter: {voter}')
            voter.save()
        
        except:
            print(f"Exception occurred: {fields}.")
    
    #After the loop
    print(f'Done. Created {len(Voter.objects.all())} voters.')