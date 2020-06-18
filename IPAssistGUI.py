import tkinter
import socket

# Get the IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 1))
ip_address = str(s.getsockname()[0])


# Draw the UI window
root = tkinter.Tk()
root.title("Ben Assist")

# Calculate and set window position and size
scr_x = root.winfo_screenwidth()
scr_y = root.winfo_screenheight()
win_x = 200
win_y = 25
x_pos = (scr_x//2)-(win_x//2)
y_pos = (scr_y//2)-(win_y//2)
root.geometry(str(win_x)+'x'+str(win_y)+'+'+str(x_pos)+'+'+str(y_pos))

# Populate the window
tkinter.Label(root, text="IP address:"+ip_address).grid(row=0, column=0)
