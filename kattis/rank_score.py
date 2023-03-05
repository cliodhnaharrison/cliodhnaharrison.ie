from bs4 import BeautifulSoup
import urllib.request

url = "http://open.kattis.com/users/cliodhna-harrison"
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
page = urllib.request.urlopen(req)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
numbers = soup.find_all("span", attrs={"class":"important_number"})

print("Rank:", numbers[0].contents[0])
print("Score:", numbers[1].contents[0])
