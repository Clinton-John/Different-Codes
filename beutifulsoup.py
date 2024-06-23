from bs4 import BeutifulSoup
import requests


url = ''

page = requests.get(url)

soup = BeutifulSoup(page.text, 'html')
print(soup) 