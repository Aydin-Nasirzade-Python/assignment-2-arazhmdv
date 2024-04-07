#import libraries here

def main():
  m = input('Enter a month [ex. March]: ')
  d = int(input('Enter the day [ex. 12]: '))
  
  if (m == 'March') and 21 <= d <= 31 or (m == 'April') and 1 <= d <= 19:
      print('Your zodiac sign is Aries')
  elif m == 'April' and 20 <= d <= 30 or m == 'May' and 1 <= d <= 20:
      print('Your zodiac sign is Taurus')
  elif m == 'May' and 21 <= d <= 31 or m == 'June' and 1 <= d <= 20:
      print('Your zodiac sign is Gemini')
  elif m == 'June' and 21 <= d <= 30 or m == 'July' and 1 <= d <= 22:
      print('Your zodiac sign is Cancer')
  elif m == 'July' and 23 <= d <= 31 or m == 'August' and 1 <= d <= 22:
      print('Your zodiac sign is Leo')
  elif m == 'August' and 23 <= d <= 31 or m == 'September' and 1 <= d <= 22:
      print('Your zodiac sign is Virgo')
  elif m == 'September' and 23 <= d <= 30 or m == 'October' and 1 <= d <= 22:
      print('Your zodiac sign is Libra')
  elif m == 'October' and 23 <= d <= 31 or m == 'November' and 1 <= d <= 21:
      print('Your zodiac sign is Scorpion')
  elif m == 'November' and 22 <= d <= 30 or m == 'December' and 1 <= d <= 21:
      print('Your zodiac sign is Sagittarius')
  elif m == 'December' and 22 <= d <= 31 or m == 'January' and 1 <= d <= 19:
      print('Your zodiac sign is Capricorn')
  elif m == 'January' and 20 <= d <= 31 or m == 'February' and 1 <= d <= 18:
      print('Your zodiac sign is Aquarius')
  elif m == 'February' and 19 <= d <= 29 or m == 'March' and 1 <= d <= 20:
      print('Your zodiac sign is Pisces')
  else:
      print('Either a month or a day is invalid!')
  pass

if __name__ == "__main__":
  main()
