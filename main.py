import requests
import random
import BirdrecordingsAPI
import IpfastAPI

# def main():
  # birdapi = BirdrecordingsAPI.BirdrecordingsAPI()
  # birds = birdapi.get()
  # species is a Recordings object inside the recordings list
  # print(species(birds[random.randrange(1,len(birds)+1]['cnt'])

                
def main():
  birdapi = BirdrecordingsAPI.BirdrecordingsAPI()
  ipapi = IpfastAPI.IpfastAPI()
  birds = birdapi.get()
  user_ip = ipapi.getIP()
  user_country = ipapi.get_country()
  bird_country = (birds[random.randrange(1,len(birds)+1)]['cnt'])
  print("Troglodytes Troglodytes genus birds are one of the most common birds found in every continent. In fact, lets pick a random bird and see if it's near you:")
  if str(user_country) == str(bird_country):
    print("Looks like a Troglodytes Troglodytes is near you. It even knows your IP address!" + user_ip + "It's coming for you. Run")
  else:
    print("Looks like a Troglodytes Troglodytes does not live in your region. This particular bird is living in" + bird_country + "It knows your IP address though. It's" + user_ip + ". It's coming to you.")


main()

