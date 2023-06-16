import tkinter as tk
import os
import platform


window = tk.Tk()
window.geometry("250x170")
window.title("Connect to doomroom server")

ip = tk.Label(window, text="Server ip:")
iptext = tk.Text(window, height = 1, width=8)

roomname = tk.Label(window, text="Room name:")
roomnametext = tk.Text(window, height=1, width= 15)

def connect():
    if platform.system() == "Linux":
        os.system(f"./client connect {iptext.get('1.0', tk.END).strip()} \"{roomnametext.get('1.0', tk.END).strip()}\"")
    elif platform.platform() == "Windows":
        os.system(f".\client.exe connect {iptext.get('1.0', tk.END)} \"{roomnametext.get('1.0', tk.END)}\"")
    window.destroy()

connectbtn = tk.Button(window, text="Connect", command=connect)

ip.pack()
iptext.pack()
roomname.pack()
roomnametext.pack()
connectbtn.pack()

defaultip = ""
iptext.insert(tk.END, defaultip)


window.mainloop()