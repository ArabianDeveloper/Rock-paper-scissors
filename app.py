from tkinter import *
import random

def play(btn, ply):
    global win
    global t
    if not win and not t:
        if ply['emy'] == btn['text']:
            win = True
            dash.configure(text = 'لقد فزت')
        if ply['emy'] != btn['text']:
            win = True
            dash.configure(text = 'فزت عليك')
        

def clear():
    global ply
    global win
    global t
    ply = random.choice(r)
    win = False
    t = False
    dash.configure(text='')


win = False
t = False
font = 'Tajawal'
width = 50
height = 50
r = [
    {
        'it' : '✂',
        'emy' : '🧱'
    },
    {
        'it' : '🧱',
        'emy' : '📜'
    },
    {
        'it' : '📜',
        'emy' : '✂'
    }
]

ply = random.choice(r)


root = Tk()
root.geometry("200x160")
root.resizable(False, False)
root.title("لعبة")

dash = Label(root, bg='black', fg='white', font = (font))
dash.place(x = 50, y = 8, width=100, height=35)

btn1 = Button(root, text = "🧱", command = lambda:play(btn1 ,ply), font = (font, 13))
btn2 = Button(root, text = "📜", command = lambda:play(btn2 ,ply), font = (font, 13))
btn3 = Button(root, text = "✂", command = lambda:play(btn3 ,ply), font = (font, 13))
btn1.place(x = 20, y = 50, width = width, height = height)
btn2.place(x = 75, y = 50, width = width, height = height)
btn3.place(x = 130, y = 50, width = width, height = height)


btn4 = Button(root, text = "اعادة", command = clear, font = (font, 11))
btn4.place(x = 50, y = 110, width = 100, height = 40)
root.mainloop()