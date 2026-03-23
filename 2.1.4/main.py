#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_my_button():
    entered_password = ent_password.get()
    password_label.config(text=f"Password: {entered_password}")
    frame_auth.tkraise()

# main window
root = tk.Tk()
root.wm_geometry("400x400")
root.title("authentication")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text = "Password:", font = "Courier")
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3, show="*")
ent_password.pack(pady=5)

btn_login = tk.Button(root, text = "login", command=test_my_button)
btn_login.grid()

password_label = tk.Label(frame_auth, text="Password will be displayed here.")
password_label.pack(pady=20)

frame_login.tkraise()



root.mainloop()