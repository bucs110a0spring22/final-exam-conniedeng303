import requests

class IpfastAPI:

  def __init__(self,format = "json", location = "True"):
    self.api_url = f'https://ip-fast.com/api/ip/?format={format}&location={location}'

  def __str__(self):
    return self.api_url

  def getIP(self):
    r = requests.get(self.api_url)
    data = r.json()
    if data.get('ip'):
      print(data['ip'])
      return data['ip']
    else:
      return None
      
  def get_country(self):
    r = requests.get(self.api_url)
    data = r.json()
    if data.get('country'):
      print(data['country'])
      return data['country']
    else:
      return None