import unittest, requests
from crudapi import app

class ApiTest(unittest.TestCase):
    base_url = 'http://localhost:5000/fileserver'
        
    def test_delete_audiofile(self):
        #----------------------- Test Data ------------------------
        audioFileType = 'podcast'
        audioFileID = 6
         #----------------------- Test Data ------------------------
        
        url = f'{self.base_url}/delete_file/{audioFileType}/{audioFileID}'
        resp=requests.post(url)
        self.assertEqual(resp.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()