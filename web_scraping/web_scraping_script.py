from bs4 import BeautifulSoup

soup = BeautifulSoup(open("avclub.html"))
soup2 = BeautifulSoup(open("bruin.html"))

news_pane = soup2.find("div", class_="medium-8 columns section-left")
main_news = news_pane.find_all("div", class_="db-story-c1")
other_news = news_pane.find_all("div", class_="row db-list")

for header in main_news:
	h2_main = header.find("h2")
	h2_cool = h2_main.a
	print h2_cool.string.strip()

for header2 in other_news:
	h2_other = header2.find("h2")
	h2_cool2 = h2_other.a
	print h2_cool2.string.strip()

start_url = requests.get('http://dailybruin.com/category/news/')
soup3 = BeautifulSoup(start_url.content)
print start_url
