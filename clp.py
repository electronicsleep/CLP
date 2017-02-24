#!/usr/bin/env python
from __future__ import print_function
import click
import subprocess
import six 

@click.command()
@click.option('-c', '--count', default=1, help='Number of iterations.')
@click.option('-v', '--verbose', is_flag=True, help='Print verbose output.')

def main(count, verbose):
    """ Example program that runs a specfic command a number of times and scans output. """

    for x in range(count):

        pipe = ''
        line_num = 0

        if verbose:
            click.echo("We are in the verbose mode.")

        print("#Python open file example")
        with open('data.txt', 'rU') as f:
            for line in f:
                line_num += 1
                if 'bar' in line:
                    print("found bar")
                print(line.strip())

        print('lines: ' + str(line_num))
        print("#" * 10)

        line_num = 0
        print("#Python subprocess example")
        pipe = subprocess.Popen('ls -ltra', shell=True, stdout=subprocess.PIPE)
        for line in pipe.stdout:
            print(line.strip())
            line_num += 1
            if verbose:
                if '.py' in line:
                    print("found python file")
                if '.txt' in line:
                    print("found txt file")

        print('Lines: ' + str(line_num))

    print('Run: ', end='')
    print(x + 1)

if __name__ == '__main__':
    main()
