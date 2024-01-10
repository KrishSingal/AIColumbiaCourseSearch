import csv
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup('', 'html.parser')
depts = soup.find_all(href=re.compile("Spring2024"))

with open()

for dept in depts:
    soup = BeautifulSoup(dept, 'html.parser') # need to get attr
    courses = soup.find_all(href=re.compile("/subj"))

    for course in courses:


