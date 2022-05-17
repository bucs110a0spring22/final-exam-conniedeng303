import requests
import json

response = requests.get('https://ip-fast.com/api/ip/')
print(response.text)


class IpfastAPI:
  def __init__(self,format = json, location = True):
    self.url = "https://ip-fast.com/api/ip/?format=json&location=True"
    
  def getlocation(self):
    iplocation = requests.get(self.url)
    response = iplocation.json
    if response.get('Country'):
      return response['Country']
    else:
      return None
    
  def __str__(self):
    return self.url

  #   `
  # def get(self):
  #     r = requests.get(self.url)
  #     #response is just a json dictonary of values after .json() call
  #     response = r.json()
  #     #check to make sure I got a question, i.e. results
  #     if response.get('results'):
  #         return response['results']
  #     else:
  #         return None

  # def change_category(self, category):
  #     pass
  #     #self.url = #...