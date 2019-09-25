from nginxparser_eb import load
import os

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
