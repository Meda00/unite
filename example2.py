import requests
from bs4 import BeautifulSoup

content = requests.get('https://www.zhihu.com/question/293095043/answer/674732071/').content
soup = BeautifulSoup(content, 'html.parser')

for div in soup.find_all('div', {'class':'Banner-link'}):
    print div.text.strip()