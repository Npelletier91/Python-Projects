import requests
from bs4 import BeautifulSoup

url = "https://www.learncodinganywhere.com/codingbootcamps/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

title_element = soup.find('title')
print("The title is: ", title_element)

footer_element = soup.find('footer')
print(footer_element)




