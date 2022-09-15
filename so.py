import requests
from bs4 import BeautifulSoup

URL = f"http://stackoverflow.com/jobs/companies?q=python"

def extract_so_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  #print(soup)
  pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def extract_job(html):
  company_title = html.find("h2",{"class":"fs-body2"}).find("a",{"class":"s-link"}).string
  location, company = html.find("div",{"class":"fs-body1"}).find_all("div",{"class":"flex--item"})


  company_job = company.get_text()
  company_location = location.get_text()
  #print(title,company, location)
  return {"title":company_title, "company":company_job, "location":company_location, "apply_link": f"http://stackoverflow.com/jobs/companies/{company_title}"}
   
def extract_so_jobs(last_page):
  jobs=[]
  for page in range(last_page):
    print(f"Scrapping SO: Page {page}")
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div",{"class":"dismissable-company"})
    #print(result.status_code)
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs
    
#def get_jobs():
 # last_page = get_last_page()
  #jobs = extract_jobs(last_page)
  #return jobs