from indeed import get_jobs as get_indeed_jobs, get_last_page
from so import get_jobs as get_so_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
jobs = so_jobs + indeed_jobs
save_to_file(jobs)

