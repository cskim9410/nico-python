import requests
from bs4 import BeautifulSoup



def extract_indeed_pages(): 
    start = 0
    URL = f"https://www.indeed.com/jobs?q=python&limit=50&start={start*50}"
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("ul", {"class":"pagination-list"})
    next_button = pagination.find("a", {"aria-label":"Next"})
    
    while next_button:
        URL_last = f"https://www.indeed.com/jobs?q=python&limit=50&start={start*50}"
        result_last = requests.get(URL_last)
        soup_last = BeautifulSoup(result_last.text, "html.parser")
        pagination_last = soup_last.find("ul", {"class":"pagination-list"})
        next_button_last = pagination_last.find("a", {"aria-label":"Next"})
        start = start +1
        print(URL_last)
        print(start)
        if next_button_last == None:
            return start
        
def extract_indeed_jobs(last_page):
    for page in range(last_page):
       result = requests.get(f"https://www.indeed.com/jobs?as_and=python&limit=50&start={page*50}")
       soup = BeautifulSoup(result.text, "html.parser")
       results = soup.find_all("a", {"data-mobtk":"1fop9lsjcosn1800"})
       print(result.status_code)