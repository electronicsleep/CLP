#!/usr/bin/env python

# Author: https://github.com/electronicsleep
# Date: 01/30/2017
# Purpose: Command Line Python Examples
# Released under the BSD license

from __future__ import print_function
import click
import subprocess
import time
import os


@click.command()
@click.option('-c', '--count', default=1, help='Number of iterations.')
@click.option('-v', '--verbose', default=True, is_flag=True, help='Print verbose output.')
def main(count, verbose):
    """ Example program that runs a specific command a number of times and scans output. """

    start = time.time()

    localtime = time.asctime(time.localtime(time.time()))
    print("Date:" + localtime)

    x = 0
    found_list = []

    for x in range(count):

        line_num = 0

        if verbose:
            click.echo("We are in the verbose mode.")

        print("#Python open file example")
        file_path = "data.txt"
        if os.path.exists(file_path):
          with open(file_path, 'rU') as f:
              for line in f:
                  line_num += 1
                  if 'bar' in line:
                      print("found bar")
                      found_list.append("found bar")
                  print(line.strip())
        else:
          print("Data file not found")

        print('lines: ' + str(line_num))
        print("#" * 10)

        line_num = 0
        exit(0)
        print("#Python subprocess example")
        command = 'ls -ltra'
        pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        for line in pipe.stdout:
            print(line.strip())
            line_num += 1

            if ".py" in line:
                if verbose:
                    print("found python file")
                found_list.append("found python file: " + line.strip())
            if '.txt' in line:
                if verbose:
                    print("found txt file")
                found_list.append("found txt file: " + line.strip())

        print('Lines: ' + str(line_num))

    print("Found List")
    for item in found_list:
        print("FOUND: " + item)

    print('Run: ', end='')
    print(x + 1)
    end = time.time()
    print("Runtime: ", end='')
    print(end - start)

if __name__ == '__main__':
    main()
