import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime


def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_details_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)

    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')

    info_div = bs.find("div", class_="site-stats-count").find_all("li")

    all_details = "\n" + "Corona detail of India: " + "\n\n"
    for block in info_div:
        text = block.find("span", class_="mob-show").get_text()
        count = block.find("strong", class_="").get_text()
        all_details = all_details + text + " : " + count + "\n"


    return all_details

def refresh():
    newdata = get_corona_details_of_india()
    print("Refreshing....")
    mainLabel['text'] = newdata

#GUI

root = tk.Tk()
root.geometry("600x700")
root.iconbitmap("icon.ico")
root.title("CORONA DATA TRACKER")
root.configure(background = 'white')

f = ("poppins", 25, "bold")

banner = tk.PhotoImage(file = "image.png")
bannerLabel = tk.Label(root, image = banner, bg = 'white')
bannerLabel.pack()

mainLabel = tk.Label(root, text = get_corona_details_of_india(), font = f, bg = 'white')
mainLabel.pack()

reBtn = tk.Button(root, text = "REFRESH", font = f, command = refresh)
reBtn.pack()


root.mainloop()


