#import libraries here

def main():
  il = int(input('Enter the year [ex. 2021]: '))
  
  if il < 0:
      b = 'Invalid year!'
  elif il % 12 == 0:
      b = 'Monkey'
  elif il % 12 == 1:
      b = 'Rooster'
  elif il % 12 == 2:
      b = 'Dog'
  elif il % 12 == 3:
      b = 'Pig'
  elif il % 12 == 4:
      b = 'Rat'
  elif il % 12 == 5:
      b = 'Ox'
  elif il % 12 == 6:
      b = 'Tiger'
  elif il % 12 == 7:
      b = 'Hare'
  elif il % 12 == 8:
      b = 'Dragon'
  elif il % 12 == 9:
      b = 'Snake'
  elif il % 12 == 10:
      b = 'Horse'
  elif il % 12 == 11:
      b = 'Sheep'
  print(f'{il} is the year of the {b}')

  pass

if __name__ == "__main__":
  main()
