from requests import Session

class Greynoise:

    def __init__(self, api_key):
        self.key = api_key
        self.base_url = 'https://enterprise.api.greynoise.io/v2/'
        self._session = Session()

    def _request(self, function, params):
        headers = {
            'Key': self.key,
        }
        response = self._session.get(self.base_url + function, params=params, headers=headers)
        return response.json()
    
    def noise_bulk(self):
        offset = 0

        ips = []
        while True:
            data = self._request('noise/bulk', {
                'offset': offset,
            })
            
            if 'noise_ips' in data:
                ips.extend(data['noise_ips'])

            # We've grabbed all available data
            if data['complete']:
                break

            offset = data['offset']
        
        return ips
