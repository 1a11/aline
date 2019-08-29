import zipfile
import os
import threading
import random
import requests
import progressbar
import json
import pyAesCrypt
import time
class updater():
    global bar
    def __init__(self):
        try:
            import zipfile
            import os
            import threading
            import random
            import requests
        except Exception as err:
            raise Exception(err)
           
    def unzip(self, path_to_zip_file):
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall('./software/')

    def download_file_from_google_drive(self, id, destination):
        URL = "https://docs.google.com/uc?export=download"
        
        session = requests.Session()

        response = session.get(URL, params = { 'id' : id }, stream = True)
        token = self.get_confirm_token(response)
        if token:
                params = { 'id' : id, 'confirm' : token }
                response = session.get(URL, params = params, stream = True)


        self.save_response_content(response, destination)    

    def get_confirm_token(self, response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(self, response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        return True

    def get(self, akey, skey, server):
        values = {'akey':akey,'skey':skey} # Send User
        r = requests.post(server, json=values)
        return(r.text)
    
    def rewrite(self, filename):
        f = open(filename, 'w')
        f.write('File content is deleted automatically.')
        f.close()
        os.remove(filename)

    def start(self):
        file_id = '1vb1yT47NOM7D9Xcky_6VyFJ-5bk7pO3L'
        destination = './config.json'
        u = updater()
        print('Downloading software...')
        u.download_file_from_google_drive(file_id, destination)
        print('Done.')
        print('Reading config.json...')
        with open('config.json') as json_file:
            data = json.load(json_file)
        print('Done.')
        print('Config version: {}'.format(data['header'][0]['version']))
        for i in range(100):
            print('')
        skey1 = input('Enter key part 1   ->    ')
        print('Move away from the computer and transfer control to the second person. You have 30 seconds for that.')
        time.sleep(15)
        for i in range(1000):
            print('')
        skey2 = input('Enter key part 2   ->    ')
        for i in range(1000):
            print('')
        print('Wait for keys verifying...')
        keypart2 = self.get(data['body'][0]['apikey'], skey1, data['body'][0]['server'])
        if keypart2 == skey2:
            keypart2 = ''
            skey2 = ''
            print('Done.')
            print('Downloading config...')
            file_id = '1AiS0D2szn-YNpdM0JsL7ER7XZdF_VKyl'
            u = updater()
            destination = './config2.json.aes'
            u.download_file_from_google_drive(file_id, destination)
            print('Done.')
            print('Decryptin file...')
            bufferSize = 64 * 1024
            password = '3bff8805-1e90-4c68-869e-3972c6354c97'
            pyAesCrypt.decryptFile("config2.json.aes", "config2.json", password, bufferSize)
            print('Done.')
            print('Reading config2.json...')
            with open('config2.json') as json_file:
                data = json.load(json_file)
            print('Done.')
            file_id = data['body'][0]['gkey']
            destination = './software.zip'
            u = updater()
            print('Downloading software...')
            u.download_file_from_google_drive(file_id, destination)
            file_id = ''
            
            self.rewrite("config2.json")
            self.rewrite("config2.json.aes")
            self.rewrite("data2.json")
            self.rewrite("config.json")
            print('Done.')
            print('Unpacking file archive...')
            self.unzip(destination)
            os.remove(destination)
            print('Done')
        else:
            print('One or two of your keys are incorrect. Please, check them and run that app once again.')
            time.sleep(15)
        
u = updater()
u.start()
        
        

