import tkinter as tk
import random

def add_coins():
    global coins
    coins += coins_per_click
    coins_label.config(text="Твои деньги 💰: " + str(coins))

def upgrade():
    global coins, coins_per_click, upgrade_cost
    if coins >= upgrade_cost:
        coins -= upgrade_cost
        coins_per_click += 1
        upgrade_cost *= 10
        coins_label.config(text="Твои деньги 💰: " + str(coins))
        upgrade_btn.config(text="Стать лучше 🎉 (Цена: " + str(upgrade_cost) + ")")

def test_luck():
    global coins
    if coins >= 100:
        coins -= 100
        coins_label.config(text="Твои деньги 💰: " + str(coins))
        luck = random.randint(0, 1)
        if luck == 1:
            coins += 200
            coins_label.config(text="Твои деньги 💰: " + str(coins) + " Пошел дождь из $")
        else:
            coins_label.config(text="Твои деньги 💰: " + str(coins) + " Деньги сгорели !!!")

def treat_with_donut():
    global coins
    if coins >= 10:
        coins -= 10
        coins_label.config(text="Твои деньги 💰: " + str(coins))
        
    with open("donut_logs.txt", "a") as file:
        file.write("Donut treated for 10 coins\n")
    file.close()

root = tk.Tk()
root.title("Криптоигра 🤑")

coins = 200
coins_per_click = 1
upgrade_cost = 7

coins_label = tk.Label(root, text="Твои деньги 💰: " + str(coins))
coins_label.pack()

add_coins_btn = tk.Button(root, text="⚽ КЛИК ⚽", command=add_coins)
add_coins_btn.pack()

upgrade_btn = tk.Button(root, text="Стать лучше 🎉 (Цена: " + str(upgrade_cost) + ")", command=upgrade)
upgrade_btn.pack()

test_luck_btn = tk.Button(root, text="Казино 🧨|🎁 (Цена: 100)", command=test_luck)
test_luck_btn.pack()

treat_with_donut_btn = tk.Button(root, text="🍩 Угостить меня пончиком 🍩 (ЗА 10 $)", command=treat_with_donut)
treat_with_donut_btn.pack()

root.mainloop()

'''
from tkinter import *

window = Tk()
window.title("Добро пожаловать в tkinter!")
window.geometry('400x250')
lb = Label(window, text="Привет пользователь", font=("Arial Bold", 26))
lb.grid(column=0, row=0)

txt = Entry(window, width=50)
txt.grid(column=0, row=1)

def clicked_button():
    temp = "Привет {}".format(txt.get())
    lb.configure(text=temp)

btn = Button(window, text="Не нажимать!", bg="red", fg="white",
              command=clicked_button)
btn.grid(column=0, row=2)



window.mainloop()
'''
"""
from tkinter import *

coin = 0
window = Tk()
window.title("Добро пожаловать в tkinter!")
window.geometry('400x250')
lb = Label(window, text="Привет пользователь", font=("Arial Bold", 26))
lb.grid(column=0, row=0)

txt = Entry(window, width=50)
txt.grid(column=0, row=1)

def clicked_button():
    global coin
    coin = coin + 1
    temp = f"Coins {coin}"
    lb.configure(text=temp)

btn = Button(window, text="Не нажимать!", bg="red", fg="white",
              command=clicked_button)
btn.grid(column=0, row=2)



window.mainloop()
"""
