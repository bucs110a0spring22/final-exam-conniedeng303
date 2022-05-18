import requests

class BirdrecordingsAPI:
  
  def __init__(self,query = "troglodytes+troglodytes"):
    self.api_url =f'https://www.xeno-canto.org/api/2/recordings?query={query}'

  def __str__(self):
    return self.api_url

  def get(self):
    r = requests.get(self.api_url)
    data = r.json()
    if data.get('recordings'):
      return data['recordings']
    else:
      return None