from bs4 import BeautifulSoup
import urllib2
from urllib2 import urlopen
import requests

#created function for analyzing each link
def new_soup(url):
	link_url = urlopen(url).read()
	return BeautifulSoup(link_url)

start_url = urllib2.urlopen('http://dailybruin.com/category/news/') #goes online to request the page
base_url = 'http://dailybruin.com' #this is the formula to concantenate the category link later on
soup2 = BeautifulSoup(start_url) #analyze soup

news_pane = soup2.find("div", class_="medium-8 columns section-left") #entire news pane
#this is specifically for #1 article since it is different than the others
main_news = soup2.find_all("div", class_="db-story-c1")
#this is for the rest of the titles on the page
other_news = soup2.find_all("div", class_="row db-list")

#this for loop is specifically for the top article
for header in main_news:
	h2_main = header.find("h2") #finding the header
	h2_final = h2_main.a 
	print h2_final.string.strip() #only retrieving the title

#this for loop is for the rest of the articles on taht page
for header2 in other_news:
	h2_other = header2.find("h2")
	h2_other_final = h2_other.a
	print h2_other_final.string.strip()

print "\n" #creating a new line to seperate the two problems given to me

#this for loop is specifically for the top article
for header_link in main_news:
	h2_main_link = header_link.find("h2") #finding the header
	h2_main_link_title = h2_main.a
	main_category_link = h2_main_link_title.get("href")
	requesting_main_link = base_url + main_category_link

for header2_link in other_news:
	h2_other = header2_link.find("h2") #finding the header
	h2_cool2 = h2_other.a #title
	category_link = h2_cool2.get("href") #getting the title links
#combination of the base url at the top and the category link since they do not provide the link for me
	requesting_link = base_url + category_link 
	print requesting_link

#was not able to get the link and analyze number of paragraphs, I kept 
#getting a string buffer error
#souping the url for analyzing of paragraphs	
	analyzing_soup = new_soup(requesting_link)
	other_news_link = analyzing_soup.find("div", class_="db-post-content")
	for paragraph in other_news_link:
		paragraph_beta = paragraph.find('p')
#		print paragraph_beta
#	print paragraph_beta.strip() + requesting_link

