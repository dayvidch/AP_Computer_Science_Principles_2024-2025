import tkinter as tk

root = tk.Tk()
root.wm_geometry("400x400")
root.title("Question 28")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

root.grid_columnconfigure(0, weight=2) 
root.grid_columnconfigure(1, weight=1)  

topleft = tk.Frame(root, bg="blue")
topleft.grid(row=0, column=0, sticky="news")

topright = tk.Frame(root, bg="lime")
topright.grid(row=0, column=1, sticky="news")

bottomleft = tk.Frame(root, bg="red")
bottomleft.grid(row=1, column=0, sticky="news")

bottomright = tk.Frame(root, bg="yellow")
bottomright.grid(row=1, column=1, sticky="news")

root.mainloop()
