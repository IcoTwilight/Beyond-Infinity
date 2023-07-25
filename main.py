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
		self.engine.tile_size = 64
		self.test_tile_set = TileSet("test")
		self.tiles: TileSet = self.engine.load_tile_set("Images/World Sprite Sheet.png", 8, 8)
		self.selected_tile_index = 0
	
	def run(self) -> None:
		while self.engine.update():
			self.engine.load_events()
			if self.engine.is_key_pressed(pygame.K_w): self.engine.camera.move(0, -0.1)
			if self.engine.is_key_pressed(pygame.K_a): self.engine.camera.move(-0.1, 0)
			if self.engine.is_key_pressed(pygame.K_s): self.engine.camera.move(0, 0.1)
			if self.engine.is_key_pressed(pygame.K_d): self.engine.camera.move(0.1, 0)
			
			self.selected_tile_index += self.engine.get_mouse_wheel()
			self.selected_tile_index %= len(self.tiles.tiles)
			
			if self.engine.is_mouse_button_just_pressed(1):
				self.engine.world.set_tile(*self.engine.get_mouse_position_world(), self.tiles.tiles[self.selected_tile_index])
			
			# if the middle mouse button is pressed, set the tile to the tile at the mouse position
			if self.engine.is_mouse_button_just_pressed(2):
				self.selected_tile_index = self.tiles.get_tile_index(
						self.engine.world.get_tile(*self.engine.get_mouse_position_world())
				)
			
			self.engine.draw_world()
			
			self.engine.draw_raw(
					pygame.transform.scale(self.tiles.tiles[self.selected_tile_index].surface, (64, 64)),
					0, 0)
	
	def visualize_tile_set(self):
		while self.engine.update():
			# load events
			self.engine.load_events()
			# draw each tile in the tile set as a 6 by 6 grid
			for i, tile in enumerate(self.tiles.tiles):
				self.engine.draw_raw(
						pygame.transform.scale(tile.surface, (64, 64)),
						(i % 6) * 64, (i // 6) * 64)
				# draw the tile index
				self.engine.draw_raw_text(str(i), (i % 6) * 64 + 32, (i // 6) * 64 + 32)
		self.run()
			


if __name__ == "__main__":
	print("Beyond Infinity Shell")
	game = BeyondInfinity()
	while True:
		game.run()
		if game.engine.is_key_pressed(pygame.K_ESCAPE): break
		game.engine.running = True
		game.visualize_tile_set()
		if game.engine.is_key_pressed(pygame.K_ESCAPE): break
		game.engine.running = True
	