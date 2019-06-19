from flask import Flask
from flask import request
import ast

app = Flask(__name__)

storage = []

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manager():
    if(request.method == "GET"):
        return "\n\n"+str(storage)+"\n\n"
    if(request.method == "POST"):
        storage.append(request.data)
        return "\n\n"+str(request.data)+"\n\n"
    if(request.method == "PUT"):
        try:
            request.data = ast.literal_eval(request.data)
            storage[request.data["index"]] = request.data["value"]
        except:
            return "EXCEPTION OCCURRED. INVALID INDEX: \n\n"+str(storage)+"\n\n"
        return "\n\n"+str(request.data["index"])+"\n"+str(request.data["value"])+"\n\n"
    if(request.method == "DELETE"):
        try:
            storage.pop(request.data["index"])
        except:
            return "EXCEPTION OCCURRED. INVALID INDEX: \n\n"+str(storage)+"\n\n"
        return "\n\n"+str(request.data["index"])+"\n\n"

if __name__ == '__main__':
    app.run()