#Libraries and main variables initialized
import MDAnalysis as mda
from MDAnalysis.analysis import align
from MDAnalysis.analysis.rms import rmsd
import numpy as np
import urllib.request, json
import os
import re
import nglview as nv
from funcs import get_files_from_git
from funcs import view_nucl
from IPython.display import Markdown, display

#Reloading funcs if changed
from importlib import reload 
import funcs,config
reload(funcs)
reload(config)
import pickle

from IPython.display import Markdown, display
from config import folder,descr,pname,ssh_host,set_gmx_cmd,prot_url,ff_name,ffurl,gmx_eq_cmd,gen_parallel_tpr,run_profile,noappend,movtitle

print("Folder set to   : ",folder)
print("Project name    : ",pname)
print("SSH host set to :",ssh_host)
print("GMX cmd set with:",set_gmx_cmd)
print("Force field     :",ff_name)
print("Force field URL :",ffurl)
print("Run profile     :",run_profile)
