from Bs4 import BeatifulSoup
import requests

u1=input("Δώσε το URL (ex.:http://www.cs.unipi.gr):")
s=requests.get(u1)
html1=BeatifulSoup(s.text,'lxml')

new_lines=0
linkssites=0

link=html1.find_all('b')
linkssites=len(link)
space=html.find_all('br')
paragraf=html.find_all('p')
new_lines=len(space)+len(paragraf)
print(f"yparxoyn:{linkssites} syndesmoi kai{new_lines} allages stis grammes.")
