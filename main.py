from indeed import extract_indeed_pages, extract_indeed_jobs
#from indeed import get_jobs as get_indeed_jobs
from so import extract_so_pages, extract_so_jobs
from save import save_to_file

last_indeed_page = extract_indeed_pages()
indeed_jobs = extract_indeed_jobs(last_indeed_page)
#print(indeed_jobs)
#indeed_jobs = get_indeed_jobs()

#so_jobs = get_so_jobs()

last_so_page = extract_so_pages()
so_jobs = extract_so_jobs(last_so_page)

#print(so_jobs)

jobs = so_jobs + indeed_jobs
save_to_file(jobs)