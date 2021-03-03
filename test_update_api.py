import unittest, json, requests
from crudapi import app

class ApiTest(unittest.TestCase):
    base_url = 'http://localhost:5000/fileserver'
    
    def test_update_audiofile(self):
        #----------------------- Test Data ------------------------
        audioFileType = 'song'
        audioFileID = 14
        data_ = {
                        "audioFileType": "song",
                        "audioFileMetadata": {
                        "name": "Amazing Grace",
                        "duration": "15",
                        "uploaded_time":"2021-04-05 11:05:25"
                        }
                }
         #----------------------- Test Data ------------------------
        
        url = f'{self.base_url}/update_file/{audioFileType}/{audioFileID}'
        resp=requests.post(url, data=json.dumps(data_), headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)

if __name__ == '__main__':
    unittest.main()