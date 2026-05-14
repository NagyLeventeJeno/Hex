import subprocess
import tkinter as tk
from tkinter import messagebox
import math

class HexGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hex Játék")
        self.root.geometry("600x600")
        
        self.mode = None  
        self.size = 7     
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")
        
        self.show_menu()

    def clear_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_menu(self):
        self.clear_screen()
        tk.Label(self.main_frame, text="HEX JÁTÉK", font=("Arial", 20, "bold")).pack(pady=20)
        
        tk.Button(self.main_frame, text="1 Játékos", width=25, command=lambda: self.select_size(1)).pack(pady=10)
        tk.Button(self.main_frame, text="2 Játékos", width=25, command=lambda: self.select_size(2)).pack(pady=10)

    def select_size(self, mode):
        self.mode = mode
        self.clear_screen()
        tk.Label(self.main_frame, text="Válassz táblaméretet:", font=("Arial", 16)).pack(pady=20)
        
        tk.Button(self.main_frame, text="7 x 7", width=20, command=lambda: self.init_game(7)).pack(pady=5)
        tk.Button(self.main_frame, text="11 x 11", width=20, command=lambda: self.init_game(11)).pack(pady=5)
        tk.Button(self.main_frame, text="vissza", width=20, command=lambda: self.show_menu()).pack(pady=10)

    def init_game(self, size):
        self.size = size
        self.clear_screen()
        
        if self.mode == 2:
            self.start_pvp_process()
            self.show_menu() 
        elif self.mode == 1 and self.size == 7:
            self.start_bot_process()
            self.show_menu()
        else:
            tk.Label(self.main_frame, text="FEJLESZTÉS ALATT", font=("Arial", 20, "bold"), fg="red").pack(pady=50)
            tk.Button(self.main_frame, text="Vissza a menübe", width=20, command=self.show_menu).pack()

    def start_pvp_process(self):
        try:
            self.root.withdraw() 
            subprocess.run(["python", "pvp.py", str(self.size)])
            self.root.deiconify()
        except Exception as e:
            self.root.deiconify() 
            messagebox.showerror("Hiba", f"Hiba történt: {e}")

    def start_bot_process(self):
        try:            
            self.root.withdraw() 
            subprocess.run(["python", "bot_levi_1.py"])
            self.root.deiconify()
        except Exception as e:
            self.root.deiconify() 
            messagebox.showerror("Hiba", f"Hiba történt: {e}")
if __name__ == "__main__":
    root = tk.Tk()
    app = HexGameApp(root)
    root.mainloop()
