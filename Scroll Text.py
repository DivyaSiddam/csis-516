from tkinter import * # Import tkinter
    
class ScrollText:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Scroll Text Demo") # Set title
        
        frame1 = Frame(window)
        frame1.pack()
        scrollbar = Scrollbar(frame1) # Create a Scrollbar
        scrollbar.pack(side = RIGHT, fill = Y)
        text = Text(frame1, width = 40, height = 10, wrap = WORD, yscrollcommand
            = scrollbar.set) # Set text yscrollcommand to scrollbar
        text.pack()
        scrollbar.config(command = text.yview) # Configure vertical bar
        
        window.mainloop() # Create an event loop

ScrollText() # Create GUI
