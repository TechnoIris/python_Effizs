import requests
from bs4 import BeautifulSoup

URL="https://www.flipkart.com/nova-prime-series-nht-1085-runtime-45-min-trimmer-men/p/itmenaz5kbhceffm?gclid=CjwKCAiAluLvBRASEiwAAbX3GQNX3ebUtqmybVDGfJVV6uOPB0f8gfztPYRQn5uHSEngrq3njdt6vhoCfBgQAvD_BwE&pid=SHVENAZ5AQNMDGYA&lid=LSTSHVENAZ5AQNMDGYAKNSAM4&marketplace=FLIPKART&cmpid=content_trimmer_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,330072689017,1o2,,,c,,,,,,,&ef_id=CjwKCAiAluLvBRASEiwAAbX3GQNX3ebUtqmybVDGfJVV6uOPB0f8gfztPYRQn5uHSEngrq3njdt6vhoCfBgQAvD_BwE:G:s&s_kwcid=AL!739!3!330072689017!!!g!312958784358!"

headers= {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
page=requests.get(URL, headers=headers)
soup= BeautifulSoup(page.content, 'html.parser')
title=soup.find('div', class_="_1vC4OE _3qQ9m1").get_text()
print(title.strip())
#inspect the html file to find the id/class/variable in span element tag
