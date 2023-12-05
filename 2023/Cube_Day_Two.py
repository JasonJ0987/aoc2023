from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5fa6068b32d9692241675c735649b6414d6d99b0e8205688c116514da56cba803c032182257f7f51f9f6b1e77e71cba71afdd400d3266c048a"
puzzle = Puzzle(year=2023, day=2)

def parse(puzzle_input):
  return [str(line) for line in puzzle_input.split("\n")]

print(parse(puzzle.input_data))
