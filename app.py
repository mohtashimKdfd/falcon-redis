import json
import falcon


class Home:
    def on_get(self, req, resp):
        
        resp.body = json.dumps("Helooo")


api = falcon.App()

api.add_route('/',Home())