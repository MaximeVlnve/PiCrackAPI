from threading import Thread
from subprocess import Popen, PIPE

WORDLIST_PATH = "wordlist.txt"
ROOT_PASSWORD = "grandmastersplinter"

def commandAsRoot(command):
    print("%------"+command+"------%")
    p = Popen(["sudo","-S"] + command.split(),stdin=PIPE,stdout=PIPE,stderr=PIPE,universal_newlines=True)
    r = p.communicate(ROOT_PASSWORD + "\n")
    if r[0] == '':
        return "NOT FOUND"
    
    return r[0]

class BruteForceThread(Thread):
    def __init__(self,network):
        Thread.__init__(self)
        self.network = network
    
    def run(self):
        command = "aircrack-ng -a2 -b %s -w %s %s -q" % (self.network.bssid, WORDLIST_PATH, self.network.file.path)
        print(command)
        r = commandAsRoot(command)
        print(r)
        if r == "NOT FOUND":
            self.network.status = 'not_cracked'
        else:
            self.network.password = r.split(' ')[3]
            self.network.status = 'cracked'
        self.network.save()