import subprocess

from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(2)

def bash_command(cmd):
    p=subprocess.Popen(['/bin/bash', '-c', cmd])
    print p.communicate()



inst = ['gfortran -o analisis1 analisis1.f; ./analisis1'
,'gfortran -o analisis2 analisis2.f; ./analisis2'
,'gfortran -o analisis3 analisis3.f; ./analisis3'
,'gfortran -o analisis4 analisis4.f; ./analisis4'
  ]
results=pool.map(bash_command,inst)
pool.close()
pool.join()
