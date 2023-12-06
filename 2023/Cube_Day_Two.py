from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5fa6068b32d9692241675c735649b6414d6d99b0e8205688c116514da56cba803c032182257f7f51f9f6b1e77e71cba71afdd400d3266c048a"
puzzle = Puzzle(year=2023, day=2)

def parse(puzzle_input):
  dic = {}
  listy = [str(line) for line in puzzle_input.split("\n")]
  for game in listy:
    round_list = []
    sep_colon = game.split(": ")
    sep_rounds = sep_colon[1].split("; ")
    for round in sep_rounds:
      round_dic = {}
      curr_col = ""
      curr_num = ""
      for s in round:
        if ord('0') <= ord(s) <= ord('9'):
          curr_num += str(s)
        elif ord('a') <= ord(s) <= ord('z'):
          curr_col += s
        if curr_col == "red":
          round_dic["R"] = int(curr_num)
          curr_num=""
          curr_col = ""
        elif curr_col == "green":
          round_dic["G"] = int(curr_num)
          curr_num = ""
          curr_col = ""
        elif curr_col == "blue":
          round_dic["B"] = int(curr_num)
          curr_num = ""
          curr_col = ""
      round_list.append(round_dic)
    dic[sep_colon[0]] = round_list
  return dic

def part1(puzzle_input, maxr=12, maxg=13, maxb=14):
  result = []
  counter = 1
  for game, rounds in (puzzle_input).items():
    valid = True
    for round in rounds:
      if valid == False:
        break
      for key, value in round.items():
        if key == "R":
          if value <= maxr:
            valid = True
          else:
            valid = False
            break
        elif key == "G":
          if value <= maxg:
            valid = True
          else:
            valid = False
            break
        else:
          if value <= maxb:
            valid = True
          else:
            valid = False
            break
    if valid == True:
      result.append(counter)
    counter+=1
  return print(sum(result))

# print(part1(puzzle.input_data))
part1(parse(puzzle.input_data))
#part1(parse("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"))

#print(parse("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"))
# {Game 1: [{B:1, R:2, G:2}, {B:1, R:2, G:4}, {B:1, R:2, G:2}]}
