from PyTiled import TileSet, Tile, pygame

class TileGenerator:
	def __init__(self, tileset):
		self.tileset = tileset
		self.top_left_tiles = TileSet("top_left")
		self.top_right_tiles = TileSet("top_right")
		self.bottom_left_tiles = TileSet("bottom_left")
		self.bottom_right_tiles = TileSet("bottom_right")
		self.top_left_tiles.add_tile(self.tileset[0],
		                             self.tileset[1],
		                             self.tileset[6],
		                             self.tileset[7],
		                             self.tileset[31],
		                             
		                             self.tileset[3],
		                             self.tileset[4],
		                             self.tileset[9],
		                             self.tileset[10],
		                             
		                             self.tileset[19],
		                             self.tileset[20],
		                             self.tileset[22],
		                             self.tileset[23],
		                             self.tileset[25],
		                             self.tileset[28],
		                             
		                             self.tileset[34],
		                             )
		
		self.top_right_tiles.add_tile(self.tileset[1],
		                              self.tileset[2],
		                              self.tileset[7],
		                              self.tileset[8],
		                              self.tileset[30],
		                              
		                              self.tileset[4],
		                              self.tileset[5],
		                              self.tileset[10],
		                              self.tileset[11],
		                              
		                              self.tileset[20],
		                              self.tileset[21],
		                              self.tileset[18],
		                              self.tileset[23],
		                              self.tileset[24],
		                              self.tileset[25],
		                              
		                              self.tileset[35],
		                              )
		
		self.bottom_left_tiles.add_tile(self.tileset[6],
		                                self.tileset[7],
		                                self.tileset[12],
		                                self.tileset[13],
		                                self.tileset[33],
		                                
		                                self.tileset[9],
		                                self.tileset[10],
		                                self.tileset[15],
		                                self.tileset[16],
		                                
		                                self.tileset[22],
		                                self.tileset[23],
		                                )
		
		self.bottom_right_tiles.add_tile(self.tileset[7],
		                                 self.tileset[8],
		                                 self.tileset[13],
		                                 self.tileset[14],
		                                 self.tileset[32],
		                                 
		                                 self.tileset[10],
		                                 self.tileset[11],
		                                 self.tileset[16],
		                                 self.tileset[17],
		                                 
		                                 self.tileset[23],
		                                 self.tileset[18],
		                                 )
		                              
	
	
	
	def generate(self, tile_above:  TileSet,
	             tile_above_right:  TileSet,
	             tile_right:        TileSet,
	             tile_below_right:  TileSet,
	             tile_below:        TileSet,
	             tile_below_left:   TileSet,
	             tile_left:         TileSet,
	             tile_above_left:   TileSet,
	             ):
		tile = [None, None, None, None]
		if tile_above.name == "Water":
		
		
		