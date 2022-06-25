# from urllib.request import Request, urlopen

# link = "http://google.com"
# link = "https://tracker.gg/valorant/profile/riot/dabqu%23dabqu/overview"
# req = Request(link)
# #url_response = urllib.request.urlopen(link)
# url_contents = urlopen(req).read()

# x = str(url_contents)


# print(x.index("Wins"))



import requests

from lxml import html
session = requests.Session()

from requests_html import HTMLSession
s = HTMLSession()
respoz = s.get("https://tracker.gg/valorant/profile/riot/dabqu%23dabqu/matches?playlist=competitive", timeout=(3.05, 27))
respoz.html.render(wait=2,sleep=6)
print(respoz)


# https://tracker.gg/valorant/profile/riot/dabqu%23dabqu/overview
link = "https://tracker.gg/valorant/profile/riot/dabqu%23dabqu/matches?playlist=competitive"
response = session.get(link, headers={'User-Agent': 'Mozilla/5.0'})

x = respoz.text
#print(x[x.index("Wins"):x.index("Wins")+1000])

tree = html.fromstring(x)

#print(tree.xpath('//div[@class="match match--lost"]/text()'))
#print(tree.xpath('//div[@class="label"]/text()'))
#print(tree.findall('.//div data-v-7c8e0719'))
#print([b.text for b in tree.iterfind('.//::before')])
#print(tree.findall('.//::before'))

el = tree.xpath(".//div[contains(@title-slug, 'valorant')]")[1].text_content() 
print(el)