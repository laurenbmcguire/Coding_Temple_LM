
import requests 
import json

from collections import Counter
import datetime
import time

import itertools
from operator import *

url = 'https://ct-mock-tech-assessment.herokuapp.com/'

r = requests.get(url)

print(f"Status code: {r.status_code}")
#

response_dict = r.json()

repo_dicts = response_dict['partners']

repo_dict=repo_dicts[0]

class Person:
    def __init__(self,email,fname,lname,country,availability=[]):
        self.email = email 
        self.fname = fname
        self.lname = lname
        self.country = country
        self.availability = availability

    def get_email(self):
        email = f"{self.email}"
        return email
    
        

people =[]
for p in response_dict['partners']:
    person = Person(p['email'],p['firstName'],p['lastName'],p['country'],p['availableDates'])
    people.append(person)


countries=[]
for p in people:
    if p.country not in countries:
        countries.append(p.country)

print(countries)

   
meeting_dates = []

meets=[]
a=[]
meetings = {}
all_meetings = {}
for p in people:
    for c in countries:
        if p.country == c: 
            meetings[p.country]= meets
            
            m = {   
                'email': p.email, 
                'fname': p.fname,
                'lname': p.lname,
                'availability': p.availability
                }
            
            meets.append(m)
    
        a += p.availability
        all_meetings[c] = a


############### FIGURE OUT ########################################
dates=[]
# for k in all_meetings:
# for i in all_meetings:
for i in a:
    dates.append(int(datetime.datetime.strptime(i, '%Y-%m-%d').strftime('%Y%m%d')))
cleaned_dates = sorted(set(dates))
    
# print(all_meetings)
for k, g in itertools.groupby(enumerate(cleaned_dates), lambda ix: ix[0] - ix[1]):
    meeting_dates.append(list(map(itemgetter(1), g)))

print(meeting_dates)
#####################################################################

# print(len(meeting_dates))
        
        
        