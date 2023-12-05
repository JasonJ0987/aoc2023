from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5fa6068b32d9692241675c735649b6414d6d99b0e8205688c116514da56cba803c032182257f7f51f9f6b1e77e71cba71afdd400d3266c048a"
puzzle = Puzzle(year=2023, day=1)

def parse(puzzle_input):
  return [str(line) for line in puzzle_input.split()]


def part1(data):
  converted_num = []
  for line in data:
    l, r = 0, len(line)-1
    temp_num = ""
    while l != None:
      if is_num(line[l]):
        temp_num += line[l]
        l = None
      else:
        l += 1
    while r != None:
      if is_num(line[r]):
        temp_num += line[r]
        r = None
      else:
        r -= 1
    converted_num.append(int(temp_num))
  print(sum(converted_num))

def is_num(c):
  return (ord("0") <= ord(c) <= ord("9"))
def is_letternum(c):
  hmap = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
  for key in hmap.keys():
    if key in c:
      return hmap[key]

# part1(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"])
# part1(parse(puzzle.input_data))

def part2(data):
  converted_num = []
  for line in data:
    l, r = 0, len(line)-1
    poss_numl = ""
    poss_numr = ""
    current_num = ""
    while l != None:
      if is_num(line[l]):
        current_num += line[l]
        l = None
        break
      poss_numl += line[l]
      if is_letternum(poss_numl) == None:
        l += 1
      else:
        current_num += is_letternum(poss_numl)
        l = None
    while r != None:
      if is_num(line[r]):
        current_num += line[r]
        r = None
        break
      poss_numr = line[r] + poss_numr
      if is_letternum(poss_numr) == None:
        r -= 1
      else:
        current_num += is_letternum(poss_numr)
        r = None
    converted_num.append(int(current_num))
  return print(sum(converted_num))

part2(parse("two1nine eightwothree abcone2threexyz xtwone3four 4nineeightseven2 zoneight234 7pqrstsixteen"))
part2(parse(puzzle.input_data))
