import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.geometry('400x400')

# Add a button to the window
button = tk.Button(root, text='Move me')
button.place(x=50, y=50)
deltaX = -2
deltaY = 5

# Define a function to move the button
def move_button():
    x, y = int(button.place_info()['x']), int(button.place_info()['y'])
    button.place(x=x+deltaX, y=y+deltaY)
    wrap(button,400,400)

# Create an update function
def update():
    move_button()
    root.after(50, update)

# wraps the button to the other side of the screen
# adds the hight of it's self to make it look smoother
def wrap(obj, width, height):
    x = int(obj.place_info()['x'])
    y = int(obj.place_info()['y'])
    button_width = obj.winfo_width()
    button_height = obj.winfo_height()
    if x > width:
        obj.place(x=-button_width, y=y)
    elif y > height:
        obj.place(x=x, y=-button_height)
    elif x + button_width < 0:
        obj.place(x=width, y=y)
    elif y + button_height < 0:
        obj.place(x=x, y=height)


# Start the update function
update()

# Run the Tkinter event loop
root.mainloop()
