import tkinter as tk
from bs4 import BeautifulSoup
import requests

def get():
  a = e1.get()
  b=requests.get(f'https://google.com/search?q={a}')
  soup = BeautifulSoup(b, "html")
  for html in soup.find_all("tag1"):
    html = html.htmltext.text
    cdata_soup = BeautifulSoup(html, "html")
    title=cdata_soup.title.text
  window.title(title)
  anchor.config(text=cdata_soup.a.text)
  bold.config(text=cdata_soup.b.text)
  paragraph.config(text=cdata_soup.p.text)
  get.after(100, get())

window = tk.Tk()
window.title("Browser")
window.geometry("300x300")
window.config(bg="black")
tk.Label(text="Browser", bg="black",fg="cyan", font=("calibre", 19, "bold")).pack(anchor="n", side="top")
e1=tk.Entry(window).pack(anchor="ne", side="top")
button = tk.Button(text="Search", bg="black", fg="cyan",borderwidth=0, command=get())
button.pack(anchor="ne", side="top")
anchor=tk.Lable(bg="black",fg="cyan")
anchor.pack()
bold=tk.Lable(bg="black",fg="cyan")
bold.pack()
paragraph=tk.Lable(bg="black", fg="cyan")
paragraph.pack()
window.mainloop()