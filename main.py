"""
Path: main.py
Python Version: 3.11.4
Author: Bradley Pleasant - https://github.com/IcoTwilight
Project GitHub: https://github.com/IcoTwilight/Beyond-Infinity
File Description: This is the main file for the Beyond Infinity project.
"""
from PyTiled import PyTiled, World, TileSet, Tile


class BeyondInfinity:
	def __init__(self) -> None:
		self.engine = PyTiled(window_resolution = (800, 600), window_title = "Beyond Infinity")
	
	def run(self) -> None:
		pass


if __name__ == "__main__":
	print("Beyond Infinity Shell")
	game = BeyondInfinity()
	game.run()
