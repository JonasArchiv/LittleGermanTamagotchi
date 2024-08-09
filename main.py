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