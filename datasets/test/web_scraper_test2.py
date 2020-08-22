from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

# url
baseUrl = 'https://www.google.com/searcher?q='
plusUrl = input("검색어 입력 :")
url = baseUrl + quote_plus(plusUrl)

# 브라우저 제어 (chromedriver.exe 경로 설정 필요)
driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html)

# print
r = soup.select('.r')
for i in r:
  print(i.select_one('.ellip').text)
  print(i.select_one('.iUh30.bc').text)
  print(i.a.attrs['href'])
  print()
driver.close()