
import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import webbrowser

GREEN = "#24C66B"
DARK = "#101510"
WHITE = "#FFFFFF"
GREY = "#A8B5AA"

class RokoriPS:

    def __init__(self, root):
        self.root = root
        self.root.title("Rokori PS")
        self.root.geometry("650x520")
        self.root.configure(bg=DARK)
        self.root.resizable(False, False)

        self.runtime = None
        self.home()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def header(self):
        tk.Label(
            self.root,
            text="PS",
            bg=GREEN,
            fg=WHITE,
            font=("Arial", 26, "bold"),
            width=4,
            height=2
        ).pack(pady=(25, 5))

        tk.Label(
            self.root,
            text="ROKORI PS",
            bg=DARK,
            fg=WHITE,
            font=("Arial", 25, "bold")
        ).pack()

    def button(self, title, command):
        tk.Button(
            self.root,
            text=title,
            command=command,
            bg=GREEN,
            fg=WHITE,
            activebackground="#15994D",
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
            width=30,
            height=2
        ).pack(pady=9)

    def home(self):
        self.clear()
        self.header()

        tk.Label(
            self.root,
            text="Welcome!",
            bg=DARK,
            fg=WHITE,
            font=("Arial", 24, "bold")
        ).pack(pady=(25, 5))

        tk.Label(
            self.root,
            text="Your Linux Roblox launcher",
            bg=DARK,
            fg=GREY,
            font=("Arial", 12)
        ).pack(pady=5)

        self.button("SELECT CORDIAL APPIMAGE", self.select_runtime)
        self.button("PLAY ROBLOX", self.play)
        self.button("DOWNLOAD CORDIAL", self.download)
        self.button("SETTINGS", self.settings)

        self.status = tk.Label(
            self.root,
            text="Runtime not selected",
            bg=DARK,
            fg=GREY
        )
        self.status.pack(pady=15)

        tk.Label(
            self.root,
            text="PS_STUDIOS | ROKORI PS",
            bg=DARK,
            fg=GREEN
        ).pack(side="bottom", pady=20)

    def select_runtime(self):
        path = filedialog.askopenfilename(
            title="Select Cordial AppImage",
            filetypes=[("AppImage", "*.AppImage"), ("All files", "*.*")]
        )

        if path:
            self.runtime = path
            self.status.config(
                text="Cordial selected",
                fg=GREEN
            )

    def play(self):
        if not self.runtime:
            messagebox.showinfo(
                "Rokori PS",
                "Select your Cordial AppImage first."
            )
            return

        try:
            os.chmod(self.runtime, 0o755)
            subprocess.Popen([self.runtime])
        except Exception as error:
            messagebox.showerror("Launch error", str(error))

    def download(self):
        webbrowser.open(
            "https://github.com/luohoa97/cordial"
        )

    def settings(self):
        messagebox.showinfo(
            "Settings",
            "Rokori PS\nLinux Edition\nPS_Studios"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = RokoriPS(root)
    root.mainloop()
