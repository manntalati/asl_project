from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.wikihow.com/Fingerspell-the-Alphabet-in-American-Sign-Language")

alphabet_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

all_images = soup.find_all(name="img", class_="whcdn content-fill")
i = 0
for image in all_images:
    if (image.get("data-src") != None):
        file = open(f'C:/Users/Mann/demos/asl/train/{alphabet_letters[i]}_train/ASL-{alphabet_letters[i]}2.png', 'wb')
        file.write(requests.get(image.get("data-src")).content)
        file.close()
        i+=1