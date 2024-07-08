from bs4 import BeautifulSoup
import requests

response = requests.get("https://1000logos.net/asl-alphabet/")

alphabet_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

images = soup.find_all(name="img")

for image in images:
    url = image.get("data-src")
    asl_text = url.split("https://1000logos.net/wp-content/uploads/2023/08/")
    if len(asl_text) == 2:
        asl_text_end = asl_text[1].split('ASL-Alphabet-')
        if len(asl_text_end) == 2:
            alphabet = asl_text_end[1].split("-")
            if len(alphabet) == 2:
                if alphabet[0] in alphabet_letters:
                    data = requests.get(url).content
                    file = open(f'C:/Users/Mann/demos/asl/asl_alphabet_train/asl_alphabet_train/{alphabet[0]}/ASL-{alphabet[0]}.png', 'wb')
                    file.write(data)
                    file.close()