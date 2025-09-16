import tkinter as tk

affirmations = [
    "Main duniya saktisali banunga.",
    "Har din main mentally aur physically strong ho raha hoon.",
    "Koi bhi takleef mujhe rok nahi sakti."
]

def show_affirmation():
    label.config(text=affirmations.pop(0) if affirmations else "Ho gaya bhaiya!")

root = tk.Tk()
root.title("MMA Mindset Booster")

label = tk.Label(root, text="Start your day strong!", font=("Arial", 16))
label.pack(pady=20)

btn = tk.Button(root, text="Next Affirmation", command=show_affirmation)
btn.pack(pady=10)

root.mainloop()
