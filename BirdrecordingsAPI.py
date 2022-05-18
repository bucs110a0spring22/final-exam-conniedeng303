import requests

class BirdrecordingsAPI:
  
  def __init__(self,query = "troglodytes+troglodytes"):
    self.url =f'https://www.xeno-canto.org/api/2/recordings?query={query}'

  def get(self):
    r = requests.get(self.url)
    data = r.json()
    if data.get('recordings'):
      return data['recordings']
    else:
      return None