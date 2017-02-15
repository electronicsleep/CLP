import click
import subprocess

@click.command()
@click.option('--count', default=1, help='Number of iterations.')
@click.option('--name', prompt='Your name', help='Who are you?')
@click.option('--verbose', is_flag=True, help='Print verbose output.')

def hello(count, name, verbose):
    """Simple program that greets NAME for a total of COUNT times."""

    pipe = ''
    line_num = 0

    print "#" * 10 

    if verbose:
        click.echo("We are in the verbose mode.")

    pipe = subprocess.Popen('cat data.txt', shell=True, stdout=subprocess.PIPE)
    for line in pipe.stdout:
        print(line.strip())
        line_num += 1

    print 'lines: ' + str(line_num)

    print "#" * 10 

    line_num = 0
    pipe = subprocess.Popen('ls -ltra', shell=True, stdout=subprocess.PIPE)
    for line in pipe.stdout:
        print(line.strip())
        if '.py' in line:
            print "found python file"
        if '.txt' in line:
            print "found txt file"
        line_num += 1

    print 'lines: ' + str(line_num)

    print "#" * 10 

    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
