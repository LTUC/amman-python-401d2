import requests
import pprint
from bs4 import BeautifulSoup


URL = "https://www.monster.com/jobs/search/?q=Python-Developer&where=San-Francisco__2C-CA"
response = requests.get(URL)

# pprint.pprint(response.content)


soup = BeautifulSoup(response.content, 'html.parser')


# print(soup)
# print('*'*50)
# print(dir(soup))

# Read all jobs
results = soup.find(id='SearchResults')
# print(results.prettify())

# Find all results with class card-content
all_jobs = results.find_all('section', class_='card-content')
# print(len(all_jobs))
# print(all_jobs[3])

final_result = []

for job in all_jobs:
    if not job.find('h2', class_='title'):
        continue

    title = job.find('h2', class_='title').text.strip()
    name = job.find('div', class_='company').text.strip()
    location = job.find('div', class_='location').text.strip()

    job_dict = {
                'title': title,
                'name': name,
                'location': location
               }

    final_result.append(job_dict)

    # print(f'Job Title: {title}')
    # print(f'Company Name: {name}')
    # print(f'Company Location: {location}')
    # print()
    # print(job_dict)


import json
json_object = json.dumps(final_result, indent=4)

with open('data.json', 'w') as f:
    f.write(json_object)

# print(final_result)
