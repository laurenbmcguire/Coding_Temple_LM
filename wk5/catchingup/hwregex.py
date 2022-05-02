import re

file = open('./names.txt', encoding='utf-8')
data = file.read()
separated_string = data.splitlines()

for files in separated_string:
    name = re.search('.+?(?=\t)', files)
    name = re.search('.+?(?=\t)', files)
    list = {}
    if name:
        list["Name"] = (name.group())
    job = re.findall('/\t[\s\S]*/', files)
    if job:
      list["Job"] = (job[0])
    email = re.search('[\d\w\'-+.]*@[\w+]+[.com]+[.\w]{3}', files)
    if email:
      list["Email"] = (email.group())
    phone = re.search('\(?\d{3}\)?\s?-?\d{3}-\d{4}', files)
    if phone:
      list["Phone"] = (phone.group())
    twitter = re.search('@+[\w]+$', files)
    if twitter:
      list["Twitter"] = (twitter.group())
    print(list)


file.close()
