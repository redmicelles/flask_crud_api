import unittest, json, requests
from crudapi import app

class ApiTest(unittest.TestCase):
    base_url = 'http://localhost:5000/fileserver'
    
    def test_create_audiofile(self):
        #-----------------------Test Data ------------------------
        data_ = {
                        "audioFileType": "song",
                        "audioFileMetadata": {
                        "name": "To God be the Glory",
                        "duration": "2",
                        "uploaded_time":"2021-04-05 11:05:25"
                        }
                }
        #----------------------- Test Data ------------------------
        
        url = f'{self.base_url}/create_file'
        resp=requests.post(url, data=json.dumps(data_), headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)
        
    
if __name__ == '__main__':
    unittest.main()