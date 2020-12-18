'''
Refreshes the master README.md file with the current calendar and
progress bar.

Author: Braedyn Lettinga
Dependencies: gitpython
'''

import git

from course_calendar import Calendar
from progress_bar import generate_bar_html

repo = git.Repo()
origin = repo.remote('origin')

readme_temp = open('.assets/README_TEMP.md', 'r').read()

### 🠗 CHANGE AS NECESSARY 🠗 ###
STARTING_DATE = '12/27/2020'  # (starting date must be a Sunday)
ENDING_DATE = '4/23/2021'

calendar = Calendar(STARTING_DATE, 16)

### 🠗 DO NOT CHANGE 🠗 ###
calendar_html = calendar.generate_calendar_html()
progress_bar_html = generate_bar_html(STARTING_DATE, ENDING_DATE)

readme_temp = readme_temp.replace('&progress&', progress_bar_html).replace('&calendar&', calendar_html)

readme = open('README.md', 'w+', encoding="utf-8")
print(readme_temp, file=readme)
readme.close()

changed_files = [ item.a_path for item in repo.index.diff(None) ]
repo.index.add(changed_files)

repo.index.commit('gitpython test commit')
origin.push()