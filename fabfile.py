#!/usr/bin/python
#fab -R dev deploy
import time

from termcolor import colored

print colored('Hello', 'cyan'), colored('Fabric', 'green')

from fabric.api import settings,run,put,task,hide
from fabric.api import env,execute,hosts,sudo

#from inventory import *

# Update host roles
env.roledefs = {
    'dev': ['www.yourideaspace.com'],
    'production': ['prod-web1', 'prod-web2'],
    'mail': ['mail1', 'mail2'],
    'web': ['prod-web1', 'prod-web2'],
    'all' : ['dev'] + ['Prod']
}

# Use all as default
if not len(env.roles):
    env.roles = ["all"]

@task
def deploy():
    """Deploy to environments"""
    run('echo test')
    output = run('hostname')

    if(output.return_code != 0):
        print("Error")
        print(output)
        print(output.return_code)
        #raise Exception(error) 
    else:
        print(output.return_code)
        print("OK")
