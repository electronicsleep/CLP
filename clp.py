import click
import subprocess

@click.command()
@click.option('--count', default=1, help='Number of iterations.')
@click.option('--verbose', is_flag=True, help='Print verbose output.')

def main(count, verbose):
    """Program that runs a specfic command for count iterations."""

    for x in range(count):

        pipe = ''
        line_num = 0

        if verbose:
            click.echo("We are in the verbose mode.")

        pipe = subprocess.Popen('cat data.txt', shell=True, stdout=subprocess.PIPE)
        for line in pipe.stdout:
            if 'bar' in line:
                print("found bar")
            print(line.strip())
            line_num += 1


        print 'lines: ' + str(line_num)

        print "#" * 10 

        line_num = 0
        pipe = subprocess.Popen('ls -ltra', shell=True, stdout=subprocess.PIPE)
        for line in pipe.stdout:
            print(line.strip())
            line_num += 1
            if verbose:
                if '.py' in line:
                    print "found python file"
                if '.txt' in line:
                    print "found txt file"

        print 'lines: ' + str(line_num)

    print 'RUN:',
    print x + 1


if __name__ == '__main__':
    main()
