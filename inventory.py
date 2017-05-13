#!/usr/bin/env python
# Author: https://github.com/electronicsleep
# Date: 01/30/2017
# Purpose: Command Line Python Examples
# Released under the BSD license

from fabric.api import env


def return_inventory():

    hn = ".example.com"
    env.roledefs = {
        'db': ['www' + hn],
        'dev': ['dev' + hn],
        'web': ['www' + hn],
        'mon': ['mon' + hn],
        'prod': ['www' + hn],
        'mail': ['mail' + hn],
    }
    for roles in env.roledefs:
        env.roledefs['all'] += roles

    return env.roledefs
