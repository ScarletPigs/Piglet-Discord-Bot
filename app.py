from restservice import RestClient
import json


def main():
    serv = RestClient('api-link-here')
    
    resp = serv.get("/req")
    
    print(json.dumps(resp, indent=4))

if __name__ == '__main__':
    main()