import sys
import os

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message):
        print(message)

        if message == 'working':
            #os.system('ls')
            return (True, os.system("st2 run core.remote hosts='10.54.158.195' username='root' private_key='/home/stanley/.ssh/id_rsa' cmd='cd /root ; python rabbitmqa$
        return (False, message)

