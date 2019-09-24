from nginxparser_eb import load
import os

class NGINX:
    def __init__(self, path):
        self.parsed = load(open(path))
    def locations(self):
        sift = []
        for i in range(len(self.parsed[0][1])):
            element_for_eval = self.parsed[0][1][i][0]
            if element_for_eval[0] == "location":
                sift.append(element_for_eval[1])
        return sift
