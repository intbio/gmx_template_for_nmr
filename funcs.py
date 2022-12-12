import os
import urllib.request
import json
import nglview as nv
import MDAnalysis as mda


def view_nucl(*args,gui=False,chconv={},selection='all'):
    ch_conv={'A':'A','B':'B','C':'C','D':'D','E':'E','F':'F','G':'G','H':'H','I':'I','J':'J'}
    ch_conv.update(chconv)
    if(isinstance(args[0],mda.Universe)):
        nuclMD=args[0]
    else:
        nuclMD=mda.Universe(*args)
    #prot = nuclMD.select_atoms("protein")
    sel=nuclMD.select_atoms(selection)
    show=nv.show_mdanalysis(sel,gui=gui)
    show.representations = [
    {"type": "cartoon", "params": {
        "sele": ":%s :%s"%(ch_conv['A'],ch_conv['E']), "color": 0x020AED,"aspectRatio":2, "radius":1.5,"radiusSegments":1,"capped":1
    }},
    {"type": "cartoon", "params": {
        "sele": ":%s :%s"%(ch_conv['B'],ch_conv['F']), "color": "green","aspectRatio":2, "radius":1.5,"radiusSegments":1,"capped":1
    }},
    {"type": "cartoon", "params": {
        "sele": ":%s :%s"%(ch_conv['C'],ch_conv['G']), "color": 0xE0F705,"aspectRatio":2, "radius":1.5,"radiusSegments":1,"capped":1
    }},
    {"type": "cartoon", "params": {
        "sele": ":%s :%s"%(ch_conv['D'],ch_conv['H']), "color": 0xCE0000,"aspectRatio":2, "radius":1.5,"radiusSegments":1,"capped":1
    }},
    {"type": "cartoon", "params": {
        "sele": "nucleic", "color": "grey","aspectRatio":2, "radius":1.5,"radiusSegments":1,"capped":1
    }},
    {"type": "base", "params": {
        "sele": "nucleic", "color": "grey",
    }},
    ]
    show.camera = 'orthographic'
    return show


def get_files_from_git(gitapiurl,savefoldername):
    os.mkdir(savefoldername)
    json_url = urllib.request.urlopen(gitapiurl)
    data = json.loads(json_url.read())
    for d in data:
        if(d['type']=='file'):
            print("Downloading "+os.path.join(savefoldername,d['name']))
            urllib.request.urlretrieve(d['download_url'],os.path.join(savefoldername,d['name']))
        if(d['type']=='dir'):
            get_files_from_git(d['url'],os.path.join(savefoldername,d['name']))

  
def plot_plumed(filename,figsize=(5,5),colormap='Set1', bg_color='lightgray',plot=True,col2plot=False,xlim=False,silent=False,multi=1,xmult=1,ymult=1,xlabel=None,ylabel=None):
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError as e:
        print('[!] The required Python libraries could not be imported:', file=sys.stderr)
        print('\t{0}'.format(e))
        sys.exit(1)
    num_data=[]
    with open(filename,'r') as fhandle:
        for line in fhandle:
            line = line.strip()
            if line.startswith('#!'):
                l=line[2:].strip()
                if l.startswith('FIELDS'):
                    l2=l[6:].strip()
                    labels=l2.split()
                    if(not silent):
                        print("Labels found:",labels)
            else:
                if(len(line.split())>1):
                    num_data.append(list(map(float, line.split())))
    data=np.array(num_data)
    
    #n_series=1.0
    ndata=len(labels)-1
    if plot:
        grid=[1+ndata//3,3]
        plt.figure(figsize=(grid[1]*figsize[0],grid[0]*figsize[1]))
        if(not col2plot):
            col2plot=range(1,ndata+1)
        for i in col2plot:
            ax=plt.subplot(*grid, i)
            #color_map = getattr(plt.cm, colormap)
            #color_list = color_map(np.linspace(0, 1, n_series))
            #print(np.linspace(0, 1, n_series))
            #print(color_list)
            for k in range(multi):
                ax.plot(data[k::multi,0]*xmult, data[k::multi,i]*ymult,label="%d"%k)
            if(xlim):
                ax.set_xlim(*xlim)


    # Formatting Labels & Appearance
            if(xlabel):
                ax.set_xlabel(xlabel)
            else:
                ax.set_xlabel(labels[0])
            if(ylabel):
                ax.set_ylabel(ylabel)
            else:
                ax.set_ylabel(labels[i])
            ax.set_facecolor(bg_color)
            ax.grid(True)
        plt.legend()
        plt.show()
    return data