import streamlit as sl
import requests
from bs4 import BeautifulSoup

# sl.image("https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114")
sl.markdown("<h1 style ='text-align: center;'>Web Scraper</h1>", unsafe_allow_html=True)
with sl.form("Search"):
     keyword = sl.text_input("Enter Your Keyword")
     search = sl.form_submit_button("Search")
     if search:
      page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
      print(page.status_code)
      soup=BeautifulSoup(page.content,'lxml') 
      rows = soup.find_all("div", class_="bugb2")
      for row in rows:
          figures = row.find_all("figure")
          for i in range(2):
              img = figures[i].find("img", class_="SpgDA")
              print(img)
              print("\n\n")      
     