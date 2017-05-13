#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 01/30/2017
# Purpose: Command Line Python Examples
# Released under the BSD license

from fabric.api import env


def return_inventory():

    hn = ".example.com"
    env.roledefs = {
        'dev': ['dev' + hn],
        'prod': ['www' + hn],
        'mail': ['www', 'mail' + hn],
        'web': ['www' + hn],
    }
    env.roledefs['all'] = env.roledefs['dev'] + env.roledefs['prod'] + env.roledefs['mail'] + env.roledefs['web']

    return env.roledefs
