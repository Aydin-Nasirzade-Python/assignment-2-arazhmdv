#import libraries here

def main():
  a = float(input("Enter the wavelength in nm: "))
  
  if 380 <= a < 450:
      b = "Violet"
  elif 450 <= a < 495:
      b = "Blue"
  elif 495 <= a < 570:
      b = "Green"
  elif 570 <= a < 590:
      b = "Yellow"
  elif 590 <= a < 620:
      b = "Orange"
  elif 620 <= a <= 750:
      b = "Red"
  else:
      b = "Invalid input!"
  
  print(f"The relevant color is {b}")

  pass

if __name__ == "__main__":
  main()
