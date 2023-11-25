from restservice import RestClient
from models import *
import json


def main():
    serv = RestClient('api-link-here')
    
    resp = serv.get("/req")
    
    myEvent = Event.from_dict(resp)
    
    print(myEvent)

if __name__ == '__main__':
    main()