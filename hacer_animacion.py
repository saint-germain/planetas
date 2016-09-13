import numpy as np
import matplotlib.pyplot as plt
import os
import sys
filename=sys.argv[1]
command = 'awk \'{{print $1}}\' {} | uniq -c > indices.txt'.format(filename)
os.system(command)
ind=np.loadtxt('indices.txt',skiprows=1)
rawdata=np.loadtxt(filename,skiprows=1)
ncols=6
myrange=len(ind)
figure_list = ''
ii=0
trange=ind[:myrange,0].sum()
radmax=rawdata[:trange,5].max()
eradcm=6.37e8
for j in np.arange(myrange):
    plt.xlim(0,rawdata[:trange,2].max()+0.2)
    plt.ylim(0,rawdata[:trange,4].max()+0.2)
    plt.ylim(0,3)
    data=np.zeros((ind[j,0],ncols))
    for i in range(int(ind[j,0])):
        for k in range(ncols):
            data[i,k]=rawdata[ii,k]
        ii=ii+1
    plt.scatter(data[:,2],data[:,4],s=50*data[:,5],c=data[:,5]/eradcm,cmap='cubehelix',vmin=0,vmax=radmax/eradcm)   
    plt.colorbar(label='Planet radius (R_Earth)');
    plt.xlabel('Semi-major axis (AU)')
    plt.ylabel('Planet mass (M_Earth)')
    plt.title('Time=%e' % data[i,1])
    figure_name='plot%06d.png' % j
    plt.savefig(figure_name)
    figure_list = figure_list + ' {} '.format(figure_name)
    plt.close() 
for i in range(15):    
    figure_list = figure_list+ ' {} '.format(figure_name)      
command = 'convert -delay 10 -loop 0 {}'.format(figure_list)+' animation_{}.gif'.format(filename[:-4])
os.system(command)
command = 'rm *.png'
os.system(command)
