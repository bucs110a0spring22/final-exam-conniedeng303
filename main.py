import requests
import json
import BirdrecordingAPI
import IpfastAPI



def main():
  bird = BirdrecordingAPI.BirdrecordingAPI()
  ip = IpfastAPI.IpfastAPI()
  names = bird.getname()
  for name in names:
    print(name)
  results_bird = bird.get()
  results_ip = ip.get()
  print("The bird we are looking at today is called" + BirdrecordingAPI[0] + "!")
  if bird.getcountry() == bird.getlocation():
    print("This bird is in your country! It knows your IP address, and is coming straight for your location. Run.")
  else:
    print("This bird does not reside in your country. It knows your IP address though.")

main()