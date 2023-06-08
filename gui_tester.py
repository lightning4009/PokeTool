import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text = 'hi howdy hey',
                    foreground='white',
                    background='purple',
                    width=10,
                    height=10)

button=tk.Button(text='Click me!',
                 width=25,
                 height=5,
                 bg='blue',
                 fg='yellow')

entry=tk.Entry(fg='yellow',
               bg='blue',
               width=50)

text_box=tk.Text()

text_box.pack()
entry.pack()
button.pack()
greeting.pack()

window.mainloop()