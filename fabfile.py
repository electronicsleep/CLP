#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 01/30/2017
# Purpose: Command Line Python Examples
# Released under the BSD license

# fab -R test deploy

import time
import errno
import os

from termcolor import colored
from fabric.api import run, task
from inventory import *

print colored('Hello', 'cyan'), colored('Fabric', 'green')

run_error_text = "ERROR NOT RUNNING"

localtime = time.asctime(time.localtime(time.time()))
print("Date:" + localtime)

inv = return_inventory()

# Use all as default
if not len(env.roles):
    env.roles = ["all"]


@task
def deploy():
    """Deploy to environments"""
    run('echo test')
    output = run('hostname')

    if output.return_code != 0:
        print("Error")
        print(output)
        print(output.return_code)
    else:
        print(output.return_code)
        print("OK")


def mkdir_path(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


@task
def check_resources():
    """Check resource related info"""
    check_load()
    check_type()
    check_space()


def check_load():
    run('w')


def check_type():
    ret = run('uname -a')
    print ret


@task
def check_space():
    output = run('df -h')
    if output.return_code != 0:
        print("ERROR RUNNING COMMAND")
        error = "On %s: %s" % ("df -h1123", output.stderr)
        print(error)
        print(output.return_code)
        print("Run command error")
        exit(1)
    else:
        print("DISK SPACE:")
        print(output.text)


@task
def check_top():
    """Check top and write a report"""
    print "HOST:"
    print env.host
    output = run('top -n1 -b | head')

    host = env.host
    outputf = ""
    for line in output.splitlines():
        outputf = outputf + "[" + host + "] " + line + "\n"

    write_report(outputf)


def write_report(output):
    mkdir_path('reports')
    d = time.strftime("%Y%m%d-%H%M")
    f = open('reports/report-' + d + '.txt', 'a')
    f.write("\n\n" + output)
    f.close()


def check_fail2ban():
    output = run('ps -ef | grep fail2ban')
    if "pid" not in output:
        print colored(run_error_text, 'red')
        output = run('su - -c "service ntp fail2ban"')
        print(output)


def check_spamassassin():
    output = run('ps -ef | grep spamd')
    if "pid" not in output:
        print colored(run_error_text, 'red')
        output = run('su - -c "service spamd restart"')
        print(output)


def check_postfix():
    output = run('ps -ef | grep postfix')
    if "postfix/master" not in output:
        print colored(run_error_text, 'red')
        output = run('su - -c "service postfix restart"')
        print(output)


def check_nagios():
    output = run('ps -ef | grep nagios')
    if "cfg" not in output:
        print(colored(run_error_text, 'red'))
        output = run('su - -c "service nagios3 restart"')
        print(output)


def check_mysql():
    output = run('ps -ef | grep mysql')
    if "mysqld" not in output:
        print(colored(run_error_text, 'red'))
        output = run('su - -c "service mysql restart"')
        print(output)


def check_ntp():
    output = run('ps -ef | grep ntp')
    if "pid" not in output:
        print(colored("run_error_tex", 'red'))
        output = run('su - -c "service ntp restart"')
        print(output)
