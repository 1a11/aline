import json
##c = {'header':{'versions':{'self':'0.1EB'},'libs':['SpeechRecognition','pyttsx3','pyaudio','gTTS','pypiwin32','Pillow','opencv-python','numpy','scipy','tensorflow-gpu']},\
##'body':{'akey':'a5d5d0d5-e582-4a99-8659-1677a8b7b237','activation_url':'https://protected-temple-64796.herokuapp.com/activate/','act':False}}
class parser():
    def __init__(self,config_name):
        import json
        with open(config_name) as json_file:
            global data
            data = json.load(json_file)
    def reload(self, config_name):
        global data
        with open(config_name) as json_file:
            data = json.load(json_file)
        return data['header']['versions']['self']
    def get(self):
        return data
    def check_versions(self):
        return data['header']['versions']
            
##with open('config.json', 'w') as outfile:
##    json.dump(c, outfile, indent=4)            
