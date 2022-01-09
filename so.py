import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs"


def get_last_page():
    result = requests.get(URL,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div',{'class':'s-pagination'})
    pages = pagination.find_all('a',{'class':'s-pagination--item'})
    pages = pages[:-1]
    last_page = pages[-1].get_text(strip = True)
    return int(last_page)

def extract_job(html):
    title = html.find("a",{"class":"s-link"})['title']
    company = html.find('h3',{'class':'fc-black-700'}).find('span').get_text(strip = True)
    location = html.find('h3',{'class':'fc-black-700'}).find('span', {'class':'fc-black-500'}).get_text(strip = True)
    job_id = html['data-jobid']
    return {'title':title, 'company':company, 'location':location, 'link':f'https://stackoverflow.com/jobs/{job_id}'}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Scrapping SO: Page {page+1}')
        result = requests.get(f'{URL}?pg={page+1}', headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class':'-job'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return(jobs)
    

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs