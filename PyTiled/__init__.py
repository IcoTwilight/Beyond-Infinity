"""
Path: PyTiled/__init__.py
Python Version: 3.11.4
Author: Bradley Pleasant - https://github.com/IcoTwilight
Project GitHub: https://github.com/IcoTwilight/Beyond-Infinity
File Description: This file is used to initialize the PyTiled package.
"""
import pygame
from pygame import Surface
import math

# Constants
ANY_TILE = 0


class Tile:
	def __init__(self, surface: Surface, tile_set) -> None:
		self.surface = surface
		self.tile_set: TileSet = tile_set
	
	def __str__(self) -> str:
		return f"(<{self.tile_set.name}> Tile)"
	
	def __repr__(self) -> str:
		return str(self)


class TileSet:
	def __init__(self, name: str, tiles: list[Tile]) -> None:
		self.name = name
		self.tiles = tiles


class World:
	def __init__(self) -> None:
		self.default_tile_set = TileSet("default", [])
		self.world: dict[tuple[int, int]: Tile] = {}
		# tile_rules is a dictionary of rules for tiles
		# it states that if a tile is surrounded by certain tiles,
		# it should be replaced with a different tile
		# the keys are a tuple of 8 tiles, with None representing any tile
		self.tile_rules: dict[tuple[
				TileSet | ANY_TILE, TileSet | ANY_TILE,
				TileSet | ANY_TILE, TileSet | ANY_TILE,
				TileSet | ANY_TILE, TileSet | ANY_TILE,
				TileSet | ANY_TILE, TileSet | ANY_TILE,
			]: Tile] = {}
		
		self.default_tile = Tile(Surface((0, 0)), self.default_tile_set)
	
	def set_tile(self, x: int, y: int, tile: Tile) -> None:
		# use math.floor to round down to the nearest integer
		self.world[(math.floor(x), math.floor(y))] = tile
	
	def get_tile(self, x: int | float, y: int | float) -> Tile:
		x, y = math.floor(x), math.floor(y)
		if (x, y) in self.world:
			return self.world[(x, y)]
		else:
			self.world[(x, y)] = self.generate_tile(x, y)
			return self.world[(x, y)]
	
	def generate_tile(self, x: int | float, y: int | float) -> Tile:
		return self.default_tile
	
	def auto_tile(self, x: int | float, y: int | float) -> None:
		# use math.floor to round down to the nearest integer
		x, y = math.floor(x), math.floor(y)
		# get the tiles around the tile
		tiles: tuple = (
			self.get_tile(x - 1, y - 1).tile_set, self.get_tile(x, y - 1).tile_set,
			self.get_tile(x + 1, y - 1).tile_set, self.get_tile(x - 1, y).tile_set,
			self.get_tile(x + 1, y).tile_set, self.get_tile(x - 1, y + 1).tile_set,
			self.get_tile(x, y + 1).tile_set, self.get_tile(x + 1, y + 1).tile_set,
		)

		# check if the tile is in the tile_rules dictionary
		if tiles in self.tile_rules:
			return self.tile_rules[tiles]
		# if the tile is not in the tile_rules dictionary,
		# we need to iterate through the dictionary to find the
		# correct tile based on the additional ANY_TILE rules
		
		for rule, tile in self.tile_rules.items():
			# iterate through the rule tuple
			for i in range(8):
				# check if the rule is not ANY_TILE
				if rule[i] != ANY_TILE:
					# if the rule is not ANY_TILE, check if the tile matches
					if rule[i] != tiles[i]:
						# if the tile does not match, break out of the loop
						break
			else:
				# if the loop did not break, return the tile
				return tile
	
	def set_tile_rules(self, **rules) -> None:
		# rules : dict[tuple[
		# 				TileSet | ANY_TILE, TileSet | ANY_TILE,
		# 				TileSet | ANY_TILE, TileSet | ANY_TILE,
		# 				TileSet | ANY_TILE, TileSet | ANY_TILE,
		# 				TileSet | ANY_TILE, TileSet | ANY_TILE,
		# 			]: Tile]
		self.tile_rules.update(rules)


