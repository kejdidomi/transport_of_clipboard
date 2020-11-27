# transport_of_clipboard
A way to "copy" in one computer and "paste" on the other
## Inspiration
This is actually a very dumb idea. I have 2 computers in my home and sometimes I want to transfer code from my laptop to my desktop pc, 
so i thought wouldn't it be nice if I could hit "copy" in my laptop and somehow hit "paste" in my pc and it would work that way. Now I am sure there must be a ton
of different ways to do this that could be easier or more efficient, but I wanted also to learn and h=get used to socket programming, and I 
thought this would be at least useful to some extent.
## Requirements
- Python 3.x installed on both devices
- PySimpleGUI module: can be installed with the command `pip install pysimplegui` in cmd (sidenote this is only tested in Windows for now)
- At least 2 computers (we are gonna call them COMPUTER1 and COMPUTER2)
## Limitations
- You can send only text so no images or files.
- There is a limit to the length of the text you can send. By default you can only send **100 000 bytes (100 000 characters)**, although it can be changed.
## How to Use
1. Download transport.py file in COMPUTER1 and COMPUTER2
2. Edit transport.py in each computer
    1. In COMPUTER1 put the IP of COMPUTER1 here `SELF = "one-ip-here"` and the IP of COMPUTER2 here `OTHER = "the-other-ip-here"` (I'm assuming you know how to find IPs, if you don't, google it)
    2. In COMPUTER2 put the IP of COMPUTER2 here `SELF = "one-ip-here"` and the IP of COMPUTER1 here `OTHER = "the-other-ip-here"`
3. Run the program simultaneously in both computers by opening a command prompt, navigating to the folder that you seved transport.py and passing `python transport.py` as a command
4. **IT IS ESSENCIAL THAT THE FIRST THING YOU DO IS DECIDE THE RECEIVER AND CLICK "Receive" AND THEN FROM THE OTHER COMPUTER CLICK SEND.***-
Now whatever you copied in COMPUTER1, let's say, is in the clipboard of COMPUTER2 so you can hit "paste" and verify for yourself. 
NOTE: Do not close the program if you haven't his paste.
## Future Improvements
1. Geting rid of editing the IPs. This can be done by using this tutorial https://www.tutorialspoint.com/python-program-to-find-the-ip-address-of-the-client .
2. Better interface, "tkinter" module used opens some random windows that serve no purpose.
3. Maybe working with buffers in a way to store and keep the connection open.
4. Image and file transfer.
