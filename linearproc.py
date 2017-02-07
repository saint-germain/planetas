import subprocess


def bash_command(cmd):
    p=subprocess.Popen(['/bin/bash', '-c', cmd])
    print p.communicate()

bash_command('gfortran -o analisis1 analisis1.f; ./analisis1')
bash_command('gfortran -o analisis2 analisis2.f; ./analisis2')
bash_command('gfortran -o analisis3 analisis3.f; ./analisis3')
bash_command('gfortran -o analisis4 analisis4.f; ./analisis4')
