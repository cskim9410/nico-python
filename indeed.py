import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"
URL_LAST = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}&start=9999"

def get_last_page():
    result = requests.get(URL_LAST)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("ul", {"class":"pagination-list"})

    links = pagination.find_all('a')
    pages = []
    links= links[1:]

    for link in links:
        pages.append(int(link.string))
    max_page = pages[-1]+1
    return max_page

# indeed 홈페이지가 변경되어 다음버튼이 있는 동안 URL을 리퀘스트 하여 마지막 페이지를 찾았다, 하지만 리퀘스트를 다시 하기 때문에 속도가 너무 느려져서 start=9999 로 줘서 해결했다.
# def extract_indeed_pages(): 
#     start = 0
#     URL = f"https://www.indeed.com/jobs?q=python&limit=50&start={start*50}"
#     result = requests.get(URL)
#     soup = BeautifulSoup(result.text, "html.parser")
#     pagination = soup.find("ul", {"class":"pagination-list"})
    # next_button = pagination.find("a", {"aria-label":"Next"})
    # while next_button:
    #     URL_last = f"https://www.indeed.com/jobs?q=python&limit=50&start={start*50}"
    #     result_last = requests.get(URL_last)
    #     soup_last = BeautifulSoup(result_last.text, "html.parser")
    #     pagination_last = soup_last.find("ul", {"class":"pagination-list"})
    #     next_button_last = pagination_last.find("a", {"aria-label":"Next"})
    #     start = start +1
    #     print(URL_last)
    #     print(start)
    #     if next_button_last == None:
    #         return start
        
def extract_job(html):
    title = html.find("h2",{"class":"jobTitle"}).find('span', title=True).string
    company = html.find('span',{'class':'companyName'}).string
    location = html.find('div', {'class':'companyLocation'}).text
    job_id = html["data-jk"]
    return {'title':title, 'company':company, 'location':location, 'link':f'https://www.indeed.com/viewjob?jk={job_id}'}
        
def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Scrapping Indeed: Page {page+1}')
        result = requests.get(f"https://www.indeed.com/jobs?q=python&limit=50&start={page*50}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("a", {"class":"fs-unmask"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs
            
def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
