"""
Path: PyTiled/__init__.py
Python Version: 3.11.4
Author: Bradley Pleasant - https://github.com/IcoTwilight
Project GitHub: https://github.com/IcoTwilight/Beyond-Infinity
File Description: This file is used to initialize the PyTiled package.
"""
from pygame import Surface
import math

# Constants
ANY_TILE = 0


class Tile:
	def __init__(self, surface: Surface, tile_set) -> None:
		self.surface = surface
		self.tile_set: TileSet = tile_set


class TileSet:
	def __init__(self, name: str, tiles: list[Tile]) -> None:
		self.name = name
		self.tiles = tiles


class World:
	def __init__(self) -> None:
		self.all_tile_set = TileSet("All", [])
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
		]: Tile
		] = {}
	
	def set_tile(self, x: int, y: int, tile: Tile) -> None:
		# use math.floor to round down to the nearest integer
		self.world[(math.floor(x), math.floor(y))] = tile
	
	def get_tile(self, x: int, y: int) -> Tile:
		x, y = math.floor(x), math.floor(y)
		if (x, y) in self.world:
			return self.world[(x, y)]
		else:
			return self.generate_tile(x, y)
	
	def generate_tile(self, x: int, y: int) -> Tile:
		return Tile(Surface((0, 0)), self.all_tile_set)
	
	def auto_tile(self, x: int, y: int) -> Tile:
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
		else:
			return self.get_tile(x, y)


class PyTiled:
	def __init__(self) -> None:
		pass
