import requests


class BirdrecordingAPI:
  def __init__(self, query = "https://www.xeno-canto.org/api/2/recordings?query=bearded+bellbird+q:A", ):
    self.url = "https://www.xenocanto.org/api/2"
    query = "https://www.xeno-canto.org/api/2/recordings?query=bearded+bellbird+q:A"
    birdresponse: requests.get("https://www.xenocanto.org/api/2")

  def getname(self):
    birdrecording = requests.get(self.url)
    response = birdrecording.json
    if response.get('sp')
      return response['sp']
    else:
      return None

  def getcountry(self):
    birdrecording = requests.get(self.url)
    response = birdrecording.json
    if response.get('cnt')
      return response['cnt']
    else:
      return None

``



     # def get(self):
     #  r = requests.get(self.url)
     #  #response is just a json dictonary of values after .json() call
     #  response = r.json()
     #  #check to make sure I got a question, i.e. results
     #  if response.get('results'):
     #      return response['results']
     #  else:
     #      return None
        