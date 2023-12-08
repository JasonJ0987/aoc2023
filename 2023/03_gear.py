from aocd.models import Puzzle
import os
os.environ["AOC_SESSION"] = "53616c7465645f5fa6068b32d9692241675c735649b6414d6d99b0e8205688c116514da56cba803c032182257f7f51f9f6b1e77e71cba71afdd400d3266c048a"
puzzle = Puzzle(year=2023, day=3)

def parse(data):
  return [row for row in data.split('\n')]


def part1(data):
  result = []
  for row in range(len(data)-1):
    for col in range(len(data[row])):
      if ord('0') <= ord(data[row][col]) <= ord('9') or ord(data[row][col]) == ord('.'):
        pass
      else:
        # print(data[row-1][col-1], data[row-1][col], data[row-1][col+1], data[row][col-1], data[row][col+1], data[row+1][col-1], data[row+1][col], data[row+1][col+1])
        # represents which sections are touching the symbol
        for r in range(-1, 2):
          ready = True
          # initialize algorithm
          # go through every section of the 3x3 grid around the target
          for c in range(-1, 2):
            if ord('0') <= ord(data[row+r][col+c]) <= ord('9') and ready:
              i = 1
              j = 1
              num = data[row+r][col+c]
              while True:
                # detect flanking numbers to see full digit
                if col+c-i > -1 and ord('0') <= ord(data[row+r][col+c-i]) <= ord('9'):
                  num = data[row+r][col+c-i] + num
                  i += 1
                elif col+c+j < len(data) and ord('0') <= ord(data[row+r][col+c+j]) <= ord('9'):
                  num = num + data[row+r][col+c+j]
                  j += 1
                else:
                  result.append(int(num))
                  ready = False
                  break
            elif ord(data[row+r][col+c]) == ord('.') or data[row+r][col+c] == data[row][col]:
              ready = True
              # reinitialize algorithm when there is a dot or at the center of the target
  return print(sum(result))



# while loop checking if neighbours are numbers then use a temp variable to hold current digit? two pointers?
# solve for a way to figure out the full digit that is touching the symbol
# print(parse(puzzle.input_data)) test
# parse("467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..")
# part1(parse("467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."))
# part1(parse(puzzle.input_data))


def part2(data):
  # can prolly use a similar system
  result = []
  for row in range(len(data)-1):
    for col in range(len(data[row])):
      if ord(data[row][col]) == ord('*'):
        is_gear = []
        for r in range(-1, 2):
          ready = True
          for c in range(-1, 2):
            if ord('0') <= ord(data[row+r][col+c]) <= ord('9') and ready:
              i = 1
              j = 1
              num = data[row+r][col+c]
              while True:
                if col+c-i > -1 and ord('0') <= ord(data[row+r][col+c-i]) <= ord('9'):
                  num = data[row+r][col+c-i] + num
                  i += 1
                elif col+c+j < len(data) and ord('0') <= ord(data[row+r][col+c+j]) <= ord('9'):
                  num = num + data[row+r][col+c+j]
                  j += 1
                else:
                  is_gear.append(int(num))
                  ready = False
                  break
            elif ord(data[row+r][col+c]) == ord('.') or data[row+r][col+c] == data[row][col]:
              ready = True
        if len(is_gear) == 2:
          cur = 1
          for gear in is_gear:
            cur = cur*gear
          result.append(cur)
      else:
        pass
  return print(sum(result))

part2(parse("467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."))
part2(parse(puzzle.input_data))
