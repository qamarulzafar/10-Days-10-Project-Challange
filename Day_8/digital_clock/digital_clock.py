import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("600x250")  
root.resizable(False, False)  
root.configure(bg="#2C3E50")  

# Function to update time
def time():
    string = strftime('%H:%M:%S %p\n%A, %d %B %Y') 
    label.config(text=string)
    label.after(1000, time)

# Frame for styling
frame = tk.Frame(root, bg="#2C3E50")
frame.pack(expand=True, fill="both")

# Label for digital clock display
label = tk.Label(
    frame, 
    font=('Arial', 30, 'bold'),  
    background="#34495E",  
    foreground="#ECF0F1",  
    padx=20, 
    pady=10
)
label.pack(pady=20)

time()  
root.mainloop()
