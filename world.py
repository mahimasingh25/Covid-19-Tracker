import requests
import bs4
import tkinter as tk
import plyer
import time
import threading

def get_html_data(url):
    data = requests.get(url)
    return data

def get_covid_data():
    url="https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs=bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").find_all("div", id="maincounter-wrap")
    all_data = "\n CoronaVirus data of the world: \n\n"
    for block in info_div:
        text = block.find("h1", class_="").get_text()
        count = block.find("span", class_="").get_text()
        all_data = all_data+text + " " + count+"\n"
    return all_data

def get_country_data():
    name = textfield.get()
    url = "https://www.worldometers.info/coronavirus/country/"+name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").find_all("div", id="maincounter-wrap")
    all_data = "\n"
    for block in info_div:
        text = block.find("h1", class_="").get_text()
        count = block.find("span", class_="").get_text()
        all_data = all_data + text + " " + count + "\n"
    mainLabel2['text']=all_data
    

def space():
    space = "  "
    return space

def question():
    text = "\n Enter country name:"
    return text



def reload():
    new_data = get_covid_data()
    print ("Refreshing...")
    mainLabel2['text']=new_data


#notification
def notify_me():
    while True:
        plyer.notification.notify(
            title = "COVID 19 cases of the World",
            message = get_covid_data(),
            timeout = 10,
            app_icon = 'icon.ico'
        )
        time.sleep(1000)





#gui
root = tk.Tk()
root.geometry("700x750")
root.title("COVID-19 Tracker")
root.iconbitmap("icon.ico")
root.configure(background="white")

f = ("Helvetica", 20, "bold")
f2 = ("Helvetica", 20)

banner = tk.PhotoImage(file="image.png")
bannerLabel = tk.Label(root, image=banner, bg = 'white')
bannerLabel.pack()

mainLabel = tk.Label(root, text=question(), font=f2, bg='white')
mainLabel.pack()

textfield = tk.Entry(root, width=50)
textfield.pack()

mainLabel2 = tk.Label(root, text=get_covid_data(), font=f2, bg='white')
mainLabel2.pack()

gBtn = tk.Button(root, text='GET DATA', font=f2, command=get_country_data)
gBtn.pack()

mainLabel3 = tk.Label(root, text=space(), font=f2, bg='white')
mainLabel3.pack()

reBtn = tk.Button(root, text='RELOAD', font=f2, command=reload)
reBtn.pack()

#new thread

th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop()