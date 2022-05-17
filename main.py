import requests
from BirdrecordingsAPI import getcountry()
from IpfastAPI import getlocation()



def main():
  bird = BirdrecordingsAPI.BirdrecordingsAPI()
  ip = IpfastAPI.IpfastAPI()
  results_bird = bird.get()
  results_ip = ip.get()

  print("The bird we are looking at today is called" + sp + "!")
  if getcountry() == getlocation(): OR
  if cnt == country:
    print("This bird is in your country! It knows your IP address, and is coming straight for your location. Run.")
  else:
    print("This bird does not reside in your country. It knows your IP address though.")

main()