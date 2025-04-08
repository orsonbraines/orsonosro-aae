#!/usr/bin/env python3
"""
ORSONOSRO ASCII Art Engine (AAE)
"""

import argparse
import sys

def load_file(path):
	pass
	
class Canvas:
	def __init__(self, width, height):
		self.data = bytearray(b' ' * width * height)
		self.width = width
		self.height = height
	
	def coord2index(self, row: int, col: int) -> int:
		if row < 0 or row >= self.height or col < 0 or col >= self.width:
			raise ValueError("Row or column is out of bounds")
		return row * self.width + col

	def index2coord(self, index: int) -> (int, int):
		if index < 0 or index >= self.width * self.height:
			raise ValueError("Index is out of bounds")
		return divmod(index, self.width)

	def fill(self, pattern: str) -> None:
		if not pattern:
			return
			
		pattern_bytes = pattern.encode('ascii')
		pattern_len = len(pattern_bytes)
		
		# Create a repeated pattern long enough to fill the canvas
		repeated_pattern = (pattern_bytes * ((len(self.data) // pattern_len) + 1))
		
		# Copy it to the canvas
		self.data[:] = repeated_pattern[:len(self.data)]
	
	def __str__(self) -> str:
		data_str = self.data.decode('ascii')
		result = []
		for i in range(0, len(data_str), self.width):
			result.append(data_str[i:i+self.width])
		return '\n'.join(result) + '\n'



def parse_args():
	parser = argparse.ArgumentParser(description='The Official ORSONOSRO Ascii Art Engine')
	
	parser.add_argument('--width', type=int, help='Canvas Width')
	parser.add_argument('--height', type=int, help='Canvas Height')
	parser.add_argument('--pattern', type=str, default='', help='Pattern used to fill the canvas')
	parser.add_argument('--load', help='Load from file (TODO)')
	parser.add_argument('--save', help='Save to file (TODO)')
	
	args = parser.parse_args()

	# TODO: implicitly determine canvas size from input
	if args.width is None:
		args.width = 1
	if args.height is None:
		args.height = 1
	
	return args


def main():
	args = parse_args()
	canvas = Canvas(args.width, args.height)
	
	canvas.fill(args.pattern)
	sys.stdout.write(str(canvas))
	
	return 0


if __name__ == "__main__":
	sys.exit(main())
