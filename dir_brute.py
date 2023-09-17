import requests
import time
import os

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
    wordlist = open(".\diretorios.txt", "r").readlines()
    wordlist = [x.replace("\n", "") for x in wordlist]

    for word in wordlist:
        request = requests.get(website + word)
        if request.status_code != 200:
            print(f'\033[1;32m[{request.status_code}]\033[0;0m {word} ')
            os.system("cls || clear")
    for word in wordlist:
        request = requests.get(website + word)
        if request.status_code == 200:
            time.sleep(0.1)
            print(f'\033[1;32m[{request.status_code}]\033[0;0m {word} ')

if __name__ == '__main__':
    main()

print("tente /.htaccess")
print("tente /web.config\n")
