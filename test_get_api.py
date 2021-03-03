import unittest, requests
from crudapi import app

class ApiTest(unittest.TestCase):
    base_url = 'http://localhost:5000/fileserver'
    def test_get_audio_file(self):
        #-----------------------Test Data ------------------------
        audioFileType = 'song'
        audioFileID = 14
        #-----------------------Test Data ------------------------
        
        url = f'{self.base_url}/get_file/{audioFileType}/{audioFileID}'
        resp=requests.get(url)
        self.assertEqual(resp.status_code, 200)
        
    def test_get_all_audio_file(self):
        #-----------------------Test Data ------------------------
        audioFileType = 'podcast'
        #-----------------------Test Data ------------------------
        
        url = f'{self.base_url}/get_file/{audioFileType}'
        resp=requests.get(url)
        self.assertEqual(resp.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()