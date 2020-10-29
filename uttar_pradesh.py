import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime


def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_details_of_up():
    url = "https://maps.covidindia.org/?state=UP"
    html_data = get_html_data(url)

    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')

    print(html_data.text)


get_corona_details_of_up()
