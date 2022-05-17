import requests


class BirdrecordingAPI:
  def __init__(self, query = https://www.xeno-canto.org/api/2/recordings?query=troglodytes+troglodytes):
    self.api_url = "https://www.xenocanto.org/api/2"

  def getname(self):
    birdrecording = requests.get(self.api_url)
    response = birdrecording.json()
    if response.get("sp"):
      return response["sp"]
    else:
      return None
      
    def __str__(self):
      return self.api_url

  def getcountry(self):
    birdrecording = requests.get(self.api_url)
    response = birdrecording.json()
    if response.get('cnt'):
      return response['cnt']
    else:
      return None





     # def get(self):
     #  r = requests.get(self.url)
     #  #response is just a json dictonary of values after .json() call
     #  response = r.json()
     #  #check to make sure I got a question, i.e. results
     #  if response.get('results'):
     #      return response['results']
     #  else:
     #      return None
        