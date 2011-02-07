# GUI.py GUI learning and test module
from Tkinter import *
from waker import Waker
root = Tk()

# Make the labels and arrange them
macLabel = Label(root, text="Enter MAC Address (e.g., 00:11:22:33:44:55")
macLabel.grid(row = 0)
ipLabel = Label(root, text="Enter ip address or domain name:")
ipLabel.grid(row = 1)
portLabel = Label(root, text = "Enter port:")
portLabel.grid(row = 2)

# Make and arrange the text entry boxes
macEntry = Entry(root)
ipEntry = Entry(root)
portEntry = Entry(root)

macEntry.grid(row=0,column=1)
ipEntry.grid(row=1,column=1)
portEntry.grid(row=2,column=1)

'Retrieve the data entered and close the window'
def sendIt():
    mac = macEntry.get()
    ip = ipEntry.get()
    port = int(portEntry.get())
    wol = Waker()
    wol.wake(mac, ip, port)
    root.destroy()

b = Button(root, text="Send", command=sendIt)
b.grid()
root.mainloop()