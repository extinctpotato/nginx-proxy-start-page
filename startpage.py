from nginxparser_eb import load
import os

class NGINX:
    def __init__(self, path):
        self.parsed = load(open(path))
    def locations(self):
        sift = []
        for i in range(len(self.parsed[0][1])):
            element_for_eval = self.parsed[0][1][i]

            if element_for_eval[0][0] == "location":
                for j in range(len(element_for_eval[1])):
                    if element_for_eval[1][j][0] == "proxy_pass":
                        sift.append(element_for_eval[0][1])
        return sift
