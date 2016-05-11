# -*-coding:utf8
import urllib
import bs4
import urlparse

url = "http://photo.naver.com/camera/"

# website에서 정보를 가져옴
website = urllib.urlopen(url)
text = website.read()
website.close()

#가져 온 정보를 해석함
soup = bs4.BeautifulSoup(text, 'lxml')

#해석한 정보에서 img 포함된 내용을 추출함
imgs = soup.find_all('img')

#추출한 내용을 하나씩 살펴 봄
for image_info in imgs:
    imgae_url = image_info.get('src') # 각 image_info의 인터넷 주소 url 을 추출함