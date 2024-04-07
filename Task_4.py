#import libraries here

def main():
  il = int(input('Enter the year [ex. 2021]: '))
  
  if il < 0:
      print('Invalid year!')
  elif il % 12 == 0:
      print(f'{il} is the year of the Monkey')
  elif il % 12 == 1:
      print(f'{il} is the year of the Rooster')
  elif il % 12 == 2:
      print(f'{il} is the year of the Dog')
  elif il % 12 == 3:
      print(f'{il} is the year of the Pig')
  elif il % 12 == 4:
      print(f'{il} is the year of the Rat')
  elif il % 12 == 5:
      print(f'{il} is the year of the Ox')
  elif il % 12 == 6:
      print(f'{il} is the year of the Tiger')
  elif il % 12 == 7:
      print(f'{il} is the year of the Hare')
  elif il % 12 == 8:
      print(f'{il} is the year of the Dragon')
  elif il % 12 == 9:
      print(f'{il} is the year of the Snake')
  elif il % 12 == 10:
      print(f'{il} is the year of the Horse')
  elif il % 12 == 11:
      b = 'Sheep'
      print(f'{il} is the year of the Sheep')

  pass

if __name__ == "__main__":
  main()
