import json
class parser():
    def __init__(self):
        import json
        with open('../configs/vis_config.json') as json_file:
            global data
            data = json.load(json_file)
    def get(self):
        return data