class Camera:
	def __init__(self, py_tiled, x: int | float = 0, y: int | float = 0) -> None:
		self.pyTiled = py_tiled
		self.x = x
		self.y = y
	
	def convert_to_screen(self, x: int | float, y: int | float) -> tuple[float | int, float | int]:
		return (x - self.x) * self.pyTiled.tile_size, (y - self.y) * self.pyTiled.tile_size
	
	def convert_to_world(self, x: int | float, y: int | float) -> tuple[float | int, float | int]:
		return (x / self.pyTiled.tile_size) + self.x, (y / self.pyTiled.tile_size) + self.y
	
	def move(self, x: int | float, y: int | float) -> None:
		self.x += x
		self.y += y
	
	def set_position(self, x: int | float, y: int | float) -> None:
		self.x = x
		self.y = y
	
	def get_on_screen(self, screen_size: tuple[int, int]) -> tuple[int]:
		# get the tile position of the top left corner of the screen
		left, top = self.convert_to_world(0, 0)
		left, top = math.floor(left), math.floor(top)
		# get the tile position of the bottom right corner of the screen
		right, bottom = self.convert_to_world(screen_size[0], screen_size[1])
		right, bottom = math.ceil(right), math.ceil(bottom)
		
		# generate the tile_positions between the top left and bottom right
		# corners of the screen
		for x in range(left, right):
			for y in range(top, bottom):
				yield x, y
		

class PyTiled:
	def __init__(self, window_resolution, window_title) -> None:
		# initialize pygame
		pygame.init()
		self.window_height, self.window_width = self.window_resolution = window_resolution
		self.screen = pygame.display.set_mode(self.window_resolution, pygame.RESIZABLE |
		                                      pygame.DOUBLEBUF |
		                                      pygame.HWSURFACE
		                                      )
		pygame.display.set_caption(window_title)
		self.clock = pygame.time.Clock()
		self.world = World()
		
		# initialize the clock and set running to True
		self.running = True
		self.tile_size = 32
		
		# initialize the camera
		self.camera = Camera(self)
		
		self.keys_pressed                   = pygame.key.get_pressed()
		self.keys_just_pressed              = set()
		self.keys_just_released             = set()
		self.mouse_buttons_pressed          = pygame.mouse.get_pressed()
		self.mouse_buttons_just_pressed     = set()
		self.mouse_buttons_just_released    = set()
		self.mouse_position                 = pygame.mouse.get_pos()
		self.mouse_position_world           = self.camera.convert_to_world(*self.mouse_position)
	
	def load_events(self):
		self.keys_pressed                   = pygame.key.get_pressed()
		self.keys_just_pressed              = set()
		self.keys_just_released             = set()
		self.mouse_buttons_pressed          = pygame.mouse.get_pressed()
		self.mouse_buttons_just_pressed     = set()
		self.mouse_buttons_just_released    = set()
		self.mouse_position                 = pygame.mouse.get_pos()
		self.mouse_position_world           = self.camera.convert_to_world(*self.mouse_position)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
				self.keys_just_pressed.add(event.key)
			elif event.type == pygame.KEYUP:
				self.keys_just_released.add(event.key)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.mouse_buttons_just_pressed.add(event.button)
			elif event.type == pygame.MOUSEBUTTONUP:
				self.mouse_buttons_just_released.add(event.button)
			elif event.type == pygame.VIDEORESIZE:
				self.window_height, self.window_width = self.window_resolution = event.size
				self.screen = pygame.display.set_mode(self.window_resolution, pygame.RESIZABLE)
	
	def update(self):
		pygame.display.flip()
		self.clock.tick(60)
		self.screen.fill((0, 0, 0))
		return self.running

	def draw_tile(self, tile: Tile, x: int | float, y: int | float) -> None:
		self.screen.blit(tile.surface, self.camera.convert_to_screen(x, y))
	
	def draw_world(self) -> None:
		for x, y in self.camera.get_on_screen(self.window_resolution):
			self.draw_tile(self.world.get_tile(x, y), x, y)
			