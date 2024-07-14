#Відкриває додатковий звстосунок в якому має бути елементи керування 
from tkinter import *

kino = Tk()
kino.title("Кіно")
kino.geometry("1000x600")
kino.configure(bg="#181818")

button1 = Button(kino, text="Кіно 1", command=lambda: print("Кіно 1"))
button2 = Button(kino, text="Кіно 2", command=lambda: print("Кіно 2"))

# Розміщення кнопок
button1.pack(pady=10)
button2.pack(pady=10)



kino.mainloop()
