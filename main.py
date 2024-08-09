import tkinter as tk
from tkinter import messagebox
import time


class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.energy = 5
        self.alive = True
        self.update_status()

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            self.update_status()
            return True
        return False

    def play(self):
        if self.happiness < 10 and self.energy > 1:
            self.happiness += 1
            self.energy -= 1
            self.update_status()
            return True
        return False

    def sleep(self):
        if self.energy < 10:
            self.energy += 2
            self.update_status()
            return True
        return False

    def update_status(self):
        if self.hunger >= 10 or self.happiness <= 0 or self.energy <= 0:
            self.alive = False
        self.status = {
            'hunger': self.hunger,
            'happiness': self.happiness,
            'energy': self.energy
        }

    def get_status(self):
        return self.status

class TamagotchiApp:
    def __init__(self, root, tama):
        self.root = root
        self.tama = tama
        self.root.title(f"{tama.name}'s Tamagotchi")

        self.label = tk.Label(root, text=self.get_status_text(), font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.feed_button = tk.Button(root, text="Füttern", command=self.feed_tama)
        self.feed_button.pack(pady=5)

        self.play_button = tk.Button(root, text="Spielen", command=self.play_with_tama)
        self.play_button.pack(pady=5)

        self.sleep_button = tk.Button(root, text="Schlafen", command=self.sleep_tama)
        self.sleep_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Beenden", command=self.quit_app)
        self.quit_button.pack(pady=20)

        self.update_status()

    def get_status_text(self):
        if not self.tama.alive:
            return f"{self.tama.name} ist leider gestorben."
        status = self.tama.get_status()
        return (f"Hunger: {status['hunger']}\n"
                f"Glück: {status['happiness']}\n"
                f"Energie: {status['energy']}")

    def feed_tama(self):
        if not self.tama.alive:
            messagebox.showinfo("Info", "Das Tamagotchi ist leider gestorben.")
            return
        if self.tama.feed():
            messagebox.showinfo("Info", f"{self.tama.name} wurde gefüttert!")
        else:
            messagebox.showinfo("Info", f"{self.tama.name} ist nicht hungrig.")
        self.update_status()

    def play_with_tama(self):
        if not self.tama.alive:
            messagebox.showinfo("Info", "Das Tamagotchi ist leider gestorben.")
            return
        if self.tama.play():
            messagebox.showinfo("Info", f"{self.tama.name} hat gespielt!")
        else:
            messagebox.showinfo("Info", f"{self.tama.name} ist zu müde oder sehr glücklich.")
        self.update_status()