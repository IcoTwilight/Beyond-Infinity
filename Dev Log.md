# Beyond Infinity - Dev Log

---

## Project Details

### Author: [Bradley Pleasant](https://github.com/IcoTwilight)

### Project GitHub: [Beyond Infinity](https://github.com/IcoTwilight/Beyond-Infinity)

---

## Project Dev Log

1. To begin with I decided that I should create a dedicated engine that is designed as its own game engine built on top of pygame. I decided that I would call this engine PyTiled due to it being a tile engine.
2. I then decided that I should create a basic system for storing and editing worlds. This system would be designed to allow for the creation of a world that can be rendered and interacted with.
3. To start this I created multiple classes that would be used to store the data of the world. I needed 3 classes, the Tile which should simply have a texture and a tile set. I also needed a tile set class which merely holds a group of related tiles and then also the world class to hold the data of the world and methods to edit it.
4. 