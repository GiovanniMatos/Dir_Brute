import requests
import urllib.request
from os import path


print(" ex: https://httpbin.org")
print()
url = input(" URL: ")
print()
response = requests.get(url)
r = response.status_code
if (r == 200):
    print("\033[1;32m[+] Site Ativo \033[0;0m")

response = requests.get(url, verify=True)
r = response.status_code
if (r == 200):
    print("\033[1;32m[+] SSL válido \033[0;0m")


print("="*15, "Diretorios","="*15)
print()

def main():
    website = url
    words_dir = 'diretorios.txt'

    diretorios = path.realpath(words_dir)

    with open(diretorios) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    for word in lines:
        directory = website + word
        try:
            print(f'[{urllib.request.urlopen(directory).getcode()}]  /{word} ')
        except Exception as error:
            pass
if __name__ == '__main__':
    main()
