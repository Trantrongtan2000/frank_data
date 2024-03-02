from bs4 import BeautifulSoup
import requests

# Get the list of manuals from the website
url = "http://www.frankshospitalworkshop.com/equipment.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
t= []
for link in soup.find_all('a'):
  #print(str((link.get('href'))).find('equipment/'))
  if str((link.get('href'))).find('equipment/') == 0:
    t.append(link.get('href'))
    print(link.get('href'))

'''
# Find all links containing the word "manual" in their text
manuals = []
for link in soup.find_all('a', target="_blank"):
  manuals.append(link['href'])
  #print(link['href'])
#http://www.frankshospitalworkshop.com/equipment/documents/dialysis_units/user_manuals/B.Braun%20Dialog+%20Dialysis%20Machine%20-%20User%20manual.pdf
# Download the manuals
for manual_url in manuals:
  print(manual_url)
  filename = manual_url.split("/")[-1]
  t="http://www.frankshospitalworkshop.com/equipment/"+manual_url.replace(" ","%20")
  print(t)
  response = requests.get(t)
  with open(filename, "wb") as f:
    f.write(response.content)
'''
#print("Downloaded manuals:", manuals)
