import requests
import json

class IpfastAPI:

  def __init__(self,format = "json", location = "True"):
    self.url = f'https://ip-fast.com/api/ip/?format={format}&location={location}'

  def getIP(self):
    r = requests.get(self.url)
    data = r.json()
    if data.get('ip'):
      print(data['ip'])
      return data['ip']
    else:
      return None
      
  def get_country(self):
    r = requests.get(self.url)
    data = r.json()
    if data.get('country'):
      print(data['country'])
      return data['country']
    else:
      return None