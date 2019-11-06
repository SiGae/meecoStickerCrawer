from bs4 import BeautifulSoup
import re
import requests
import urllib.request

stickerId = input("스티커의 id를 입력하세요 : ")
req = requests.get('https://meeco.kr/index.php?mid=sticker&sticker_srl={}'.format(stickerId))
html = req.text

soup = BeautifulSoup(html, 'html.parser')
stic = soup.find_all("div", {"class":re.compile("stk_img_v stk_file.")})
output = []
a = 1
length = len(stic)
for i in stic:
    forma = "jpg"
    part = i.get('style').replace("background-image: url(.", "").replace(");", "")
    if ".gif" in part:
        forma = "gif"

    urllib.request.urlretrieve("https://meeco.kr{}".format(part), "{}.{}".format( str(a), forma))
    print("{}/{}".format(a, length))
    int(a)
    a += 1
    