"""
Path: main.py
Python Version: 3.11.4
Author: Bradley Pleasant - https://github.com/IcoTwilight
Project GitHub: https://github.com/IcoTwilight/Beyond-Infinity
File Description: This is the main file for the Beyond Infinity project.
"""
from PyTiled import PyTiled, TileSet, Tile, pygame


class BeyondInfinity:
	def __init__(self) -> None:
		self.engine = PyTiled(window_resolution = (800, 600), window_title = "Beyond Infinity")
		self.test_tile_set = TileSet("test")
		self.test_tile = Tile(self.engine.load_image("Images/test.png"), self.test_tile_set)
		self.test_tile2 = Tile(self.engine.load_image("Images/test2.png"), self.test_tile_set)
		self.engine.world.default_tile = self.test_tile
		self.engine.world.set_tile(0, 0, self.test_tile2)
	
	def run(self) -> None:
		while self.engine.update():
			self.engine.load_events()
			if self.engine.is_key_pressed(pygame.K_w): self.engine.camera.move(0, -0.1)
			if self.engine.is_key_pressed(pygame.K_a): self.engine.camera.move(-0.1, 0)
			if self.engine.is_key_pressed(pygame.K_s): self.engine.camera.move(0, 0.1)
			if self.engine.is_key_pressed(pygame.K_d): self.engine.camera.move(0.1, 0)
			if self.engine.is_mouse_button_just_pressed(1):
				self.engine.world.set_tile(*self.engine.get_mouse_position_world(), self.test_tile2)
			self.engine.draw_world()


if __name__ == "__main__":
	print("Beyond Infinity Shell")
	game = BeyondInfinity()
	game.run()
	