from nginxparser_eb import load
from flask import Flask, render_template, request
import os, argparse

nsp = Flask(__name__)

def spsplit(line):
    allowed = ("sp-title", "sp-desc", "sp-icon")
    line_split = line.split(" ", 1)
    if line_split[0] in allowed:
        return {line_split[0] : line_split[1].replace("\"", "")}
    
class NGINX:
    def __init__(self, path):
        self.parsed = load(open(path))
    def locations(self):
        sift = []
        for i in range(len(self.parsed[0][1])):
            element_for_eval = self.parsed[0][1][i]
            block_dict = {}

            if element_for_eval[0][0] == "location":
                for j in range(len(element_for_eval[1])):
                    if element_for_eval[1][j][0] == "#":
                        decoration = spsplit(element_for_eval[1][j][1])
                        if decoration:
                            block_dict.update(decoration)
                    if element_for_eval[1][j][0] == "proxy_pass":
                        block_dict.update({"location":element_for_eval[0][1]})
                        sift.append(block_dict)
        return sift

@nsp.route("/")
def index():
    config = NGINX(arg.config)
    locations = config.locations()
    return render_template("index-template.html", loc = locations, loc_count = len(locations), host = request.headers.get("Host"))

def main():
    parser = argparse.ArgumentParser("nginx-startpage")
    parser.add_argument("config", type=str)
    parser.add_argument("--port", type=str, default=80)
    arg = parser.parse_args()
    nsp.run(host='0.0.0.0', debug = False, port=arg.port)

if __name__ == "__main__":
    main()
